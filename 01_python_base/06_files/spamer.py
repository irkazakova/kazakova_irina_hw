# 1,2 Найти IP адрес спамера и количество отправленных им запросов
# по данным файла логов из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов;
# код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

# Cловарь счетчиков (используем словарь, чтобы быстрее проверять вхождение определенного IP)
counter_dict = {}

with open("resources/nginx_logs.txt", 'r', encoding='utf-8') as f:
    for line in f:
        ip = line[:line.index(' ')]
        if counter_dict.get(ip) is not None:
            counter_dict[ip] = counter_dict.get(ip)+1
        else:
            counter_dict[ip] = 1

max_counter = max(counter_dict.values())

# Находим ключ ip по максимальному значению счетчика
spamer_ip = list(counter_dict.keys())[list(counter_dict.values()).index(max_counter)]

print('Вот эти ip спамеры: {}, от них поступило {} запросов.'.format(spamer_ip, max_counter))
