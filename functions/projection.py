from classes.Matrix import Matrix
from math import tan, pi

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

	proj = Matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
	tan_fov = tan(fov * 0.5 * (pi / 180))
	scale_x = 1 / (tan_fov * ratio)
	scale_y = 1 / tan_fov
	proj[0, 0] = scale_x
	proj[1, 1] = scale_y
	proj[2, 2] = -far / (far - near)
	proj[2, 3] = -1
	proj[3, 2] = -far * near / (far - near)

	return proj