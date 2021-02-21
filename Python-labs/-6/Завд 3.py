import math
n = int(input("n ="))
def znach(x, y):
    A = []
    for i in range(n):
        A.append(x[i] * y[i])
    S = 0
    for i in range(n):
        S = A[i]
    return(S)
      
A = [int(input("A{0}=".format(i))) for i in range(n)]
B = [int(input("B{0}=".format(i))) for i in range(n)]
C = [int(input("C{0}=".format(i))) for i in range(n)]

S = 2 * znach(A, ) - 3 * znach(A, C)

print("Відповідь:{}".format(S))
