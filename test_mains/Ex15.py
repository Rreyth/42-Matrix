import sys
sys.path.append('../')

from classes.Vector import Vector
from classes.Matrix import Matrix
from classes.Complex import Complex
from functions.calculations import lerp
from functions.vector_calc import linear_combination, angle_cos, cross_product

# EX15: Bonus: Complex
print("-------Complex-------")
print("-------Complex class-------")

nb1 = Complex(3, 4)
nb2 = Complex(1, 2)

print(f"nb1({nb1}) + nb2({nb2}) = {nb1 + nb2}")
print(f"nb1({nb1}) + 5 = {nb1 + 5}")
print(f"nb2({nb2}) + nb1({nb1}) = {nb2 + nb1}")
print(f"5 + nb1({nb1}) = {5 + nb1}")
print(f"nb1({nb1}) - nb2({nb2}) = {nb1 - nb2}")
print(f"nb1({nb1}) - 5 = {nb1 - 5}")
print(f"nb2({nb2}) - nb1({nb1}) = {nb2 - nb1}")
print(f"5 - nb1({nb1}) = {5 - nb1}")
print(f"nb1({nb1}) * nb2({nb2}) = {nb1 * nb2}")
print(f"nb1({nb1}) * 5 = {nb1 * 5}")
print(f"nb2({nb2}) * nb1({nb1}) = {nb2 * nb1}")
print(f"5 * nb1({nb1}) = {5 * nb1}")
print(f"nb1({nb1}) / nb2({nb2}) = {nb1 / nb2}")
print(f"nb1({nb1}) / 5 = {nb1 / 5}")
print(f"nb2({nb2}) / nb1({nb1}) = {nb2 / nb1}")
print(f"4 / nb2({nb2}) = {4 / nb2}")
print(f"nb1({nb1}).absolute() = {nb1.absolute()}")
print(f"nb1({nb1}).squareRoot() = {nb1.squareRoot()}")
print(f"nb1({nb1}) pow 2 = {nb1 ** 2}")

print("\n-------Complex Vector-------")
v = Vector([1, 2, 3, Complex(4, 5), 5, 6, 7, 8, 9])

print("\nprint vec")
print(v)
print("vec size = ")
print(v.size())
print("\nvec to matrix")
print(v.toMatrix(3, 3))

print("\n-------Complex Vector Ex00-------")

v2 = Vector([1, 2, 3, Complex(4, 5), 5, 6, 7, 8, 9])

print(f"\nvector v: {v}\n+ vector v2: {v2}")
v3 = v + v2
print(v3)
print(f"\nvector v3: {v3}\n- vector v2: {v2}")
print(v3 - v2)
print(f"\nscaling vector v3: {v3} by 2")
v3.scale(2)
print(v3)
print(f"\nsetitem 5 of vector v3: {v3} to 999")
v3[5] = 999
print(f"\ngetitem 5 of vector v3: {v3}")
print(v3[5])

print("\n-------Complex Matrix-------")

m = Matrix([[Complex(1, 1), 1, 1],
        [2, Complex(2, 2), 2],
        [3, 3, Complex(3, 3)],
        [4, 4, 4]])

print("\nprint matrix")
print(m)
print("matrix size = ")
print(m.size())
print("\nmatrix is square?")
print(m.isSquare())
print("\nmatrix to vector")
print(m.toVector())

print("\n-------Complex Matrix Ex00-------")
m2 = Matrix([[Complex(1, 1), 1, 1],
        [2, Complex(2, 2), 2],
        [3, 3, Complex(3, 3)],
        [4, 4, 4]])

print(f"\nMatrix m:\n{m}\n+ Matrix m2:\n{m2}\n=")
m3 = m + m2
print(m3)
print(f"\nMatrix m3:\n{m3}\n- Matrix m2:\n{m2}\n=")
print(m3 - m2)
print(f"\nScaling Matrix m3:\n{m3}\nby 5\n=")
m3.scale(5)
print(m3)
print(f"\nSetitem Matrix [1, 2] of m3:\n{m3}\nto 999")
m3[1, 2] = 999
print(f"\nGetitem Matrix [1, 2] of m3:\n{m3}")
print(m3[1, 2])

print("\n-------Complex Ex01: Vector linear combination-------")

v = Vector([1, Complex(1, 3), 3])
w = Vector([Complex(9, 7), 10, -100])

scalars = [10, -2]

print(f"\nvectors :\nv = {v}\nw = {w}\nscalars = {scalars}")
print("res = ", linear_combination([v, w], scalars))

print("\n-------Complex Ex02: linear interpolation-------")

obj1 = Complex(2, 1)
obj2 = Complex(4, 2)
scalar = 0.98

