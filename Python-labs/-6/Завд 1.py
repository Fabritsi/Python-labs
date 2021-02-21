import random

n = int(input("Введіть кількість елементів n:"))
A=[random.randint(-25,25) for i in range(n)]
print(A)
d = 1
for i in range(n):
    if A[i]<0:
      d*=A[i]

print(d)


