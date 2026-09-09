from calculations import *

# EX14: Bonus: Projection matrix
print("-------Projection matrix-------")

fov = 90
ratio = 16/9
near = 0
far = 10

print(f"projection({fov}, {ratio}, {near}, {far}) = \n{projection(fov, ratio, near, far)}")

# 0.5625001838221594, 0.0, 0.0, 0.0
# 0.0, 1.00000032679495, 0.0, 0.0
# 0.0, 0.0, -1.0, -1.0
# 0.0, 0.0, -0.0, 0.0

fov = 84
ratio = 16/9
near = 2
far = 42

print(f"projection({fov}, {ratio}, {near}, {far}) = \n{projection(fov, ratio, near, far)}")

# 0.6247197311858411, 0.0, 0.0, 0.0
# 0.0, 1.1106128554414954, 0.0, 0.0
# 0.0, 0.0, -1.05, -1.0
# 0.0, 0.0, -2.1, 0.0