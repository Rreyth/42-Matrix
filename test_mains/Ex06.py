import sys
sys.path.append('../')

from classes.Vector import Vector
from functions.vector_calc import cross_product

# EX06: Cross product
print("-------3D Vector Cross product-------")

v = Vector([0, 0, 1])
w = Vector([1, 0, 0])

print(f"v = {v}\nw = {w}")
print(f"cross_product(v, w) = {cross_product(v, w)}")

v = Vector([1, 2, 3])
w = Vector([4, 5, 6])

print(f"\nv = {v}\nw = {w}")
print(f"cross_product(v, w) = {cross_product(v, w)}")

v = Vector([4, 2, -3])
w = Vector([-2, -5, 16])

print(f"\nv = {v}\nw = {w}")
print(f"cross_product(v, w) = {cross_product(v, w)}")
