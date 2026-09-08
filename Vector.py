class Vector:
	def __init__(self, elements : list[int | float]):
		for element in elements:
			if not isinstance(element, (int, float)):
				raise TypeError("Vector argument must be a list of [int or float]")
		self.elems = elements

	def size(self):
		return self.elems.__len__()

	def __str__(self):
		return str(self.elems)

	def toMatrix(self, rows : int, columns : int):
		from Matrix import Matrix

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
		if not isinstance(value, (int, float)):
			raise TypeError("Vector only contains int or float types")
		self.elems[key] = value

	def scale(self, scalar : int | float):
		if not isinstance(scalar, (int, float)):
			raise TypeError("Scalar must be of type int or float")
		for i in range(self.size()):
			self.elems[i] *= scalar

	def __mul__(self, scalar : int | float):
		if not isinstance(scalar, (int, float)):
			raise TypeError("Scalar must be of type int or float")
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
			res += elem if elem >= 0 else -elem

		return res

	def norm(self):
		res = 0
		for elem in self.elems:
			res += pow(elem, 2)
  
		return pow(res, 0.5)

	def norm_inf(self):
		res = [(elem if elem >= 0 else -elem) for elem in self.elems]
  
		return max(res)



# 	def __ne__(self, other):
# 		return int(self.x) != int(other.x) or int(self.y) != int(other.y)

# 	def __eq__(self, other):
# 		return self.x == other.x and self.y == other.y

# 	def div(self, nb):
# 		if nb == 0:
# 			return
# 		self.x /= nb
# 		self.y /= nb

# 	def move(self, speed, dist):
# 		self.x += (speed.x * dist)
# 		self.y += (speed.y * dist)

# def getDist(v1, v2):
# 	dx = pow(v2.x - v1.x, 2)
# 	dy = pow(v2.y - v1.y, 2)
# 	return sqrt(dx + dy)