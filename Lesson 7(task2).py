"""Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""
from abc import ABC, abstractclassmethod

class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractclassmethod
    def consumption(self):
        pass

class Jacket(Clothes):
    def __init__(self, size, name):
        super().__init__(name)
        self.size = size

    @property
    def consumption(self):
        return (self.size / 6.5) + 0.5


class Costume(Clothes):
    def __init__(self, high, name):
        super().__init__(name)
        self.high = high

    @property
    def consumption(self):
        return (2 * self.high) + 0.3


jacket_1 = Jacket(50, "Gucci")
print(f"Расход ткани на пальто {jacket_1.name}: {round(jacket_1.consumption, 2)}")

costume_1 = Costume(52, "Brioni")
print(f"Расход ткани на костюм {costume_1.name}: {round(costume_1.consumption, 2)}")

costume_2 = Costume(58, "Dolce Gabanna")
print(f"Расход ткани на костюм {costume_2.name}: {round(costume_2.consumption, 2)}")

print("*" * 10)
print(f"Общий расход материала: {round(jacket_1.consumption + costume_1.consumption + costume_2.consumption, 2)}")
