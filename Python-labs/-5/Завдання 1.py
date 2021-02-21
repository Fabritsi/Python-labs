import math
x=float(input("x="))
n=int(input("n="))
S=0
for i in range (1,n+1):
    S+=(math.sin(x))**n
print(S)

