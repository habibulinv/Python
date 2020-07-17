"""
my_func() принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    my_f = (a, b, c)
    min(my_f)
    print(sum(my_f) - min(my_f))


my_func(a=164, c=27, b=86)
