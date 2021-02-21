a = int(input('Введіть значення а:'))
b = int(input('Введіть значення b:'))
c = int(input('Введіть значення c:'))
if a > b :
    min = b
else:
    min = a
if b > c :
    max = b
else:
    max = c
P = min + (max**2)
print('Р= {0}'. format(P))