def z1():
    s={"Россия":"Москва","Франция":"Париж","Германия":"Берлин","Англия":"Лондон","США":"Вашингтон"}
    for key,value in s.items():
        print(key, "-", value)
    c=str(input("Введите страну: "))
    print("Столица: ", s[c])
    s1=list(s.keys())
    s1.sort()
    for i in s1:
        print(i, "-", s[i])

def z2():
    bukvi={1:["а","в","е","и","н","о","р","с","т"], 2:["д","к","л","м","п","у"], 3:["б","г","ё","ь","я"], 4:["й","ы"], 5:["ж","з","х","ц","ч"], 8:["ш","э","ю"], 10:["ф","щ","ъ"]}
    slovo=list(input("Введите слово: "))
    s=0
    for i in range(len(slovo)):
        for key,value in bukvi.items():
            if slovo[i] in value:
                s+=int(key)
    print("Стоимость слова: ", s)

def z3():
    students={"Иванов":["Русский","Английский"],"Смирнов":["Русский","Китайский"],"Васильев":["Русский","Английский","Китайский"],"Петров":["Русский","Татарский"],"Михайлов":["Русский","Чувашский","Китайский"]}
    languages=list(students.values())
    languages_new=[]
    for i in languages:
        languages_new.extend(i)
    k=languages_new.count("Китайский")
    print("Все языки которые знают студенты: ", sorted(set(languages_new)))
    print("Кол-во учеников, которые знают китайский: ", k)
print("---Задача 1---")
z1()
print("---Задача 2---")
z2()
print("---Задача 3---")
z3()