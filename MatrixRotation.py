import numpy as np

def rotate_matrix(array):
    array = np.array(array)
    transpose = np.ndarray.transpose(array)
    rotated = np.fliplr(transpose)
    return rotated