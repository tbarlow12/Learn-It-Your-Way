import pdb
import json
from data_tools import loading



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

def is_categorical(lines):
    categorical = []
    all_distinct_vals = []
    for i in range(0,len(lines[0])):
        distinct_vals = set([line[i] for line in lines])
        all_distinct_vals.append(distinct_vals)
        if len(distinct_vals) <= categorical_limit:
            categorical.append(1)
        else:
            categorical.append(0)
    return categorical, all_distinct_vals

def generic_labels_features(id, csv):
    with open(csv) as f:
        lines = [line.strip().split(',') for line in f.readlines()]
        titles = lines[0]
        instances = lines[1:]

        categorical, distinct_vals = is_categorical(instances)
        text_indices = get_text_indices(lines)

        format = []
        for i in range(0,len(categorical)):
            data_type = 'num'
            if i in text_indices:
                data_type = 'str'
            values = []
            if categorical[i] == 1:
                values = distinct_vals[i]
            format.append({
                'name': titles[i],
                'datatype': data_type,
                'is_categorical': categorical[i],
                'vals': list(values)
            })
        loading.save_format(format,id)
        
        pdb.set_trace()

        features = []
        labels = []
        for instance in lines:
            items = instance
            features.append([items[:-1]])
            labels.append(items[-1])
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