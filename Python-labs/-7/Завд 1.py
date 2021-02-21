import random
n = int(input("rows and columns="))
A = [[random.randint(-10,10) for j in range(n)] for i in range(n)]
print(A)
d = 1
for i in range(n):
    for j in range(n):
        if i == j:
            break
        if i != j:
            if A[i][j] > 0:
                d *= A[i][j]
                print(A[i][j])


print("d=",d)
