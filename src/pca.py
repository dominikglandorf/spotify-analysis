import numpy as np

def PCA(data):
    cov = 1 / data.shape[0] * data.T @ data
    values, vectors = np.linalg.eig(cov)

    vectors = vectors[:,np.flip(np.argsort(values))]
    values = np.flip(np.sort(values))
    return values, vectors