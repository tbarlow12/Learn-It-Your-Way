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

def all_except(folds,test_fold_index):
    result = []
    for i in range(0,len(folds)):
        if i != test_fold_index:
            result.extend(folds[i])
    return result

def k_fold(data,k):
    avg = len(data) / float(k)
    result = []
    last = 0.0
    while last < len(data):
        result.append(data[int(last):int(last + avg)])
        last += avg
    return result

def evaluate_model(model,test_features,test_labels):
    predictions = model.predict(test_features)
    total = 0.0
    count = 0.0
    for i in range(0,len(predictions)):
        if predictions[i] == test_data[i][1]:
            total += 1
        count += 1
    return total / count

def get_features_labels(data):
    features = [item[:-1] for item in data]
    labels = [item[-1] for item in data]
    return features,labels

def cross_validate(m,features,labels,k):
    data = []
    for i in range(0,len(features)):
        data.append(features[i])
        data[i].append(labels[i])
    folds = k_fold(data,k)
    total_score = 0.0
    for i in range(0,len(folds)):
        test_data = folds[i]
        training_data = all_except(folds,i)
        training_features, training_labels = get_features_labels(training_data)
        test_features, test_labels = get_features_labels(test_data)
        if m == 'regression':
            model = sklearn.regression(training_features,training_labels)
        elif m == 'svm':
            model = sklearn.svm(training_features,training_labels)
        s = evaluate_model(model,test_features,test_labels)
        total_score += s
    return total_score / float(k)
        
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
        #TODO Convert label to string value before returning it
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

@app.route('/clustering',methods=['GET','POST'])
def clustering():
    #load dataset (current temporary dataset)
    id, features, labels, titles = get_dataset(request)
    #train model
    model = sklearn.cluster(features)
    #generate guid and save model using guid
    id = loading.save_model(model,id, 'clustering')
    #return guid to user
    return id

@app.route('/svm',methods=['GET','POST'])
def svm():
    #load dataset (current temporary dataset)
    id, features, labels, titles = get_dataset(request)
    #train model
    model = sklearn.support_vector_machine(features,labels)
    #generate guid and save model using guid
    id = loading.save_model(model,id, 'svm')
    #return guid to user
    return id

@app.route('/cross/<algorithm>',methods=['GET','POST'])
def perform_cross_validate(algorithm):
    #load dataset (current temporary dataset)
    id, features, labels, titles = get_dataset(request)
    
    score = cross_validate(algorithm,features,labels,10)



if __name__ == '__main__':
    app.run(debug=True)