print(f"obj1 = {obj1}\nobj2 = {obj2}\nscalar = {scalar}")
print(f"lerp = {lerp(obj1, obj2, scalar)}")

obj1 = Vector([Complex(2, 3), 1])
obj2 = Vector([4, Complex(9, 2)])
scalar = 0.3

print(f"\nobj1 = {obj1}\nobj2 = {obj2}\nscalar = {scalar}")
print(f"lerp = {lerp(obj1, obj2, scalar)}")

obj1 = Matrix([[2, 1], [Complex(2, 3), 4]])
obj2 = Matrix([[20, Complex(10, 10)], [30, 40]])
scalar = 0.5

print(f"\nobj1 = \n{obj1}\nobj2 = \n{obj2}\nscalar = {scalar}")
print(f"lerp = \n{lerp(obj1, obj2, scalar)}")

print("\n-------Complex Ex03: Vector dot product-------")

v = Vector([1, Complex(1, 1)])
w = Vector([2, Complex(2, 2)])

print(f"v = {v}\nw = {w}")
print(f"v.dot(w) = {v.dot(w)}")

print("\n-------Complex Ex04: Vector Norm-------")

v = Vector([1, Complex(2, 2), 3])

print(f"v = {v}")
print(f"v.norm_1 = {v.norm_1()}\nv.norm = {v.norm()}\nv.norm_inf = {v.norm_inf()}")

v = Vector([-1, Complex(-1, -2)])

print(f"\nv = {v}")
print(f"v.norm_1 = {v.norm_1()}\nv.norm = {v.norm()}\nv.norm_inf = {v.norm_inf()}")

print("\n-------Complex Ex05: Vector Cosine-------")
v = Vector([1, Complex(2, 2), 3])
w = Vector([4, 5, Complex(5, 6)])

print(f"v = {v}\nw = {w}")
print(f"angle_cos(v, w) = {angle_cos(v, w)}")

print("\n-------Complex Ex06: 3D Vector Cross product-------")
v = Vector([1, Complex(2, 2), 3])
w = Vector([4, 5, Complex(5, 6)])

print(f"v = {v}\nw = {w}")
print(f"cross_product(v, w) = {cross_product(v, w)}")

print("\n-------Complex Ex07: Matrix multiplication-------")
print("---Matrix * Vector---")
m = Matrix([[2, Complex(3, 2)],[-2, Complex(1, 2)]])
v = Vector([4, Complex(2, 4)])

print(f"m = \n{m}\nv = {v}")
print(f"m.mul_vec(v) = {m.mul_vec(v)}")
print("\n---Matrix * Matrix---")
m1 = Matrix([[3, -5], [6, 8], [1, Complex(1, 1)]])
m2 = Matrix([[2, Complex(3, 2), 1], [4, 2, 1]])

print(f"m1 = \n{m1}\nm2 = \n{m2}")
print(f"m1.mul_mat(m2) = \n{m1.mul_mat(m2)}")

print("\n-------Complex Ex08: Matrix trace-------")
m = Matrix([[-2, -8, 4], [1, -23, 4], [0, 6, Complex(4, 5)]])

print(f"m = \n{m}")
print(f"m.trace() = {m.trace()}")

print("\n-------Complex Ex09: Matrix Transpose-------")
m = Matrix([[1, 2, Complex(2, 2)], [4, 5, 6], [Complex(7, 7), 8, 9]])

print(f"m = \n{m}")
m2 = m.transpose()
print(f"m.transpose() = \n{m2}")
print(f"transpose back = \n{m2.transpose()}")

print("\n-------Complex Ex10: Matrix row-echelon form-------")
m = Matrix([[1, Complex(2, 2), 3, 4], [0, 0, 5, 6], [7, 8, 9, 1]])

print(f"m = \n{m}")
print(f"m.row_echelon() = \n{m.row_echelon()}")

print("\n-------Complex Ex11: Matrix determinant-------")
m = Matrix([[2, 0, 0], [0, Complex(2, 2), 0], [0, 0, 2]])

print(f"m = \n{m}")
print(f"m.determinant() = \n{m.determinant()}")

print("\n-------Complex Ex12: Matrix Inverse-------")
m = Matrix([[2, 0, 0], [0, Complex(2, 2), 0], [0, 0, 2]])

print(f"m = \n{m}")
print(f"m.inverse() = \n{m.inverse()}")

print("\n-------Complex Ex13: Matrix Rank-------")
m = Matrix([[8, Complex(5, 5), -2], [4, 7, 20], [7, 6, 1], [21, 18, 7]])

print(f"m = \n{m}")
print(f"m.rank() = {m.rank()}")