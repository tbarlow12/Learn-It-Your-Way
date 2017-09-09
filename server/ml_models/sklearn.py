from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
from sklearn import svm
import pdb


def regression(features,labels):
    model = LinearRegression()
    pdb.set_trace()
    model.fit(features,labels)
    return model

def cluster(instances,k):
    model = KMeans(n_clusters=k)
    model.fit(instances)
    return model

def support_vector_machine(features,labels):
    model = svm.SVC()
    model.fit(features,labels)
    return model