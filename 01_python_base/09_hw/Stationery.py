# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки {}'.format(self.title)


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Рисуем карандашом. Запуск отрисовки {}'.format(self.title)


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Рисуем ручкой. Запуск отрисовки {}'.format(self.title)


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return 'Рисуем маркером. Запуск отрисовки {}'.format(self.title)


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
