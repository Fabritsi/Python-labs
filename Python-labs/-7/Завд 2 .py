import math
a = int(input("row number:"))
b = int(input("column number:"))
n = int(input("n = "))
matrix = []
for i in range(a):
    matrix.append([])
    for j in range(b):
        el = math.sin(((i^2)-(j^2))/n)
        matrix[i].append(el)
print(matrix)

index1 = 0
index2 = 0
k = matrix[0][0]

for i in range(a):
    for j in range(b):
        if math.fabs(k) < math.fabs(matrix[i][j]):
            k = matrix[i][j]
            index1 = i
            index2 = j

print(k, i, j)



