"""Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police, direction):
        self.speed = speed
        self.color = color
        self.name = name
        self.direction = direction
        self.is_police = bool(is_police)

    def go(self):
        print("Поехали!")

    def stop(self):
        print("Притормозим")

    def turn(self, direction):
        print(f"Едем {direction}")

    def show_speed(self, speed):
        return(f"Текущая скорость {speed}\n")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name, is_police, direction)

    def show_speed(self, speed):
        if speed >= 60:
            print("Вы превысили скорость!\n")
        else:
            print("Так держать!\n")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name, is_police, direction)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name, is_police, direction)

    def show_speed(self, speed):
        if speed >= 40:
            print("Превышаем?\n")
        else:
            print("Так держать!\n")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, direction):
        super().__init__(speed, color, name, is_police, direction)


car_1 = TownCar(50, "Grey", "Nissan Qashkai", False, "налево")
print(f"Автомобиль {car_1.name} едет со скоростью {car_1.speed}км/ч и поворачивает {car_1.direction}")
car_1.show_speed(car_1.speed)


car_2 = SportCar(60, "Yellow", "Ferrari F50", False, "направо")
print(f"Автомобиль {car_2.name} едет со скоростью {car_2.speed}км/ч и поворачивает {car_2.direction}\n")

car_3 = WorkCar(100, "Blue", "Ford Transit", False, "направо")
print(f"Автомобиль {car_3.name} едет со скоростью {car_3.speed}км/ч и поворачивает {car_3.direction}")
car_1.show_speed(car_3.speed)

car_4 = PoliceCar(100, "Monochrome", "Chevrolet Tahoe", True, "назад")
print(f"Автомобиль {car_4.name} едет со скоростью {car_4.speed}км/ч и поворачивает {car_4.direction}\n")

