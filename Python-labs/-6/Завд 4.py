import random
n = (int(input("n =")))
A = [random.randint(-2,2) for i in range(n)]
print(A)

A1 = []
A2 = []

for el in A:
    if -1 < el < 1:
        A1.append(el)
    else:
        A2.append(el)
A = A1 +  A2

print(A)

