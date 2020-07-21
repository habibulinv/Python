"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""

from sys import argv

script_name, hours, payments, bonus = argv

"""ввод параметров через командную строку или через edit configuration"""

try:
    hours = int(hours)
    payments = int(payments)
    bonus = int(bonus)
    print(hours * payments + bonus)
except ValueError:
    print("В параметры должны быть внесены числа")


