import pandas
import pickle
import uuid

model_dir = 'saved_models/'

def save_model(model):
    id = str(uuid.uuid4())
    pickle.dump(model, open(model_dir + id + '.sav', 'wb'))
    return id

def load_model(id):
    loaded_model = pickle.load(open(model_dir + id + '.sav', 'rb'))
    return loaded_model