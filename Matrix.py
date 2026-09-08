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

	def scale(self, scalar):
		if not isinstance(scalar, (int, float)):
			raise TypeError("Scalar must be of type int or float")
		for i in range(self.size()[0]):
			for j in range(self.size()[1]):
				self.elems[i][j] *= scalar