# Написать декоратор с аргументом-функцией (callback), позволяющий валидировать
# входные значения функции и выбрасывать исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5

def val_checker(s):
    def wrapper(function):
        def called(*args, **kwargs):
            for itr in filter(s, args):
                return function(*args, **kwargs)
            else: raise ValueError('wrong val')
        return called
    return wrapper


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
