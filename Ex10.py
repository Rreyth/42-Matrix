from Matrix import Matrix

# EX10: row-echelon form
print("-------Matrix row-echelon form-------")
m = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

print(f"m = \n{m}")
print(f"m.row_echelon() = \n{m.row_echelon()}")

m = Matrix([[0, 1, 1], [0, 0, 5], [3, 3, 3]])

print(f"\nm = \n{m}")
print(f"m.row_echelon() = \n{m.row_echelon()}")

m = Matrix([[1, 2], [3, 4]])

print(f"\nm = \n{m}")
print(f"m.row_echelon() = \n{m.row_echelon()}")

m = Matrix([[1, 2], [2, 4]])

print(f"\nm = \n{m}")
print(f"m.row_echelon() = \n{m.row_echelon()}")

m = Matrix([[8, 5, -2, 4, 28], [4, 2.5, 20, 4, -4], [8, 5, 1, 4, 17]])

print(f"\nm = \n{m}")
print(f"m.row_echelon() = \n{m.row_echelon()}")

m = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(f"\nm = \n{m}")
print(f"m.row_echelon() = \n{m.row_echelon()}")

m = Matrix([[1, 2, 3, 4], [0, 0, 5, 6], [7, 8, 9, 1]])

print(f"\nm = \n{m}")
print(f"m.row_echelon() = \n{m.row_echelon()}")
