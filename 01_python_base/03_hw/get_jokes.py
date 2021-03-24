"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

Например:
get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
"""

from random import randrange


def get_jokes(number: int):
    """
    function, that returns required number of jokes
    :param number: required number of jokes
    :return: list of jokes
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes_list = []
    for idx in range(number):
        # взять три случайных числа от 1 до 3
        # взять по этим числам слова из трех списков и сформировать строки
        first_word = nouns[randrange(len(nouns))]
        second_word = adverbs[randrange(len(adverbs))]
        third_word = adjectives[randrange(len(adjectives))]
        jokes_list.append('{} {} {}'.format(first_word, second_word, third_word))
    return jokes_list


print(get_jokes(5))
