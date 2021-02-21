import math
a = float(input('Введіть довжину сторони ромба:'))
c = float(input('Введіть значення кута між сторонами:'))
P = a * 4
S = (a**2) * math.sin(c)
print('Периметр = {0}, Площа = {1}'.format(P,S))