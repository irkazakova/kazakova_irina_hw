# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип:
# одна строка — один пользователь,
# разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл.
# Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи
import itertools

users_file_path = "resources/users.csv"
hobby_file_path = "resources/hobby.csv"
result_file_path = "resources/result.txt"

hobby_list = []
with open(hobby_file_path, 'r', encoding='utf-8') as hobby_file:
    for hobby_line in hobby_file:
        user_hobby = hobby_line.rstrip().split(',')
        hobby_list.append(user_hobby)
print(hobby_list)

users_list = []
with open(users_file_path, 'r', encoding='utf-8') as users_file:
    for users_line in users_file:
        user = users_line.rstrip().replace(',', ' ')
        users_list.append(user)
print(users_list)

if len(hobby_list) > len(users_list):
    exit(1)
else:
    with open(result_file_path, 'w', encoding='utf-8') as f:
        f.write(str(dict(itertools.zip_longest(users_list, hobby_list))))
