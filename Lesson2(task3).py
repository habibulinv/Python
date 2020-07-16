month = int(input("Введите месяц от 1 до 12 "))
year = {"Зима": (12, 1, 2), "Весна": (3, 4, 5), "Лето": (6, 7, 8), "Осень": (9, 10, 11)}


for key in year.keys():
    if month in year[key]:
        print(key)



