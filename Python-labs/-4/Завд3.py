import math
x1 = float(input('Введіть координати х1:')) #точ.А
y1 = float(input('Введіть координати y1:'))

x2 = float(input('Введіть координати х2:')) #точ.B
y2 = float(input('Введіть координати y2:'))

x3 = float(input('Введіть координати х3:')) #точ.C
y3 = float(input('Введіть координати y3:'))

AB = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
AC = math.sqrt(((x3-x1)**2)+((y3-y1)**2))
BC = math.sqrt(((x3-x2)**2)+((y3-y2)**2))

if AB>=BC and AB>=AC :
    print('Найбільша сторона: AB')
else:
    if BC >= AC:
        print('Найбільша сторона: BC')
    else:
        print('Найбільша сторона: AC')


        

