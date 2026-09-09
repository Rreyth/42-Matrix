from Matrix import *

# EX13: Rank
print("-------Matrix Rank-------")
m = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

print(f"m = \n{m}")
print(f"m.rank() = {m.rank()}")

m = Matrix([[1, 2, 0, 0], [2, 4, 0, 0], [-1, 2, 1, 1]])

print(f"\nm = \n{m}")
print(f"m.rank() = {m.rank()}")

m = Matrix([[8, 5, -2], [4, 7, 20], [7, 6, 1], [21, 18, 7]])

print(f"\nm = \n{m}")
print(f"m.rank() = {m.rank()}")
