import random
column = int(input("columns:"))
row = int(input("rows:"))
A = [[random.randint(-10,10) for i in range(column)] for j in range(row)]
print(A)

for j in range(row):
    for i in range(column):
        if i % 2 == 0:
            A[i].sort(reverse=True)

print(A)

