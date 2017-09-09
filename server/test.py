from ml_models import sklearn, my_models
from data_tools import csv_tools, loading
import mail_gun
import pdb

features, labels, titles = csv_tools.numeric_labels_features('datasets/test_data.csv')
cluster_model = sklearn.cluster(features,2)
regression_model = sklearn.regression(features,labels)

cluster_id = loading.save_model(cluster_model)
regression_id = loading.save_model(regression_model)

loading.save_format(titles,cluster_id)
loading.save_format(titles,regression_id)

mail_gun.send_simple_message("p.egan.anderson@gmail.com","openml.com")