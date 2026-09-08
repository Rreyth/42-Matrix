from Vector import *

# EX04: Norm
print("-------Vector Norm-------")

v = Vector([0, 0, 0])

print(f"v = {v}")
print(f"v.norm_1 = {v.norm_1()}\nv.norm = {v.norm()}\nv.norm_inf = {v.norm_inf()}")

v = Vector([1, 2, 3])

print(f"\nv = {v}")
print(f"v.norm_1 = {v.norm_1()}\nv.norm = {v.norm()}\nv.norm_inf = {v.norm_inf()}")

v = Vector([-1, -2])

print(f"\nv = {v}")
print(f"v.norm_1 = {v.norm_1()}\nv.norm = {v.norm()}\nv.norm_inf = {v.norm_inf()}")
