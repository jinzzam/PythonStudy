import math

diameter = input('diameter : ')
price = input('price : ')

r = diameter / 2
A = math.pi * r ** 2
result = price / A
print(result)
