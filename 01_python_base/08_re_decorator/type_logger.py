# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько -
# + выводить данные о каждом через запятую;
# - можете ли вы вывести тип значения функции?
# + Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора?
# + Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)


def type_logger(function):
    def wrapper(*args, **kwargs):
        res = function(*args, **kwargs)
        print('a = {}{}{}'.format(function.__name__, args, kwargs))
        print(*map(lambda x: '{}: {}, '.format(x, type(x)), args))
        print('a = {}({})'.format(function.__name__, *map(lambda x: '{}: {}, '.format(x, type(x)), args),
                                  *map(lambda x: '{}: {}, '.format(x, type(x)), kwargs)))
        return res

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


@type_logger
def calc_d(x, y):
    return x ** y


print(calc_cube(5))

print(calc_d(5, 3))
