# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def __add__(self, other):
        print('Сумма z1 и z2 равна')
        return '{} + {} * i'.format(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        print('Произведение z1 и z2 равно')
        return'{} + {} * i'.format(self.a * other.a - (self.b * other.b), self.b * other.a)

    def __str__(self):
        return '{} + {} * i'.format(self.a, self.b)


z_1 = ComplexNumber(1, -2.5)
z_2 = ComplexNumber(3, 4.89)
print(z_1)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)
