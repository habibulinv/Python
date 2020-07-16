print("Привет, заполните свои данные")

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
age = int(input("Ваш возраст: "))
acceptAge = 18

if age >= acceptAge:
    print("Добро пожаловать в наш закрытый клуб " + name + " " + surname + "!")
else:
    print(name + ", тебе пока рано вступать в наши ряды. Потерпи немного")


