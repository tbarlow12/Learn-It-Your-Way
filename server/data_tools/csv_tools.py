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
        except Exception:
            data_types.append('str')
    return data_types

def get_text_indices(lines):
    indices = set()
    for line in lines:
        for i in range(0,len(line)):
            try:
                x = float(line[i])
            except Exception:
                indices.add(i)
    return indices

def encode_text_features(lines):
    #encode text stuff
    for index in text_indices:
        items = [x[index] for x in lines]


def generic_labels_features(csv):
    with open(csv) as f:
        lines = [line.strip().split(',') for line in f.readlines()]
        titles = lines[0]
        lines = lines[1:]
        data_types = get_data_types(lines[0])
        
        text_indices = get_text_indices(lines)

        pdb.set_trace()
        
        if len(text_indices) > 0:
            encode_text_features(lines)
            

        features = []
        labels = []



        for instance in lines:
            items = instance
            features.append([items[:-1]])
            labels.append(items[-1])
        return features, labels, titles


