"""
This file contains auxiliary functions used within '761720_project1'
"""
import numpy as np

# function to reformat label data where index of 1 in otherwise zero array indicates label
def reformat_labels(A):
    A_new = np.zeros([A.shape[0], max(A)+1])
    for i in range(A.shape[0]):
        val = A[i]
        A_new[i, val] = 1
    return A_new