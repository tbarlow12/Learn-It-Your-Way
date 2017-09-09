from ml_models import sklearn, my_models
from data_tools import csv_tools, loading
import pdb

features, labels = csv_tools.get_labels_features_csv('datasets/test_data.csv')
cluster_model = sklearn.cluster(features,2)
regression_model = sklearn.regression(features,labels)

print(loading.save_model(cluster_model))
print(loading.save_model(regression_model))