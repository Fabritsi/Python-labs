
studentDict = {"LessonName": "", "HoursNumber": 0, "Teacher": "", "Rating": 0}
arrayOfStudentDict = []

def serch(choose, criteria):
    if choose == 1:
        for i in range(len(arrayOfStudentDict)):
            if arrayOfStudentDict[i]["LessonName"] == criteria:
                print(arrayOfStudentDict[i])
    if choose == 2:
        for i in range(len(arrayOfStudentDict)):
            if arrayOfStudentDict[i]["HoursNumber"] == criteria:
                print(arrayOfStudentDict[i])
    if choose == 3:
        for i in range(len(arrayOfStudentDict)):
            if arrayOfStudentDict[i]["Teacher"] == criteria:
                print(arrayOfStudentDict[i])
    if choose == 4:
        for i in range(len(arrayOfStudentDict)):
            if arrayOfStudentDict[i]["Rating"] == criteria:
                print(arrayOfStudentDict[i])


while True:
    print("\n")
    print("1. Вивести всю інформацію\n"
          "2. Ввести данні про предмет\n"
          "3. Знайти предмет\n"
          "4. Вийти\n")

    choose = int(input("Виберіть номер:"))

    if choose == 1:
        print(arrayOfStudentDict)
    elif choose == 2:
        '''----Ввід даних про студента----'''
        Lesson = input("Введіть назву предмета: ")
        HoursNumber = int(input("Введіть к-ть годин: "))
        Teacher = input("Викладач: ")
        rating = int(input("Рейтинг: "))

        '''---Заповнення словника---'''
        studentDict["LessonName"] = Lesson
        studentDict["HoursNumber"] = HoursNumber
        studentDict["Teacher"] = Teacher
        studentDict["Rating"] = rating
        arrayOfStudentDict.append(studentDict)
    elif choose == 3:
        print("Знайти за:\n"
              "1.Назва предмета\n"
              "2.К-ть годин\n"
              "3.Викладач\n"
              "4.Рейтинг\n")
        choose2 = int(input("Виберіть номер: "))
        if choose2 == 1:
            searchCriteria = input("Введіть назву предмета: ")
            serch(1, searchCriteria)

        if choose2 == 2:
            searchCriteria = int(input("Введіть к-ть годин: "))
            serch(2, searchCriteria)
        if choose2 == 3:
            searchCriteria = int(input("Введіть викладача: "))
            serch(3, searchCriteria)
        if choose2 == 4:
            searchCriteria = int(input("Введіть рейтинг: "))
            serch(4, searchCriteria)
        print("\n")
    elif choose == 4:
        break
    else:
        print("Ведіть коректне число\n")

