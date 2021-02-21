import math
import random

n = int(input("n:"))
x = int(input("x:"))
A = [ ]

i=0
while i<n:
    c = 0
    A.append((((-1)^(i+1))*math.sin(i*x)*math.cos(math.factorial(i))*x)+c)
    c = A[i]
    i+=1

print(A)

index = 0
min = A[0]
for i in range(n):
    if A[i] < min:
        min = A[i]
        index = i

print(index)


