class Matrix:
	def __init__(self, elements : list[list[int | float]]):
		size = elements[0].__len__()
		for line in elements:
			if line.__len__() != size:
				raise ValueError("Matrix must be a rectangle or a square")
			for elem in line:
				if not isinstance(elem, (int, float)):
					raise TypeError("Matrix argument must be a list of lists of [int or float]")
		self.elems = elements
  
	def size(self):
		size = [self.elems.__len__(), self.elems[0].__len__()]
		return size

	def __str__(self):
		ret = ""
		for i, line in enumerate(self.elems):
			ret += str(line)
			if i != self.elems.__len__() - 1:
				ret += "\n"
		return ret

	def __add__(self, other):
		if not isinstance(other, Matrix):
			raise TypeError("Cannot add a non Matrix to a Matrix")
		if self.size() != other.size():
			raise ValueError("Cannot add Matrix with different shape / sizes")

		res = []
		for i in range(self.size()[0]):
			res.append([])
			for j in range(self.size()[1]):
				res[i].append(self.elems[i][j] + other.elems[i][j])
    
		return Matrix(res)

	def __sub__(self, other):
		if not isinstance(other, Matrix):
			raise TypeError("Cannot substract a non Matrix to a Matrix")
		if self.size() != other.size():
			raise ValueError("Cannot substract Matrix with different shape / sizes")

		res = []
		for i in range(self.size()[0]):
			res.append([])
			for j in range(self.size()[1]):
				res[i].append(self.elems[i][j] - other.elems[i][j])
    
		return Matrix(res)

	def __getitem__(self, keys):
		r, c = keys
		return self.elems[r][c]

	def __setitem__(self, keys, value):
		if not isinstance(value, (int, float)):
			raise TypeError("Matrix only contains int or float types")
		r, c = keys
		self.elems[r][c] = value

	def isSquare(self):
		if self.elems.__len__() == self.elems[0].__len__():
			return True
		return False

	def toVector(self):
		from Vector import Vector

		vec = []
		for line in self.elems:
			for value in line:
				vec.append(value)
    
		return Vector(vec)

	def scale(self, scalar : int | float):
		if not isinstance(scalar, (int, float)):
			raise TypeError("Scalar must be of type int or float")
		for i in range(self.size()[0]):
			for j in range(self.size()[1]):
				self.elems[i][j] *= scalar
    
	def __mul__(self, scalar : int | float):
		if not isinstance(scalar, (int, float)):
			raise TypeError("Scalar must be of type int or float")

		res = []
		for i in range(self.size()[0]):
			res.append([])
			for j in range(self.size()[1]):
				res[i].append(self.elems[i][j] * scalar)
    
		return Matrix(res)

	def mul_vec(self, vec):
		from Vector import Vector

		if not isinstance(vec, Vector):
			raise TypeError("Argument must be of type Vector")
		if vec.size() != self.size()[1]:
			raise ValueError("Vector must have a size equal to Matrix number of columns")

		res = []
		for i in range(self.size()[0]):
			res.append(0)
			for j in range(self.size()[1]):
				res[i] += self.elems[i][j] * vec[j]

		return Vector(res)

	def mul_mat(self, mat):
		if not isinstance(mat, Matrix):      
			raise TypeError("Argument must be of type Matrix")
		if self.size()[1] != mat.size()[0]:
			raise ValueError("Second Matrix must have a number of line equal to first Matrix number of columns")

		res = []
		for i in range(self.size()[0]):
			res.append([])
			for j in range(mat.size()[1]):
				res[i].append(0)
				for k in range(mat.size()[0]):
					res[i][j] += self[i, k] * mat[k, j]

		return Matrix(res)

	def trace(self):
		if not self.isSquare():
			raise ValueError("Matrix must be square to compute the trace")

		res = 0
		for i in range(self.size()[0]):
			res += self[i, i]

		return res

	def transpose(self):
		res = []
		for i in range(self.size()[1]):
			res.append([])
			for j in range(self.size()[0]):
				res[i].append(self[j, i])
    
		return Matrix(res)

	def row_echelon(self):
		from Vector import Vector
		res = Matrix(self.elems)

		i, j = 0, 0
		while i < res.size()[0] and j < res.size()[1]:
			if res[i, j] == 0:
				k = i + 1
				while k < res.size()[0]:
					if res[k, j] != 0: #Row-switching
						swp = res.elems[i]
						res.elems[i] = res.elems[k]
						res.elems[k] = swp
						break
					k += 1
      
				if res[i, j] == 0:
					j += 1
					continue

			if res[i, j] != 0:
				res.elems[i] = (Vector(res.elems[i]) * (1/res[i, j])).elems #Row-multiplying
				k = 0
				while k < res.size()[0]:
					if res[k, j] != 0 and k != i:
						res.elems[k] = (Vector(res.elems[k]) + (Vector(res.elems[i]) * -res[k, j])).elems #Row-addition
					k += 1
				i += 1

			j += 1
		return res
