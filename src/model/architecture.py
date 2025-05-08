from sklearn.neighbors import NearestNeighbors

def build_model(n_neighbors, algorithm='auto', metric='cosine'):
    model = NearestNeighbors(n_neighbors=n_neighbors, algorithm=algorithm, metric=metric)
    return model
