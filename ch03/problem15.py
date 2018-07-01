import math

n = input('n : ')

sum = 0
sign = 1
for i in range(1, n + 1):
    sum = float(sum) + sign * (4 / (2 * i - 1))
    sign = sign * (-1)

error = abs(math.pi - float(sum))
print(error)
