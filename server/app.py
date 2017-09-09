#!flask/bin/python
from flask import Flask, request, redirect, url_for
import pdb
from ml_models import sklearn, my_models
from data_tools import loading, csv_tools
import uuid

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"

def get_features():
    return [[0,2,4,6,4],[1,4,2,3,5]]

def get_dataset(request):
    id = str(uuid.uuid4())
    if request.method == 'POST' and len(request.files) > 0:
        file = request.files['file']
        path = loading.save_dataset(file, id)
        #features, labels, titles = csv_tools.numeric_labels_features(path)
        features, labels, titles = csv_tools.generic_labels_features(path)
        return id, features, labels, titles
        
@app.route('/predict/<id>')
def predict(id):
    #After user has created a model, this loads the model and returns the prediction
    model = loading.load_model(id)
    features = get_features() 
    return model.predict(features)

@app.route('/regression',methods=['GET','POST'])
def regression():
    #load dataset (current temporary dataset)
    id, features, labels, titles = get_dataset(request)
    #train model
    model = sklearn.regression(features,labels)
    #generate guid and save model using guid
    id = loading.save_model(model)
    #return guid to user
    return id

@app.route('/clustering')
def clustering():
    #load dataset (current temporary dataset)
    id, features, labels, titles = get_dataset(request)
    #train model
    model = sklearn.cluster(features)
    #generate guid and save model using guid
    id = loading.save_model(model)
    #return guid to user
    return id

@app.route('/svm')
def svm():
    #load dataset (current temporary dataset)
    id, features, labels, titles = get_dataset(request)
    #train model
    model = sklearn.support_vector_machine(features,labels)
    #generate guid and save model using guid
    id = loading.save_model(model)
    #return guid to user
    return id

if __name__ == '__main__':
    app.run(debug=True)