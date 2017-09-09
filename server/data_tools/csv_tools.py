import pdb

class format:
    def __init__(self,_name,_data_type,_values):
        this.name = _name
        this.data_type = _data_type
        this.values = _values

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

def categorical_or_continuous(lines):
    result = []
    for i in range(0,len(lines[0])):
        distinct_vals = set([line[i] for line in lines])
        if len(distinct_vals) <= categorical_limit:
            result.append(0)
        else:
            result.append(1)
    return result

def generic_labels_features(csv):
    with open(csv) as f:
        lines = [line.strip().split(',') for line in f.readlines()]
        titles = lines[0]
        lines = lines[1:]

        category_or_continuous = categorical_or_continuous(lines)
        
        data_types = get_data_types(lines[0])
        
        text_indices = get_text_indices(data_types)

        pdb.set_trace()

        features = []
        labels = []
        for instance in lines:
            items = instance
            features.append([items[:-1]])
            labels.append(items[-1])
        return features, labels, titles

def get_text_indices(data_types):
    indices = []
    for i in range(0,len(data_types)):
        if data_types[i] == 'str':
            indices.append(i)
    return indices