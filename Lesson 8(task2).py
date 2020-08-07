"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой."""


class DontDoIt:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @staticmethod
    def divide(num1, num2):
        try:
            return num1 / num2
        except:
            return (f"Конец вселенной")


div = DontDoIt(34, 47)
print(div.num1, div.num2)
print(DontDoIt.divide(25, 0))
print(div.divide(100, 0))
