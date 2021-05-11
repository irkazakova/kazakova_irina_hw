# 1. Реализовать класс «Дата», функция-конструктор которого должна
# принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        return [int(x) for x in day_month_year.split('-')]

    @staticmethod
    def validate(day, month, year):
        # Не огонь проверка, конечно
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                return 'Дата корректна'
            else:
                return 'Некорректный месяц'
        else:
            return 'Некорректный день'

    def __str__(self):
        return f'Текущая дата {self.day_month_year}'


today = Date('11-1-2001')
print(today)
print(Date.extract('11-11-2011'))
print(Date.validate(11, 31, 2011))
