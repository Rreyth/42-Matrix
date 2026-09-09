from Vector import *
from Matrix import *

from math import tan, pi

# Vector linear combination
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


# Linear interpolation
def lerp(obj1, obj2, scalar : int | float):
	if not isinstance(scalar, (int, float)):
		raise TypeError("last argument must be a scalar of type int or float")
	if not 0 <= scalar <= 1:
		raise ValueError("last argument must be a scalar between 0 and 1")

	if type(obj1) != type(obj2):
		raise TypeError("first two arguments must have the same type")

	return obj1 + ((obj2 - obj1) * scalar)


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

# Bonus: Projection matrix
def projection(fov : int|float, ratio : int|float, near : int|float, far : int|float):
	if not isinstance(fov, (int, float)) or not isinstance(ratio, (int, float))\
		or not isinstance(near, (int, float)) or not isinstance(far, (int, float)):
		raise TypeError("All arguments must be of type int or float")
	if not fov in range(0, 360):
		raise ValueError("FOV must be between 0 and 360 (not included)")
	if ratio <= 0:
		raise ValueError("Ratio must be greater than 0")
	if near < 0:
		raise ValueError("Near must be superior or equal to 0")
	if far < 0:
		raise ValueError("Far must be superior or equal to 0")
	if far <= near:
		raise ValueError("Far must be superior to near")

	# return Matrix(mat)
