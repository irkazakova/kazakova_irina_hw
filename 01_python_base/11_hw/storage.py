# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры,
# общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники
# на склад и передачу в определённое подразделение компании. Для хранения данных о наименовании и
# количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру
# (например, словарь).

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class Storage:
    def __init__(self, name):
        self.name = str(name)
        # Словарь в экземпляре склада для хранения информации {тип оргтехники: количество}
        self.structure = {}

    def addEquipment(self, office_equipment, quantity):
        old_quantity = self.structure.get(office_equipment.name, 0)
        print(old_quantity)
        self.structure.update({office_equipment.name: old_quantity + quantity})

    def removeEquipment(self, office_equipment, quantity):
        old_quantity = self.structure.get(office_equipment.name, 0)
        if old_quantity - quantity < 0:
            print('На складе отсутствует офисная техника указанного вида: {} в необходимом количестве'.format(
                office_equipment.name))
        else:
            self.structure.update({office_equipment.name: old_quantity - quantity})

    @staticmethod
    def validate(quantity):
        try:
            q = int(quantity)
            if q <= 0:
                raise ValueError('Необходимо указывать целое число техники')
        except ValueError:
            print('На складе отсутствует офисная техника указанного вида в необходимом количестве')

    def __str__(self):
        return 'Текущее состояние склада {}: {}'.format(self.name, self.structure)


class OfficeEquipment:
    def __init__(self, name):
        self.name = str(name)


class Printer(OfficeEquipment):
    def __init__(self):
        super().__init__('принтер')


class Scanner(OfficeEquipment):
    def __init__(self):
        super().__init__('сканер')


class Copier(OfficeEquipment):
    def __init__(self):
        super().__init__('ксерокс')


storage_name = input('Введите имя склада, с которым хотите работать: ')
storage = Storage(storage_name)
user_command = 'add'
while user_command != 'stop':
    user_command = input('Задайте операцию, которую хотите выполнить, возможные варианты: add, remove, stop ')
    if user_command == 'stop':
        print(storage)
    else:
        if user_command not in ('add', 'remove'):
            print('Задана некорректная операция, попробуйте еще раз, возможные варианты: add, remove, stop')
            continue
        else:
            t = input("Введите тип техники, возможные варианты принтер, сканер, ксерокс: ")
            q = input('Введите количество: ')

            Storage.validate(q)

            if t.lower() == 'принтер':
                office_equipment = Printer()
            elif t.lower() == 'сканер':
                office_equipment = Scanner()
            elif t.lower() == 'ксерокс':
                office_equipment = Copier()
            else:
                office_equipment = OfficeEquipment(t.lower())

            if user_command == 'add':
                storage.addEquipment(office_equipment, int(q))
                print(storage)
            else:
                storage.removeEquipment(office_equipment, int(q))
                print(storage)
