import random
a = int(input("rows:"))
b = int(input("columns:"))
A = [[random.randint(-10,10) for i in range(b)] for j in range(a)]
print(A)

B = [[A[i][j] for i in range(a)]for j in range(b)]
print(B)
