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

# linear_combination::<K>(u: &[Vector<K>], coefs: &[K]) -> Vector<K>;
def linear_combination(vectors : list[Vector], scalars : list[int | float]):
	for v in vectors:
		if not isinstance(v, Vector):
			raise TypeError("First argument must be a list of Vectors")
	for s in scalars:
		if not isinstance(s, (int, float)):
			raise TypeError("Second argument must be a list of scalars of type int or float")
	if vectors.__len__() != scalars.__len__():
		raise ValueError("Vectors list and scalars list must have the same size")
	
	for i in range(vectors.__len__()):
		vectors[i].scale(scalars[i])
	
	res = vectors[0]
	for i in range(vectors.__len__() - 1):
		res = res + vectors[i + 1]

	return res
			
			


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
  
# 	def normalize(self):
# 		len = sqrt((self.x * self.x) + (self.y * self.y))
# 		self.div(len)

# def dotProduct(v1, v2):
# 	return ((v1.x * v2.x) + (v1.y * v2.y))

# def crossProduct(v1, v2):
# 	return ((v1.x * v2.y) - (v1.y * v2.x))

# def getDist(v1, v2):
# 	dx = pow(v2.x - v1.x, 2)
# 	dy = pow(v2.y - v1.y, 2)
# 	return sqrt(dx + dy)