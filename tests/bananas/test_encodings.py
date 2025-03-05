import unittest
import numpy as np
import bananas.nas_encodings as encoding

class MyTestCase(unittest.TestCase):
    def test_adj_encoding(self):
        matrix = np.array([
            [0, 1, 2],
            [1, 0, 3],
            [2, 3, 0]
        ])
        ops = {'CONV_3X3':10, 'POOL_3X3':30, 'CONV_5X5':5, 'POOL_5X5':5}
        expected_encoding = np.array([1, 2, 3, 10, 30, 5, 5])
        result = encoding.adj_encoding(matrix, ops)
        np.testing.assert_array_equal(result, expected_encoding)


if __name__ == '__main__':
    unittest.main()
