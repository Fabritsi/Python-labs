n=int(input("Введіть номер n-го елемента: "))
A =[1, 7, 7 ,7]
for i in range(4,n+1):
    A.append(((A[i-1])*(1+A[i-2])+(A[i-3]))/A[i-4])
print(A[n-1])



