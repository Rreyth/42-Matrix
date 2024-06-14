from Matrix import Matrix
from Vector import Vector
from calculations import lerp

# EX02: Linear interpolation
print("-------linear interpolation-------")

obj1 = 21
obj2 = 42
scalar = 0.98

print(f"obj1 = {obj1}\nobj2 = {obj2}\nscalar = {scalar}")
print(f"lerp = {lerp(obj1, obj2, scalar)}")

obj1 = Vector([2, 1])
obj2 = Vector([4, 2])
scalar = 0.3

print(f"\nobj1 = {obj1}\nobj2 = {obj2}\nscalar = {scalar}")
print(f"lerp = {lerp(obj1, obj2, scalar)}")

obj1 = Matrix([[2, 1], [3, 4]])
obj2 = Matrix([[20, 10], [30, 40]])
scalar = 0.5

print(f"\nobj1 = \n{obj1}\nobj2 = \n{obj2}\nscalar = {scalar}")
print(f"lerp = \n{lerp(obj1, obj2, scalar)}")