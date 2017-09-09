import pdb

def get_labels_features_csv(csv):
    with open(csv) as f:
        lines = f.readlines()
        titles = lines[0]
        features = []
        labels = []
        for instance in lines[1:]:
            items = instance.split(',')
            features.append([float(x) for x in items[:-1]])
            labels.append(float(items[-1]))
        return features,labels