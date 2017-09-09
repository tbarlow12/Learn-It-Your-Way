import ml_models
import data_tools
from data_tools import csv_tools
import pdb

features, labels = csv_tools.get_labels_features_csv('datasets/test_data.csv')
cluster_model = ml_models.cluster(features,2)
regression_model = ml_models.regression(features,labels)

pdb.set_trace()