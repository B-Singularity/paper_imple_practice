import numpy as np

def adj_encoding(matrix, ops):
    # encoding
    num_vertices = matrix.shape[0]
    ops_arr = np.array(list(ops.values()))
    upper_triangle = np.triu_indices(num_vertices, 1)
    upper_vals = matrix[upper_triangle]

    encoding_length = (num_vertices * (num_vertices - 1)) // 2 + len(ops)
    encoding = np.zeros(encoding_length)

    encoding[:len(upper_vals)] = upper_vals
    encoding[len(upper_vals):] = ops_arr

    return encoding


matrix = np.random.randn(4, 4)
upper_triangle = np.triu_indices(4, 1)
encoding = np.zeros(8)
ops = {'CONV_3X3':10, 'CONV_5X5':20, 'POOL_3X3':30}

# print(matrix)
# print(upper_triangle)
# print(matrix[upper_triangle])
