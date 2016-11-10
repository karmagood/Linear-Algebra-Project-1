import unittest
from inverse_via_lu import Matrix

class TestMatrixInverse(unittest.TestCase):

    def test_LU_2x2_matrix(self):
        matrix = Matrix([[3, 4], [5, 6]])
        matrix.LU()
        self.assertEqual(matrix.L.tolist(), [[1.0, 0.0], [0.6, 1.0]])
        self.assertEqual(matrix.U.tolist(), [[5.0, 6], [0.0, 0.4]])

    def test_LU_3x3_matrix(self):
        matrix = Matrix([[1, 2, 4], [2, 1, 2], [1, 2, 1]])
        matrix.LU()
        self.assertEqual(matrix.L.tolist(), [[1, 0, 0], [0.5, 1, 0], [0.5, 1, 1]])
        self.assertEqual(matrix.U.tolist(), [[2, 1, 2], [0, 1.5, 0], [0, 0, 3]])

    def test_inverse_2x2_matrix(self):
        matrix = Matrix([[3, 4], [5, 6]])
        expected = [[-3, 2], [2.5, -1.5]]
        self.assertEqual(matrix.matrix_inverse().tolist(), expected)

    def test_inverse_3x3_matrix(self):
        matrix = Matrix([[1, 0, 0], [0.5, 1, 0], [0.5, 1, 1]])
        expected = [[1, 0, 0], [-0.5, 1, 0], [0, -1, 1]]
        self.assertEqual(matrix.matrix_inverse().tolist(), expected)

    def test_not_square_matrix(self):
        matrix = Matrix([[1, 2], [2, 3], [1, 2, 3]])
        self.assertEqual(matrix.check_matrix(), "Matrix is not square matrix, it doesn't have an inverse")

    def test_not_square_matrix_2(self):
        matrix = Matrix([[1, 3], [1, 2, 3]])
        self.assertEqual(matrix.check_matrix(), "Matrix is not square matrix, it doesn't have an inverse")

    def test_det_matrix(self):
        matrix = Matrix([[1, 2, 3], [4, 5, 6], [5, 7, 9]])
        self.assertEqual(matrix.det(), "The determinant of a matrix is equal to zero, then the matrix does not have an inverse")

    def test_wrong_matrix(self):
        matrix  = Matrix([[1,2,3],[2, 3, 4], ["a", "b", "c"]])
        self.assertEqual(matrix.check_matrix(),"Wrong matrix")

    def final_check_2x2_matrix(self):
        matrix = Matrix([[1, 2], [2, 1]])
        expected = [[1, 0], [0, 1]]
        self.assertEqual(matrix.final_check().tolist(), expected)

    def final_check_3x3_matrix(self):
        matrix = Matrix([[1, 0, 0], [0.5, 1, 0], [0.5, 1, 1]])
        expected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.assertEqual(matrix.final_check().tolist(), expected)

if __name__ == '__main__':
    unittest.main()
