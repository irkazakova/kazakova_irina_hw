# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно.
# Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.


class Matrix:
    def __init__(self, matrix_as_list):
        self.matrix_as_list = matrix_as_list

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix_as_list]))

    def __add__(self, other_matrix):
        # По идее, если писать в реальности, наверное надо добавить проверку одинаковой размерности матриц
        first_list = self.matrix_as_list;
        second_list = other_matrix.matrix_as_list;
        result_matrix_as_list = []
        for i in range(len(first_list)):
            result_matrix_row = [x + y for (x, y) in zip(first_list[i], second_list[i])]
            result_matrix_as_list.append(result_matrix_row)
        return Matrix(result_matrix_as_list)

first_matrix = Matrix([[1, 2, 3],
                    [2, 4, 6],
                    [3, 6, 9]])
second_matrix = Matrix([[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]])
print(first_matrix)
print(second_matrix)
print(first_matrix + second_matrix)

