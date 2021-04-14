"""
1/2. Написать функцию num_translate_adv(), переводящую числительные от 0 до 10
c английского на русский язык без учета регистра.
Например:
num_translate("one") -> "один"
num_translate("Eight") -> "восемь"
Если перевод сделать невозможно, вернуть None.
Подумайте, как и где лучше хранить информацию, необходимую для перевода:
какой тип данных выбрать, в теле функции или снаружи.
"""


def num_translate_adv(english_word: str):
    """ Function for russian translate number from 1 to 10
    :param english_word: number as english word
    :return: russian translate of word in param
    """

    translate_dict = {
        'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
        'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
        'nine': 'девять', 'ten': 'десять'
    }
    return translate_dict.get(str(english_word).lower())


user_word_e = input("Введите, число по-английски для перевода: ")
user_word_r = num_translate_adv(user_word_e)
print(user_word_r)
