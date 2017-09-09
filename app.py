#!flask/bin/python
from flask import Flask
import pdb
from ml_models import sklearn, my_models
from data_tools import loading, csv_tools

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"

@app.route('/regression')
def regression():
    #load dataset
    #train model
    #generate guid
    #save model using guid
    #return guid to user
    #when user makes another call to endpoint, load model
    return "Regression"

if __name__ == '__main__':
    app.run(debug=True)