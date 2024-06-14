from Vector import Vector
from Complex import Complex

# Vector linear combination
def linear_combination(vectors : list[Vector], scalars : list[int | float | Complex]):
	for v in vectors:
		if not isinstance(v, Vector):
			raise TypeError("First argument must be a list of Vectors")
	for s in scalars:
		if not isinstance(s, (int, float, Complex)):
			raise TypeError("Second argument must be a list of scalars of type int or float")
	if vectors.__len__() != scalars.__len__():
		raise ValueError("Vectors list and scalars list must have the same size")
	
	for i in range(vectors.__len__()):
		vectors[i].scale(scalars[i])
	
	res = vectors[0]
	for i in range(vectors.__len__() - 1):
		res = res + vectors[i + 1]

	return res


# Vector cosine
def angle_cos(u : Vector, v : Vector):
	if not isinstance(u, Vector) or not isinstance(v, Vector):
		raise TypeError("Both arguments must be of type Vector")
	if u.size() != v.size():
		raise ValueError("Both vectors must have the same size")

	return u.dot(v) / (u.norm() * v.norm())


# 3D Vector cross product
def cross_product(u : Vector, v : Vector) -> Vector:
	if not isinstance(u, Vector) or not isinstance(v, Vector):
		raise TypeError("Both arguments must be of type Vector")
	if u.size() != 3 or v.size() != 3:
		raise ValueError("Both vectors must be of size 3")

	res = [u[1] * v[2] - u[2] * v[1],
        	u[2] * v[0] - u[0] * v[2],
         	u[0] * v[1] - u[1] * v[0]]

	return Vector(res)
