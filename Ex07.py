from Vector import *
from Matrix import *

# EX07: Linear map, Matrix multiplication
print("-------Matrix multiplication-------")
print("---Matrix * Vector---")
m = Matrix([[1, 0],[0, 1]])
v = Vector([4, 2])

print(f"m = \n{m}\nv = {v}")
print(f"m.mul_vec(v) = {m.mul_vec(v)}")

m = Matrix([[2, 0],[0, 2]])
v = Vector([4, 2])

print(f"\nm = \n{m}\nv = {v}")
print(f"m.mul_vec(v) = {m.mul_vec(v)}")

m = Matrix([[2, -2],[-2, 2]])
v = Vector([4, 2])

print(f"\nm = \n{m}\nv = {v}")
print(f"m.mul_vec(v) = {m.mul_vec(v)}")

print("\n---Matrix * Matrix---")

m1 = Matrix([[1, 0], [0, 1]])
m2 = Matrix([[1, 0], [0, 1]])

print(f"m1 = \n{m1}\nm2 = \n{m2}")
print(f"m1.mul_mat(m2) = \n{m1.mul_mat(m2)}")

m1 = Matrix([[1, 0], [0, 1]])
m2 = Matrix([[2, 1], [4, 2]])

print(f"\nm1 = \n{m1}\nm2 = \n{m2}")
print(f"m1.mul_mat(m2) = \n{m1.mul_mat(m2)}")

m1 = Matrix([[3, -5], [6, 8], [1, 1]])
m2 = Matrix([[2, 1, 1], [4, 2, 1]])

print(f"\nm1 = \n{m1}\nm2 = \n{m2}")
print(f"m1.mul_mat(m2) = \n{m1.mul_mat(m2)}")
