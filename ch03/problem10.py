import math

height = input('height : ')
angle = input('angle : ')

sinangle = math.pi / 180 * angle

length = float(height) / float(sinangle)

print(length)
