#!flask/bin/python
from flask import Flask, request, redirect, url_for
import pdb
from ml_models import sklearn, my_models
from data_tools import loading, data_cleaning
import uuid
import json

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"

def get_dataset(request):
    id = str(uuid.uuid4())
    if request.method == 'POST' and len(request.files) > 0:
        file = request.files['file']
        path = loading.save_dataset(file, id)
        features, labels, titles = data_cleaning.generic_labels_features(id, path)
        return id, features, labels, titles
        
@app.route('/predict/single/<id>/<algorithm>',methods=['GET','POST'])
def predict_single(id,algorithm):
    #After user has created a model, this loads the model and returns the prediction
    model = loading.load_model(id,algorithm)
    format = loading.load_format(id)
    features = data_cleaning.get_features(format,request.form) 
    return model.predict(features)[0]

@app.route('/predict/multi/<id>/<algorithm>',methods=['GET','POST'])
def predict_multi(id,algorithm):
    content = request.get_json()
    model = loading.load_model(id,algorithm)
    format = loading.load_format(id)    
    for instance in content:
        features = data_cleaning.get_features(format,instance)
        instance['Label'] = model.predict(features)[0]
    return str(content)        

@app.route('/regression',methods=['GET','POST'])
def regression():
    #load dataset (current temporary dataset)
    id, features, labels, titles = get_dataset(request)
    #train model
    model = sklearn.regression(features,labels)
    #generate guid and save model using guid
    id = loading.save_model(model, id,'regression')
    #return guid to user
    return id

@app.route('/clustering')
def clustering():
    #load dataset (current temporary dataset)
    id, features, labels, titles = get_dataset(request)
    #train model
    model = sklearn.cluster(features)
    #generate guid and save model using guid
    id = loading.save_model(model,'clustering')
    #return guid to user
    return id

@app.route('/svm')
def svm():
    #load dataset (current temporary dataset)
    id, features, labels, titles = get_dataset(request)
    #train model
    model = sklearn.support_vector_machine(features,labels)
    #generate guid and save model using guid
    id = loading.save_model(model,'svm')
    #return guid to user
    return id

if __name__ == '__main__':
    app.run(debug=True)