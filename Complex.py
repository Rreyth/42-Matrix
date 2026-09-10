from calculations import absolute

class Complex:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __str__(self):
		return f"{self.a} + {self.b}i"

	def __repr__(self):
		return f"{self.a} + {self.b}i"

	def __add__(self, other):
		if not isinstance(other, (Complex, int, float)):
			raise TypeError("Must be of type Complex, int or float to add to a Complex")
		if type(other) == Complex:
			a = self.a + other.a
			b = self.b + other.b
		else:
			a = self.a + other
			b = self.b

		return Complex(a, b)

	def __radd__(self, other):
		return self.__add__(other)

	def __sub__(self, other):
		if not isinstance(other, (Complex, int, float)):
			raise TypeError("Must be of type Complex, int or float to substract to a Complex")
		if type(other) == Complex:
			a = self.a - other.a
			b = self.b - other.b
		else:
			a = self.a - other
			b = self.b

		return Complex(a, b)

	def __rsub__(self, other):
		if not isinstance(other, (int, float)):
			raise TypeError("Must be of type Complex, int or float to substract to a Complex")
		a = other - self.a
		b = -self.b

		return Complex(a, b)

	def __mul__(self, other):
		if not isinstance(other, (Complex, int, float)):
			raise TypeError("Must be of type Complex, int or float to multiply a Complex")

		if type(other) == Complex:
			a = (self.a * other.a) - (self.b * other.b)
			b = (self.a * other.b) + (self.b * other.a)
		else:
			a = self.a * other
			b = self.b * other

		return Complex(a, b)

	def __rmul__(self, other):
		return self.__mul__(other)

	def __truediv__(self, other):
		if not isinstance(other, (Complex, int, float)):
			raise TypeError("Must be of type Complex, int or float to divide a Complex")

		if type(other) == Complex:
			a = ((self.a * other.a) + (self.b * other.b)) / (other.a ** 2 + other.b ** 2)
			b = ((self.b * other.a) - (self.a * other.b)) / (other.a ** 2 + other.b ** 2)
		else:
			a = self.a / other
			b = self.b / other

		return Complex(a, b)

	def __rtruediv__(self, other):
		if not isinstance(other, (int, float)):
			raise TypeError("Must be of type Complex, int or float to divide a Complex")
		a = (other * self.a) / (self.a ** 2 + self.b ** 2)
		b = -((other * self.b) / (self.a ** 2 + self.b ** 2))

		return Complex(a, b)

	def __pow__(self, exp):
		if exp == 0.5:
			res = self.squareRoot()
		else:
			res = self
			for i in range(exp - 1):
				res *= self
		return res

	def __gt__(self, other):
		return self.absolute() > absolute(other)

	def __ne__(self, value):
		return self.absolute() != value

	def absolute(self):
		res = self.a ** 2 + self.b ** 2
		res = res ** 0.5
		return res

	def squareRoot(self):
		absolute = self.absolute()
		a = ((absolute + self.a) / 2) ** 0.5
		b = ((absolute - self.a) / 2) ** 0.5
  
		return Complex(a, b)
