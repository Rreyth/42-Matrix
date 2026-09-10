from matrix_calc import projection

# EX14: Bonus: Projection matrix
print("-------Projection matrix-------")

fov = 90
ratio = 16/9
near = 0
far = 10

print(f"projection({fov}, 16/9, {near}, {far}) = \n{projection(fov, ratio, near, far)}")

fov = 84
ratio = 16/9
near = 2
far = 42

print(f"\nprojection({fov}, 16/9, {near}, {far}) = \n{projection(fov, ratio, near, far)}")
