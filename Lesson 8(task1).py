"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""


class Data:
    def __init__(self, data):
        self.data = str(data)

    @classmethod
    def pars_data(cls, data):
        data_list = []
        for i in data.split():
            if i != '-':
                data_list.append(i)
        return int(data_list[0]), int(data_list[1]), int(data_list[2])

    @staticmethod
    def check_data(year, month, day):
        if 2010 <= year <= 2021:
            if 1 <= month <= 12:
                if 1 <= day <= 31:
                    return f'Дата введена верно'
                else:
                    return f'Дата должна содержать значение от 1 до 31'
            else:
                return f'Месяц должен содержать значение от 1 до 12'
        else:
            return f'Рассматривая период с 2010 по 2021'

    def __str__(self):
        return f'Текущая дата {Data.pars_data(self.data)}'


d = Data('11 - 1 - 2001')
print(d)
print(Data.check_data(2020, 11, 11))
print(d.check_data(2011, 13, 20))

