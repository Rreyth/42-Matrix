import sys
sys.path.append('../')

from classes.Vector import Vector
from functions.vector_calc import angle_cos

# EX05: Cosine
print("-------Vector Cosine-------")

v = Vector([1, 0])
w = Vector([1, 0])

print(f"v = {v}\nw = {w}")
print(f"angle_cos(v, w) = {angle_cos(v, w)}")

v = Vector([1, 0])
w = Vector([0, 1])

print(f"\nv = {v}\nw = {w}")
print(f"angle_cos(v, w) = {angle_cos(v, w)}")

v = Vector([-1, 1])
w = Vector([1, -1])

print(f"\nv = {v}\nw = {w}")
print(f"angle_cos(v, w) = {angle_cos(v, w)}")
# print(f"rounded with subject precision = {round(angle_cos(v, w), 9)}")

v = Vector([2, 1])
w = Vector([4, 2])

print(f"\nv = {v}\nw = {w}")
print(f"angle_cos(v, w) = {angle_cos(v, w)}")
# print(f"rounded with subject precision = {round(angle_cos(v, w), 9)}")

v = Vector([1, 2, 3])
w = Vector([4, 5, 6])

print(f"\nv = {v}\nw = {w}")
print(f"angle_cos(v, w) = {angle_cos(v, w)}")
