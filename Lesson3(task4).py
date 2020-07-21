"""my_func принимает действительное положительное число 'x' и целое отрицательное число 'y'
Возводит 'x' в степень 'y'

Более простое решение:
def my_func(x, y):
    x = abs(x)
    y = abs(y) * (-1)
    return x ** y

"""


def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
        if x <= 0 or y >= 0:
            return ("Вы ввели не верное значение х и y. Х - положительный, Y - отрицательный")
        else:
            result = 1
            for _ in range(abs(y)):
                result *= 1 / x
            return f'Резултат {round(result, 6)}'
    except ValueError:
        return "Нужно ввести именно число"



print(my_func(40, -2))
