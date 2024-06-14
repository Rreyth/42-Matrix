from classes.Complex import Complex
from functions.calculations import absolute

class Vector:
	def __init__(self, elements : list[int | float | Complex]):
		for element in elements:
			if not isinstance(element, (int, float, Complex)):
				raise TypeError("Vector argument must be a list of [int or float or Complex]")
		self.elems = elements

	def size(self):
		return self.elems.__len__()

	def __str__(self):
		return str(self.elems)

	def toMatrix(self, rows : int, columns : int):
		from classes.Matrix import Matrix

		if not isinstance(rows, int) or not isinstance(columns, int):
			raise TypeError("Width and height must be integers")
		if rows * columns != self.size():
			raise ValueError(f"Cannot make a {rows}x{columns} matrix, vector has {self.size()} values")
		mat = []
		pos = 0
		for i in range(rows):
			mat.append([])
			for j in range(columns):
				mat[i].append(self.elems[pos])
				pos += 1

		return Matrix(mat)

	def __add__(self, other):
		if not isinstance(other, Vector):
			raise TypeError("Cannot add a non vector to a vector")
		if self.size() != other.size():
			raise ValueError("Cannot add vectors with different size")
		res = []
		for i in range(self.size()):
			res.append(self.elems[i] + other.elems[i])
  
		return Vector(res)

	def __sub__(self, other):
		if not isinstance(other, Vector):
			raise TypeError("Cannot substract a non vector to a vector")
		if self.size() != other.size():
			raise ValueError("Cannot substract vectors with different size")
		res = []
		for i in range(self.size()):
			res.append(self.elems[i] - other.elems[i])
  
		return Vector(res)

	def __getitem__(self, key):
		return self.elems[key]

	def __setitem__(self, key, value):
		if not isinstance(value, (int, float, Complex)):
			raise TypeError("Vector only contains int, float or Complex types")
		self.elems[key] = value

	def scale(self, scalar : int | float | Complex):
		if not isinstance(scalar, (int, float, Complex)):
			raise TypeError("Scalar must be of type int, float or Complex")
		for i in range(self.size()):
			self.elems[i] *= scalar

	def __mul__(self, scalar : int | float | Complex):
		if not isinstance(scalar, (int, float, Complex)):
			raise TypeError("Scalar must be of type int, float or Complex")
		res = []
		for i in range(self.size()):
			res.append(self.elems[i] * scalar)
	
		return Vector(res)

	def dot(self, other):
		if not isinstance(other, Vector):
			raise TypeError("Cannot do a dot product with a non vector on a vector")
		if self.size() != other.size():
			raise ValueError("Vectors must be of same size")
 
		res = 0
		for i in range(self.size()):
			res += (self.elems[i] * other.elems[i])

		return res

	def norm_1(self):
		res = 0
		for elem in self.elems:
			res += absolute(elem)

		return res

	def norm(self):
		res = 0
		for elem in self.elems:
			res += elem ** 2

		return res ** 0.5

	def norm_inf(self):
		res = [absolute(elem) for elem in self.elems]
  
		return max(res)
