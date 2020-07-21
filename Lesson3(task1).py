"""func принимает два числа 'a' и 'b'.

Аргументы
    а - делимое
    b - делитель
"""


def func(a=input("Введите делимое A: "), b=input("Введите делитель B: ")):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("В параметры должнs быть внесены числа")
    try:
        return (a / b)
    except ZeroDivisionError:
        return ("на ноль делить нельзя")



print(func())
