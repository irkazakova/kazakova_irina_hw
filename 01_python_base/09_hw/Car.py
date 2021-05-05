# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return '{} поехала'.format(self.name)

    def stop(self):
        return '{} остановилась'.format(self.name)

    def turn_right(self):
        return '{} повернула направо'.format(self.name)

    def turn_left(self):
        return '{} повернула налево'.format(self.name)

    def show_speed(self):
        return 'Текущая скорость {} {}'.format(self.name, self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        print('Текущая скорость {} {}'.format(self.name, self.speed))
        if self.speed > 40:
            return 'Текущая скорость {} {} превышает допустимую'.format(self.name, self.speed)


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        print('Текущая скорость {} {}'.format(self.name, self.speed))
        if self.speed > 60:
            return 'Текущая скорость {} {} превышает допустимую'.format(self.name, self.speed)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


lamborgini = SportCar(150, 'Red', 'Lamborgini')
ford = TownCar(50, 'White', 'Ford Fusion')
niva = WorkCar(70, 'Rose', 'Lada')
police = PoliceCar(110, 'Blue',  'Police Car')
print(lamborgini.is_police)
print(ford.is_police)
print(niva.is_police)
print(police.is_police)
print(lamborgini.turn_left())
print(ford.go())
print(niva.stop())
print(police.turn_right())
print(lamborgini.show_speed())
print(ford.show_speed())
print(niva.show_speed())
print(police.show_speed())
