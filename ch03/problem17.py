import math

x = input('x : ')
n = input('n : ')

guess = x / 2
for i in range(0, n):
    guess = (guess + x / guess) / 2
print(guess)
print(abs(math.sqrt(x) - guess))
