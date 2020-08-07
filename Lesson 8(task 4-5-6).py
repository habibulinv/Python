class Storehouse:
    def __init__(self, name, price, quantity, numb, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = numb
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def moving(self):
        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену за ед '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return Storehouse.moving(self)


class Printer(Storehouse):
    def to_print(self):
        return f'Напечатать {self.numb} раз'


class Scaner(Storehouse):
    def to_scan(self):
        return f'Отсканировать {self.numb} страниц'

class Xerox(Storehouse):
    def to_copy(self):
        return f'Сделать {self.numb} копий документа'



unit_1 = Printer('hp', 2000, 5, 7)
unit_2 = Scaner('Canon', 1200, 5, 10)
unit_3 = Xerox('Xerox', 1500, 1, 15)
print(unit_1.moving())
print(unit_1.to_print())
print(unit_2.to_scan())
print(unit_3.to_copy())
