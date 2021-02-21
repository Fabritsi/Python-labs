import random
candr = int(input("columns and rows:"))
A = [[random.randint(-10,10) for i in range(candr)] for j in range(candr)]
print(A)
B = []
l = 0
S = 0
for j in range(candr):
    for i in range(candr):
        if A[i][j] < 0:
            for k in range(candr):
                if A[k][j] == A[i][k]:
                    l += 1
                    if l == 3:
                        for t in range(candr):
                            S += A[i][t]
                        B.append(S)
    l = 0
    S = 0
print(B)

