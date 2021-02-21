import random
import math
row = int(input("rows:"))
column = int(input("columns:"))
A = [[random.randint(-10,10) for j in range(column)] for i in range(row)]
print(A)

l = 0
B = []
for i in range(row):
    for j in range(column):
        if A[j][i] < 0:
            l += math.fabs(A[j][i])
    B.append(l)
    l = 0
print(B)
C = sorted(B)
print(C)

T = [[random.randint(0,0) for j in range(column)] for i in range(row)]
for i in range(row):
    for j in range(column):
        if C[i] == B[j]:
            for k in range(column):
                T[k][j] = A[k][i]
print(T)

