from Matrix import Matrix
from Vector import Vector

# BASE VECTOR TESTS
print("-------Vector tests-------")
v = Vector([1, 2, 3, 4, 5, 6, 7, 8, 9])

print("vec size = ")
print(v.size())
print("\nprint vec")
print(v)
print("\nvec to matrix")
print(v.toMatrix(3, 3))

# EX00
v2 = Vector([1, 2, 3, 4, 5, 6, 7, 8, 9])
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

# BASE MATRIX TESTS
print("\n-------Matrix tests-------")
m = Matrix([[1, 1, 1],
        [2, 2, 2],
        [3, 3, 3],
        [4, 4, 4]])

print("matrix size = ")
print(m.size())
print("\nprint matrix")
print(m)
print("\nmatrix is square?")
print(m.isSquare())
print("\nmatrix to vector")
print(m.toVector())

m2 = Matrix([[1, 1, 1],
        [2, 2, 2],
        [3, 3, 3],
        [4, 4, 4]])

# EX00
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