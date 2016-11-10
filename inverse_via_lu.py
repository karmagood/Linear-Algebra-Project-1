import numpy as np
import copy

class Matrix(object):
	"""Simple matrix calls for inverses"""
	def __init__(self, matrix):
		self.matrix = np.matrix(matrix)
		self.L = None
		self.U = None
		self.matrix_inversed = None

	def LU(self):
		"""For LU-decomposition we will use Doolittle's Algorithm"""
		m = self.matrix.shape[0]
		self.L = np.zeros((m,m))
		self.U = np.zeros((m,m))
		self.P = self._P()
		PA = self.P * self.matrix
		for j in range(m):
			self.L[j,j] = 1.0
			for i in range(j+1):
				s1 = sum(self.U[k,j] * self.L[i,k] for k in range(i))
				self.U[i,j] = PA[i,j] - s1

			for i in range(j, m):
				s2 = sum(self.U[k,j] * self.L[i,k] for k in range(j))
				self.L[i,j] = (PA[i,j] - s2) / self.U[j,j]
		self.L = np.around(self.L,1)
		self.U = np.around(self.U,1)

	def _P(self):
		"""Computing rearengments of rows for Doolittle's Algorithm"""
		m = self.matrix.shape[0]
		ident = np.identity(m)
		for i in range(m-1, -1, -1):
			row = max(range(0,i+1), key=lambda k: abs(self.matrix.item(k,i)))
			if i != row:
				temp = copy.copy(ident[i,:])
				ident[i,:] =  ident[row,:]
				ident[row, :] = temp
		return ident

	def gj_inverse(self, matrix):
		arr = matrix.tolist()
		#Add identity matrix on the right
		for i in range(matrix.shape[0]):
			for j in range(matrix.shape[1]):
				if j == i:
					arr[i].append(1)
				else:
					arr[i].append(0)
		#Reset all that is below the main diagonal

		for i in range(matrix.shape[0]):
			arr[i] = [round(x * (1/arr[i][i]), 4) for x in arr[i]]
			for j in range(matrix.shape[1]):
				try:
					j += i
					arr1 = [round(x * (-arr[j+1][i]),4) for x in arr[i]]
					arr[j+1] = list(map(lambda x,y: round(x+y, 4), arr[j+1], arr1 ))
				except IndexError:
					break
		#Reset all that is above the main diagonal
		for i in range(matrix.shape[0]-1, -1,  -1):
			arr[i] = [round(x * (1/arr[i][i]), 4) for x in arr[i]]
			for j in range(matrix.shape[1]-1, 0, -1):
				if j <= i:
					arr1 = [round(x * (-arr[j-1][i]),4) for x in arr[i]]
					arr[j-1] = list(map(lambda x, y: round(x+y, 4), arr[j-1], arr1))
		arr2 = [arr[l][matrix.shape[0]:] for l in range(matrix.shape[1])]
		return arr2

	def transpose(self, matrix):
		tran = [[j[i] for j in matrix] for i in range(len(matrix[0]))]
		return tran

	def check_matrix(self):
		if not self.matrix.shape[0] == self.matrix.shape[1]:
			raise Exception("Matrix is not square matrix, it doesn't have an inverse")
		d = self.det()
		if d:
			raise Exception(d)
	def det(self):
		determ = round(np.linalg.det(self.matrix),1)
		
		if not determ:
		 	return "The determinant of a matrix is equal to zero, then the matrix does not have an inverse"
	
	def final_check(self):
		matrix_A = self.matrix
		inverse = matrix.matrix_inverse()
		dot = np.dot(matrix_A, inverse)
		return dot.round(0)

	def matrix_inverse(self):
		self.LU()
		self.check_matrix()
		inversed_matrix = np.matrix(self.gj_inverse(self.U))*np.matrix(self.gj_inverse(self.L))*np.matrix(self.transpose(self.P))
		return inversed_matrix.round(1)

