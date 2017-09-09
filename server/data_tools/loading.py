import pandas
import pickle
import pdb
import json

model_dir = 'saved_models/'
format_dir = 'saved_formats/'
dataset_dir = 'datasets/'

def save_model(model,id,algorithm):
    pickle.dump(model, open(model_dir + id + '-' + algorithm + '.sav', 'wb'))
    return id

def load_model(id, algorithm):
    loaded_model = pickle.load(open(model_dir + id + '-' + algorithm + '.sav', 'rb'))
    return loaded_model

def save_format(format, id):
    with open(format_dir + id + '.json', 'w') as f:
        json.dump(format,f)

def load_format(id):
    with open(format_dir + id + '.json') as f:
        return json.load(f)

def save_dataset(file, id):
    path = dataset_dir + id + '.csv'
    file.save(path)
    return path
