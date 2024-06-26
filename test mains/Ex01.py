import sys
sys.path.append('../')

from classes.Vector import Vector
from functions.vector_calc import linear_combination

# EX01: Vector linear combination
print("-------Vector linear combination-------")
v = Vector([1, 2, 3])
w = Vector([0, 10, -100])

scalars = [10, -2]

print(f"\nvectors :\nv = {v}\nw = {w}\nscalars = {scalars}")
print("res = ", linear_combination([v, w], scalars))