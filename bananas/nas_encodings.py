import numpy as np

def adj_encoding(matrix, ops, ops_dic):
    # encoding
    num_vertices = matrix.shape[0]
    ops_arr = np.vectorize(lambda op: ops_dic[op])(ops)
    upper_triangle = np.triu_indices(num_vertices, 1)
    upper_vals = matrix[upper_triangle]

    encoding_length = (num_vertices * (num_vertices - 1)) // 2 + (num_vertices - 2)
    encoding = np.zeros(encoding_length)

    encoding[:len(upper_vals)] = upper_vals
    encoding[len(upper_vals):] = ops_arr

    return encoding

def cat_adj_encoding(matrix, ops):
    num_vertices = matrix.shape[0]
    encoding_length = (num_vertices * (num_vertices - 1)) // 2 + (num_vertices - 2)

