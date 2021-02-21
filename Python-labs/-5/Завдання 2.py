n = int(input("n="))
S = 0
i = 1
count = 0
d = n
while n > 0:
    S += n%10
    Ser_ar = S / i
    i += 1
    n = n//10
print("Середнє арифметичне={0}".format(Ser_ar))
while d > 0:
    c = d%10
    if c < Ser_ar:
        count += 1
        print("Цифра {0} менше за середнє арифметичне".format(c))
    d = d//10
print("Кількість цифр менших за середнє арифметичне:{0}".format(count))


