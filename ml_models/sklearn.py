from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans


def regression(features,labels):
    model = LinearRegression()
    model.fit(features,labels)
    return model

def cluster(instances,k):
    model = KMeans(n_clusters=k)
    model.fit(instances)
    return model

    