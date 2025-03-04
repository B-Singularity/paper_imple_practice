import numpy as np

def adj_edcoding(matrix, ops):
    # encoding
    num_vertices = len(matrix)
    encoding_length = (num_vertices * (num_vertices - 1)) // 2 + len(ops)
    encoding = np.zeros(encoding_length)
    upper_triangle = np.triu_indices(num_vertices, 1)
    encoding[:len(upper_triangle)] = matrix[upper_triangle]
    ops_arr = np.array(list(ops.values()))
    encoding[len(upper_triangle):] = ops_arr[upper_triangle]
    return encoding


matrix = np.random.randn(4, 4)
upper_triangle = np.triu_indices(4, 1)
encoding = np.zeros(8)

print(matrix)
print(matrix[upper_triangle])