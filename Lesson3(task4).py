"""my_func принимает действительное положительное число 'x' и целое отрицательное число 'y'
Возводит 'x' в степень 'y'

Более простое решение:
def my_func(x, y):
    x = abs(x)
    y = abs(y) * (-1)
    return x ** y

"""


def my_func(x, y):
    x = abs(x)
    y = abs(y) * (-1)
    while y < -1:
        x = x * x
        y += 1
    return 1 / x


print(my_func(40, -2))
