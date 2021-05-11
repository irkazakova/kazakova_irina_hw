# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class DivisionByZeroException(Exception):
    def __init__(self, text):
        self.txt = text


a = input('Введите делимое: ')
b = input('Введите делитель: ')

try:
    a = int(a)
    b = int(b)
    if b == 0:
        raise DivisionByZeroException('На 0 делить нельзя')
except ValueError:
    print('Введено некорректное значение делимого или делителя')
except DivisionByZeroException:
    print(DivisionByZeroException)
else:
    print(a / b)
finally:
    print('Заканчиваем выполнение')
