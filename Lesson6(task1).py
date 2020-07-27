"""Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — 7.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт"""

from time import sleep


class TrafficLight:

    def __init__(self, color_1, color_2, color_3, color_4):
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.color_4 = color_4

    def running(self, delay_time_1, delay_time_2):
        count = 0
        light_line = [self.color_1, self.color_2, self.color_3, self.color_4]
        while count <= 2:
            for colors in light_line:
                print(colors)
                if colors == "Yellow":
                    sleep(delay_time_1)
                else:
                    sleep(delay_time_2)
            count += 1


traffic = TrafficLight("Red", "Yellow", "Green", "Yellow")
traffic.running(2, 7)





