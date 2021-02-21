x=float(input("Введіть змінну x="))
e=float(input("Введіть точність е="))
import math
d=x
n=2
while math.fabs(1-(x**2/((n-1)**2)*(math.pi**2)))>e:
    d*=(1-(x**2/((n-1)**2)*(math.pi**2)))
    n+=1
print("Добуток:{0}".format(d))
if math.sin(x)-d<e:
    print("Рівність справедлива d=sin(x)")
else:
     print("Рівнсть не справедлива")
     

