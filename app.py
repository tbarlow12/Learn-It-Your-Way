#!flask/bin/python
from flask import Flask
import pdb
from ml_models import sklearn, my_models
from data_tools import loading, csv_tools

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"

def get_features():
    return [[0,2,4,6,4],[1,4,2,3,5]]

@app.route('/predict/<id>')
def predict(id):
    #After user has created a model, this loads the model and returns the prediction
    model = loading.load_model(id)
    features = get_features() 
    return model.predict(features)

@app.route('/regression')
def regression():
    #load dataset (current temporary dataset)
    features, labels = csv_tools.get_labels_features_csv('datasets/test_data.csv')
    #train model
    model = sklearn.regression(features,labels)
    #generate guid and save model using guid
    id = loading.save_model(model)
    #return guid to user
    return id

@app.route('/clustering')
def clustering():
    #load dataset (current temporary dataset)
    features, labels = csv_tools.get_labels_features_csv('datasets/test_data.csv')
    #train model
    model = sklearn.cluster(features)
    #generate guid and save model using guid
    id = loading.save_model(model)
    #return guid to user
    return id

@app.route('/svm')
def svm():
    #load dataset (current temporary dataset)
    features, labels = csv_tools.get_labels_features_csv('datasets/test_data.csv')
    #train model
    model = sklearn.support_vector_machine(features,labels)
    #generate guid and save model using guid
    id = loading.save_model(model)
    #return guid to user
    return id

if __name__ == '__main__':
    app.run(debug=True)