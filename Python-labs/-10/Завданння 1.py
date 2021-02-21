class SraightLine:
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b

    def vvid(self):
        n = 3
        print("Введіть коефіцієнти: ")
        self.a = [int(input("Коефіцієнт a[{0}]=  ".format(i))) for i in range(1, n + 1)]
        self.b = [int(input("Коефіцієнт b[{0}]=  ".format(i))) for i in range(1, n + 1)]

    def print_k(self):
        print(f"StraightLine \n пряма a: {self.a}, \n пряма b :{self.b}")

    def peretyn(self, b):
        d = self.a[0] * self.a[1] * self.b[1]
        x = (self.a[0] * self.b[2] - self.b[1] * self.a[2]) / d
        y = (self.b[0] * self.a[2] - self.a[0] * self.b[2]) / d
        print(f'Прямі перетинаються у точці({x};{y})')

    def parallel(self,b):
        if self.a[0]/self.b[0] == self.a[1]/self.b[1] == self.a[2]/self.b[2]:
            print("Прямі а і b паралельні")
        else:
            print("Прямі а і b не паралельні")

    def belonging(self):
        x = float(input("x = "))
        y = float(input("y = "))
        if self.a[0] * x + self.a[1] * y + self.a[2] == 0:
            print('Точка належить')
        else:
            print('Точка не належить')


a = SraightLine()
b = SraightLine()
a.input()
a.print_k()
a.peretyn(b)
a.parallel(b)
a.belonging()

