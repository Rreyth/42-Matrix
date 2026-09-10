from Matrix import Matrix

# EX08: Trace
print("-------Matrix trace-------")
m = Matrix([[1, 0], [0, 1]])

print(f"m = \n{m}")
print(f"m.trace() = {m.trace()}")

m = Matrix([[2, -5, 0], [4, 3, 7], [-2, 3, 4]])

print(f"\nm = \n{m}")
print(f"m.trace() = {m.trace()}")

m = Matrix([[-2, -8, 4], [1, -23, 4], [0, 6, 4]])

print(f"\nm = \n{m}")
print(f"m.trace() = {m.trace()}")
