from Vector import *
from Matrix import *
from Complex import *
from calculations import *

# EX15: Bonus: Complex
print("-------Complex-------")
print("-------Complex class-------")

nb1 = Complex(3, 4)
nb2 = Complex(1, 2)

print(f"nb1({nb1}) + nb2({nb2}) = {nb1 + nb2}")
print(f"nb1({nb1}) + 5 = {nb1 + 5}")
print(f"nb2({nb2}) + nb1({nb1}) = {nb2 + nb1}")
print(f"5 + nb1({nb1}) = {5 + nb1}")
print(f"nb1({nb1}) - nb2({nb2}) = {nb1 - nb2}")
print(f"nb1({nb1}) - 5 = {nb1 - 5}")
print(f"nb2({nb2}) - nb1({nb1}) = {nb2 - nb1}")
print(f"5 - nb1({nb1}) = {5 - nb1}")
print(f"nb1({nb1}) * nb2({nb2}) = {nb1 * nb2}")
print(f"nb1({nb1}) * 5 = {nb1 * 5}")
print(f"nb2({nb2}) * nb1({nb1}) = {nb2 * nb1}")
print(f"5 * nb1({nb1}) = {5 * nb1}")
print(f"nb1({nb1}) / nb2({nb2}) = {nb1 / nb2}")
print(f"nb1({nb1}) / 5 = {nb1 / 5}")
print(f"nb2({nb2}) / nb1({nb1}) = {nb2 / nb1}")
print(f"4 / nb2({nb2}) = {4 / nb2}")
print(f"nb1({nb1}).absolute() = {nb1.absolute()}")
print(f"nb1({nb1}).squareRoot() = {nb1.squareRoot()}")

print("\n-------Complex Vector-------")
print("\n-------Complex Matrix-------")