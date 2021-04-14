"""
3/4. Написать функцию thesaurus_adv(), принимающую в качестве аргументов
строки в формате «Имя Фамилия» и возвращающую словарь,
в котором ключи — первые буквы фамилий, а значения — словари,
реализованные по схеме предыдущего задания и содержащие записи,
в которых фамилия начинается с соответствующей буквы. Например:
thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": "Петр Алексеев"
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}
Сможете ли вы вернуть отсортированный по ключам словарь?
"""


def thesaurus_adv(full_names: list[str]):
    """
    Return sorted thesaurus as dict (if you use Python that supported sorted dict)
    :param full_names: list of string "Name Surname"
    :return: dict
    """
    print('Входной список: {}'.format(full_names))

    # Вспомогательный список для сортировки (это было, что попрактиковать просто:))
    full_names_for_sort =\
        map(lambda s: '{}{}{}'.format(s[s.index(' ') + 1:][0],
                                        s[:s.index(' ')][0], s), full_names)
    sorted_full_names_ex = list(full_names_for_sort)
    sorted_full_names_ex.sort()
    sorted_full_names =\
        map(lambda s: s[2:], sorted_full_names_ex)
    full_names_for_dict = list(sorted_full_names)

    # Строим словарь по уже верно отсортированному списку
    result_thesaurus: dict[str, dict: str, list[str]] = {
    }
    for full_name in full_names_for_dict:
        name = full_name[:full_name.index(' ')]
        # Первая буква имени
        name_first_letter = name[:1].upper()
        surname = full_name[full_name.index(' ') + 1:]
        # Первая буква фамилии
        surname_first_letter = surname[:1].upper()
        # Если по первой букве фамилии нет ключа, то добавляем новый словарь из
        # первой буквы имени и лист и полного имени в наш словарь
        if result_thesaurus.get(surname_first_letter) is None:
            name_thesaurus = {name_first_letter: [full_name]}
            result_thesaurus.update({surname_first_letter: name_thesaurus})
        # Если по фамилии ключ есть, то смотрим ключи по имени
        else:
            # Если по имени ключа нет, то добавим новый
            if result_thesaurus.get(surname_first_letter).get(name_first_letter) is None:
                result_thesaurus.get(surname_first_letter).update({name_first_letter: [full_name]})
            # Если есть, изменим внутренний список
            else:
                dict(result_thesaurus.get(surname_first_letter)).\
                    get(name_first_letter).append(full_name)
    print(result_thesaurus)
    return result_thesaurus


full_names_input = ['Ирина Казакова', 'Лёва Винокуров', 'Лёша Винокуров',
                    'Кот Василий Старший', 'Кот Василий Младший', 'Луна Котофеевна', 'И С', 'И К']

thesaurus_adv(full_names_input)
