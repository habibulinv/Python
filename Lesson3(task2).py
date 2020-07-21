"""
PersonalData принимает параметры:
- имя,
- фамилия,
- год рождения,
- город проживания,
- email,
- телефон.

Функция принимает параметры как именованные аргументы.
"""

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
birth = input("Введите год рождения: ")
city = input("Введите город проживания: ")
email = input("Введите email: ")
phone = input("Введите телефон: ")

def personalData(name, surname, birth, city, email, phone):
    return(name, surname, birth, city, email, phone)


print(" ".join(personalData(name=name, surname=surname, email=email, phone=phone, city=city,
             birth=birth)))


