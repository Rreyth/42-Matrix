import sys
sys.path.append('../')

from classes.Matrix import Matrix

# EX11: Determinant
print("-------Matrix determinant-------")
m = Matrix([[1, -1], [-1, 1]])

print(f"m = \n{m}")
print(f"m.determinant() = \n{m.determinant()}")

m = Matrix([[2, 0, 0], [0, 2, 0], [0, 0, 2]])

print(f"\nm = \n{m}")
print(f"m.determinant() = \n{m.determinant()}")

m = Matrix([[8, 5, -2], [4, 7, 20], [7, 6, 1]])

print(f"\nm = \n{m}")
print(f"m.determinant() = \n{m.determinant()}")

m = Matrix([[8, 5, -2, 4], [4, 2.5, 20, 4], [8, 5, 1, 4], [28, -4, 17, 1]])

print(f"\nm = \n{m}")
print(f"m.determinant() = \n{m.determinant()}")
