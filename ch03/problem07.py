import math

x1 = input('x1 : ')
y1 = input('y1 : ')
x2 = input('x2 : ')
y2 = input('y2 : ')

distance = math.sqrt((float(x2) - float(x1)) ** 2 + (float(y2) - float(y1)) ** 2)
print(distance)

#형변환을 배웠다