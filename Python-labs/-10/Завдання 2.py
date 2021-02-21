
class Monitor():
    def __init__(self, manufacturer, dateCreate, dateBuy, price, typeof, size):
        self.manufacturer = manufacturer
        self.dateCreate = dateCreate
        self.dateBuy = dateBuy
        self.price = price
        self.typeof = typeof
        self.size = size

    def age(self):
        return 2020 - self.dateCreate


    def DisplayTheImage(self, ImageSize, size):
        if ImageSize == size:
            print("Зображення можна вивести без масштабування")
        else:
            #визначити коефіцієнт масштабування
            size - ImageSize #?
            print("Зображення можна вивести з масштабуванням")


Monitor_1 = Monitor('Samsung', 2007, 2009, 1562, 'Проекційний', 35)

print('Вкажіть розмір зображення:')
ImageSize = int(input('Розмір зображення:'))
size = int(input('Розмір Монітора: '))


print('З дати виробництва пройшло {0} років'.format(Monitor_1.age()))
