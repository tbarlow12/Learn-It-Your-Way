import pdb
import json
from data_tools import loading
from operator import itemgetter


def get_features(format,d):
    form_data = []
    for key in d:
        form_data.append([format[key]['index'],key,d[key]])
    sorted(form_data,key=itemgetter(0))
    features = []
    for t in form_data:
        if len(format[t[1]]['vals_mapping']) == 0:
            #number
            try:
                features.append(int(t[2]))
            except ValueError:
                features.append(float(t[2]))
        else:
            features.append(format[t[1]]['vals_mapping'][t[2]])
    return [features]

def numeric_labels_features(csv):
    with open(csv) as f:
        lines = f.readlines()
        titles = lines[0]
        features = []
        labels = []
        for instance in lines[1:]:
            items = instance.split(',')
            features.append([float(x) for x in items[:-1]])
            labels.append(float(items[-1]))        
        return features, labels, titles

def get_data_types(line):
    data_types = []
    for item in line:
        try:
            x = float(item)
            data_types.append('num')
        except ValueError:
            data_types.append('str')
    return data_types

categorical_limit = 2

def is_categorical(instances):
    categorical = []
    all_distinct_vals = []
    for i in range(0,len(instances[0])):
        distinct_vals = set([line[i] for line in instances])
        all_distinct_vals.append(distinct_vals)
        if len(distinct_vals) <= categorical_limit:
            categorical.append(1)
        else:
            categorical.append(0)
    text_indices = get_text_indices(instances)
    for index in text_indices:
        categorical[index] = 1
    return categorical, all_distinct_vals, text_indices

def serialize_format(id, titles, instances):
    categorical, distinct_vals, text_indices = is_categorical(instances)
    format = {}
    mappings = {}
    cat_indices = []
    for i in range(0,len(categorical)):
        data_type = 'num'
        if i in text_indices:
            data_type = 'str'
        mapping = {}
        if categorical[i] == 1:
            cat_indices.append(i)
            mapping = {}
            j = 0
            for item in distinct_vals[i]:
                mapping[item] = j
                j += 1
            mappings[i] = mapping
        format[titles[i]] = {
            'index': i,
            'datatype': data_type,
            'is_categorical': categorical[i],
            'vals_mapping': mapping
        }
    
    return cat_indices, mappings, format

def encode_instances(instances,cat_indices,mappings):
    for instance in instances:
        for index in cat_indices:
            instance[index] = mappings[index][instance[index]]
        for i in range(0,len(instance)):
            try:
                instance[i] = int(instance[i])
            except ValueError:
                instance[i] = float(instance[i])

def generic_labels_features(id, csv):
    with open(csv, encoding='utf-8-sig') as f:
        lines = [line.strip().split(',') for line in f.readlines()]
        titles = lines[0]
        instances = lines[1:]

        cat_indices, mappings, format = serialize_format(id, titles, instances)
        loading.save_format(format,id)
        encode_instances(instances,cat_indices,mappings)

        features = []
        labels = []
        for instance in instances:
            features.append(instance[:-1])
            labels.append(instance[-1])
        return features, labels, titles

def get_text_indices(lines):
    indices = set()
    for line in lines:
        for i in range(0,len(line)):
            try:
                x = float(line[i])
            except ValueError:
                indices.add(i)
    return indices