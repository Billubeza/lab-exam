import numpy as np

def reconstruct_matrix(U, S, V):
    if len(S.shape) == 1:  
        S = np.diag(S)
    reconstructed_matrix = np.dot(U, np.dot(S, V))
    
    return reconstructed_matrix
