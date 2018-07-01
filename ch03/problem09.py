import math

a = input('a :')
b = input('b :')
c = input('c :')

s = (a + b + c) / 2
A = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(A)
