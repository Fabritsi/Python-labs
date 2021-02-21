InspectorDict = {"LastName": "", "Name": "", "Surname": "", "BornDate": 0, "TypeOfCrime": "", "Judgment": "" }
arrayOfInspectorDict = []

def serch(choose, criteria):
    if choose == 1:
        for i in range(len(arrayOfInspectorDict)):
            if arrayOfInspectorDict[i]["LastName"] == criteria:
                print(arrayOfInspectorDict[i])
    if choose == 2:
        for i in range(len(arrayOfInspectorDict)):
            if arrayOfInspectorDict[i]["Name"] == criteria:
                print(arrayOfInspectorDict[i])
    if choose == 3:
        for i in range(len(arrayOfInspectorDict)):
            if arrayOfInspectorDict[i]["Surname"] == criteria:
                print(arrayOfInspectorDict[i])
    if choose == 4:
        for i in range(len(arrayOfInspectorDict)):
            if arrayOfInspectorDict[i]["BornDate"] == criteria:
                print(arrayOfInspectorDict[i])
    if choose == 5:
        for i in range(len(arrayOfInspectorDict)):
            if arrayOfInspectorDict[i]["TypeOfCrime"] == criteria:
                print(arrayOfInspectorDict[i])
    if choose == 6:
        for i in range(len(arrayOfInspectorDict)):
            if arrayOfInspectorDict[i]["Judgment"] == criteria:
                print(arrayOfInspectorDict[i])


while True:
    print("\n")
    print("1. Вивести всю інформацію\n"
          "2. Ввести данні про злочинця\n"
          "3. Знайти злочинця\n"
          "4. Вийти\n")

    choose = int(input("Виберіть позицію:"))

    if choose == 1:
        print(arrayOfInspectorDict)
    elif choose == 2:
        '''----Ввід даних про студента----'''
        LastName = input("Введіть прізвище: ")
        Name = input("Введіть ім'я: ")
        Surname = input("По - батькові: ")
        BornDate = int(input("Рік народження: "))
        TypeCrime = input("Вид злочину: ")
        Judgment = input("Покарання: ")

        InspectorDict = {"LastName": LastName, "Name": Name, "Surname": Surname, "BornDate": BornDate, "TypeOfCrime": TypeCrime, "Judgment": Judgment}

        '''---Заповнення словника---'''
        InspectorDict["LastName"] = LastName
        InspectorDict["Name"] = Name
        InspectorDict["Surname"] = Surname
        InspectorDict["BornDate"] = BornDate
        InspectorDict["TypeCrime"] = TypeCrime
        InspectorDict["Judgment"] = Judgment
     

        arrayOfInspectorDict.append(InspectorDict)
    elif choose == 3:
        print("Знайти за:\n"
              "1.Прізвище\n"
              "2.Ім'я\n"
              "3.По - батькові\n"
              "4.Рік народження\n"
              "5.Вид злочину\n"
              "6.Покарання\n")

        choose2 = int(input("Виберіть позицію: "))
        if choose2 == 1:
            searchCriteria = input("Введіть прізвище злочинця: ")
            serch(1, searchCriteria)

        if choose2 == 2:
            searchCriteria = input("Введіть ім'я злочинця: ")
            serch(2, searchCriteria)
        if choose2 == 3:
            searchCriteria = input("Введіть по - батькові злочинця: ")
            serch(3, searchCriteria)
        if choose2 == 4:
            searchCriteria = int(input("Введіть рік народження злочинця: "))
            serch(4, searchCriteria)
        if choose2 == 5:
            searchCriteria = input("Введіть вид злочину злочинця: ")
            serch(5, searchCriteria)
        if choose2 == 6:
            searchCriteria = input("Введіть покарання для злочинця: ")
            serch(6, searchCriteria)



        print("\n")
    elif choose == 4:
        break
    else:
        print("Ведіть коректне число\n")
