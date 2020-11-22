# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        return f'{self.name} is started'


    def stop(self):
        return f'{self.name} is stopped'


    def turn(self, direction):
        return f'{self.name} is turned ' + direction


    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')
        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'


first_car = PoliceCar(60, 'yellow', 'police car')
second_car = WorkCar(50, 'black', 'work car')
third_car = SportCar(100, 'blue', 'sport car')
fourth_car = TownCar(80, 'orange', 'town car')

print(first_car.is_police)
print(second_car.go())
print(second_car.stop())
print(third_car.turn('left'))
print(fourth_car.turn('right'))
print(third_car.show_speed())