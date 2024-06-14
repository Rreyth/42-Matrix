# Linear interpolation
def lerp(obj1, obj2, scalar : int | float):
	if not isinstance(scalar, (int, float)):
		raise TypeError("last argument must be a scalar of type int or float")
	if not 0 <= scalar <= 1:
		raise ValueError("last argument must be a scalar between 0 and 1")

	if type(obj1) != type(obj2):
		raise TypeError("first two arguments must have the same type")

	return obj1 + ((obj2 - obj1) * scalar)


# Utils
def absolute(value):
	from Complex import Complex

	if type(value) == Complex:
		res = value.absolute()
	else:
		res = value if value >= 0 else -value
	return res
