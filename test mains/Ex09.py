import sys
sys.path.append('../')

from classes.Matrix import Matrix

# EX09: Transpose
print("-------Matrix Transpose-------")
m = Matrix([[1, 2], [3, 4], [5, 6]])

print(f"m = \n{m}")
print(f"m.transpose() = \n{m.transpose()}")

m = Matrix([[1, 2, 3], [4, 5, 6]])

print(f"\nm = \n{m}")
print(f"m.transpose() = \n{m.transpose()}")

m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(f"\nm = \n{m}")
m2 = m.transpose()
print(f"m.transpose() = \n{m2}")
print(f"transpose back = \n{m2.transpose()}")
