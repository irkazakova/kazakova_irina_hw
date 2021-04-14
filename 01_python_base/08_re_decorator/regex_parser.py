# 2.
# Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs для
# получения информации вида:
# <remote_addr>,
# <request_datetime>,
# <request_type>,
# <requested_resource>,
# <response_code>,
# <response_size>,
# например:
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-" "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
# Были ли особенные строки? Можно ли для них уточнить регулярное выражение?
import logging
from datetime import datetime
from os import path
import requests
import re

LOG_FILE_URL = "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
LOG_FILE_NAME = "nginx_logs.txt"


def main():
    # Если файл не существует, скачиваем его
    if not path.exists(LOG_FILE_NAME):
        download_log_file()
    # Наверное результат надо сложить в СУБД, но мы их еще не проходили
    parse_log_file()


# Анализ примера строки лога
# Запись значения как есть: 91.77.238.152 - remote_addr, 304 - response_code, 0 - response_size.
# Запись в квадратных скобках: [17/May/2015:08:05:49 +0000] - request_datetime
# Запись в двойных кавычках: "GET /downloads/product_2 HTTP/1.1" - request_type + requested_resource,
# причем в начале там обязательно тип запроса
# Отсутствующее значение: -, "-", может быть в двойных кавычках, а может не быть
# Правила для
# 1 WHITESPACES '\s+' - один и более пробелов
# 2 NO_DATA '-|"-"' - отсутствующее значение, может быть -, а может быть ""
# 3 QUOTED_STRING '"([^"]+)"' - что-то в двойных кавычках
# 4 DATE '\[([^\]]+)\]' - дата
# 5 STR_WITHOUT_WHITESPACES - '([^\s]+)'
# NO_DATA QUOTED_STRING STR_WITHOUT_WHITESPACES конфликтуют, но можно обработать в порядке от самого строго к самому нестрогому

WHITESPACES, QUOTED_STRING, DATE, STR_WITHOUT_WHITESPACES, NO_DATA = range(5)

RULES = [
    ('\s+', WHITESPACES),
    ('-|"-"', NO_DATA),
    ('"([^"]+)"', QUOTED_STRING),
    ('\[([^\]]+)\]', DATE),
    ('([^\s]+)', STR_WITHOUT_WHITESPACES),
]

# Пока не работает.... закоммичу, чтобы не потерялось, можно не смотреть
def parse_log_file():
    prepared = [(re.compile(regexp), token_type) for regexp, token_type in RULES]
    with open(LOG_FILE_NAME, 'r', encoding='utf-8') as f:
        for line in f:
            parsed_raw = []
            # Обработка одной строки
            linelen = len(line)  # длина строки лога - чтобы знать, когда остановиться
            i = 0  # текущая позиция
            while i < linelen:
                for pattern, token_type in prepared:  # пробуем регулярные выражения по очереди
                    match = pattern.match(line, i)  # проверяем соответствует ли регулярное выражение строке с позиции i
                    if match is None:  # если нет - пробуем следующую регулярку
                        continue
                    i = match.end()  # передвигаем позицию анализатора до индекса, соответствующего концу совпадения
                    if token_type == WHITESPACES:
                        continue  # пробелы игнорируем
                    elif token_type == NO_DATA:
                        parsed_raw.extend('Null')
                    elif token_type == STR_WITHOUT_WHITESPACES:
                        parsed_raw.extend(match.group(1))
                    elif token_type == DATE:
                        parsed_raw.extend(match.group(1))
                        print(parsed_raw)
                    elif token_type == QUOTED_STRING:
                        parsed_raw.extend(match.group(1))
                    break  # начинаем анализировать остаток строки с новым значением сдвига i
            print(parsed_raw)

def download_log_file():
    # Скачиваем файл локально кусками, на случай, если он большой
    response = requests.get(LOG_FILE_URL, stream=True)

    with open(LOG_FILE_NAME, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)


if __name__ == '__main__':
    main()
