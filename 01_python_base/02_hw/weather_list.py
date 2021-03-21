"""
2.
Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём
до двух разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха',
'была', '"', '+05', '"', 'градусов']
Новый список не создавать! Сформировать из обработанного
списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
3. * (вместо задачи 2) Решить задачу 2 не создавая новый список
(как говорят, in place).
Эта задача намного серьёзнее, чем может сначала показаться.
"""

# вариант 1, я не поняла, зачем переводить в промежуточный список
# ['в', '"', '05', '"', 'часов', '"', # '17', '"', 'минут',
# 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
words_for_sentence = ['в', '5', 'часов', '17', 'минут',
                      'температура', 'воздуха', 'была', '+5', 'градусов']
for idx, word in enumerate(words_for_sentence):
    if word.isdigit():
        words_for_sentence[idx] = '"{}"'.format(word.zfill(2))
    elif word[1:].isdigit():
        words_for_sentence[idx] = '"{}{}"'.format(word[:1], word[1:].zfill(2))
print(' '.join(words_for_sentence))

# вариант 2, c листом с кавычками
words_for_sentence = ['в', '5', 'часов', '17', 'минут',
                      'температура', 'воздуха', 'была', '+5', 'градусов']

words_counter = len(words_for_sentence)

idx = 0
while idx < words_counter:
    word = words_for_sentence[idx]
    if word.isdigit() or word[1:].isdigit():
        if word.isdigit():
            words_for_sentence[idx] = word.zfill(2)
        else:
            words_for_sentence[idx] = '{}{}'.format(word[:1], word[1:].zfill(2))
        words_for_sentence.insert(idx, '"')
        words_for_sentence.insert(idx + 2, '"')
        idx = idx + 3
        words_counter = words_counter + 2
    else:
        idx = idx + 1

sentence = ' '.join(words_for_sentence)

for symbol in '+-0123456789':
    sentence = sentence.replace('" ' + symbol, '"' + symbol)

sentence = sentence.replace(' " ', '" ')
print(sentence)
