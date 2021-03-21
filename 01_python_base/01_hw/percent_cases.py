"""
3.
- Реализовать склонение слова «процент» для чисел до 20.
Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента».
- Вывести все склонения для проверки.
"""

percent = int(input('Пожалуйста, введите число процентов: '))
percent_cases = ['процент','процента','процентов']

# Выводим правильное склонение по введонному значению
if percent == 1:
    print('{} {}'.format(str(percent), percent_cases[0]))
elif 1 < percent < 5:
    print('{} {}'.format(str(percent), percent_cases[1]))
elif 5 <= percent < 20:
    print('{} {}'.format(str(percent), percent_cases[2]))

print('Извините, я умею склонять проценты только те, что ниже: ')

for number in range(20):
    if number == 1:
        print('{} {}'.format(str(number), percent_cases[0]))
    elif 1 < number < 5:
        print('{} {}'.format(str(number), percent_cases[1]))
    elif 1 < number < 20:
        print('{} {}'.format(str(number), percent_cases[2]))