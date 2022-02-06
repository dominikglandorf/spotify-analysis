import numpy as np

# this function standardizes data and return eigenvalues and eigenvectors from a PCA
def PCA(data):
    data = (data-data.mean(axis=0)) / data.std(axis=0)
    cov = 1 / data.shape[0] * data.T @ data
    values, vectors = np.linalg.eig(cov)

    vectors = vectors[:,np.flip(np.argsort(values))]
    values = np.flip(np.sort(values))
    return values, vectors