def find_matrix_shape(matrix):
    if not matrix:  
        return (0, 0)
    if not isinstance(matrix[0], list):  
        return (1, len(matrix))
    return (len(matrix), len(matrix[0]))
