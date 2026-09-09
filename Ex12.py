from Matrix import *

# EX12: Inverse
print("-------Matrix Inverse-------")
m = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

print(f"m = \n{m}")
print(f"m.inverse() = \n{m.inverse()}")

m = Matrix([[2, 0, 0], [0, 2, 0], [0, 0, 2]])

print(f"\nm = \n{m}")
print(f"m.inverse() = \n{m.inverse()}")

m = Matrix([[8, 5, -2], [4, 7, 20], [7, 6, 1]])

print(f"\nm = \n{m}")
print(f"m.inverse() = \n{m.inverse()}")
