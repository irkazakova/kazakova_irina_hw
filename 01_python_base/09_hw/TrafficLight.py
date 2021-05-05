# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep
import datetime


class TrafficLight:
    def __init__(self):
        self.__colour = None

    def running(self, argv):
        while True:
            self.__colour = 'Красный'
            print('Цвет светофора: {}, время: {}'.format(self.__colour, datetime.datetime.now()))
            sleep(7)
            self.__colour = 'Желтый'
            print('Цвет светофора: {}, время: {}'.format(self.__colour, datetime.datetime.now()))
            sleep(5)
            self.__colour = 'Зеленый'
            print('Цвет светофора: {}, время: {}'.format(self.__colour, datetime.datetime.now()))
            sleep(3)


if __name__ == '__main__':
    import sys

    traffic_light = TrafficLight()
    exit(traffic_light.running(sys.argv))
