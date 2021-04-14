# 1.
# Написать функцию email_parse(<email_address>), которая при помощи регулярного
# выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError.
# Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?

import re

RE_EMAIL = re.compile('^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$')


def email_is_valid(email):
    return RE_EMAIL.match(email)


RE_USERNAME = re.compile('^([a-z0-9_-]+\.)*[a-z0-9_-]+')
RE_DOMAIN = re.compile('[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$')


def email_parse(email):
    email_dict = {'username': RE_USERNAME.match(email).group(0), 'domain': RE_DOMAIN.search(email).group(0)}
    print(email_dict)


def main():
    email = input()
    if email_is_valid(email):
        email_parse(email)
    else:
        msg = 'wrong email: {}'.format(email)
        raise ValueError(msg)


if __name__ == '__main__':
    main()
