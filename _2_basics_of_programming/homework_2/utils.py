import json


def load_students(filename: any) -> list:
    """
    Загружает список студентов из файла.
    :param filename: Имя загружаемого файла.
    :return: Список студентов.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def load_professions(filename: any) -> list:
    """
    Загружает список профессий из файла.
    :param filename: Имя загружаемого файла.
    :return: Список профессий.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def get_student_by_pk(pk: int, data: list) -> dict:
    """
    Получает словарь с данными студента по его pk.
    :param pk: Номер студента
    :param data: Список студентов
    :return: Словарь студента
    """
    for item in data:
        if pk == item['pk']:
            return item


def get_profession_by_title(title: str, data: list) -> dict:
    """
    Получает словарь с инфо о профессии по названию.
    :param title: Название профессии.
    :param data: Список профессий.
    :return: Словарь профессий.
    """
    for item in data:
        if title == item['title']:
            return item


def check_fitness(student: dict, profession: dict) -> dict:
    """
    Функция возвращающая словарь типа.
    :param student: Словарь студентов.
    :param profession: Словарь профессий.
    :return: Словарь типов
    """

    set_student = set(student['skills'])
    set_profession = set(profession['skills'])

    has_skills = set_student.intersection(set_profession)
    lack_skills = set_profession.difference(set_student)

    fit_percent = round(len(has_skills) / len(set_profession) * 100)

    dict_result = {
        'has': has_skills,
        'lacks': lack_skills,
        'fit_percent': fit_percent
    }

    return dict_result


def show_result(data: dict, name: str) -> str:
    """
    Вывод результата.
    :param data: Словарь типов
    :param name: Имя студента.
    :return: Вывод информации
    """
    str_has = ', '.join(data['has'])
    str_lacks = ', '.join(data['lacks'])

    str_output = f'Пригодность {data["fit_percent"]} \n'\
                 f'{name} знает {str_has} \n'\
                 f'{name} не знает {str_lacks} \n'

    return str_output
