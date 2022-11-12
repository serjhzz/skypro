import random


def file_reading_word(filename: str) -> list:
    """
    Функция прочтения слов из файла.
    :param filename: имя считываемого файла.
    :return: слово из файла.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        word = f.read().splitlines()
    return word


def word_encoding(word: str) -> str:
    """
    Функция кодирования слова.
    :param word: слово взятое из файла для кодирования.
    :return: закодированное слово.
    """
    encode_word = list(word)
    random.shuffle(encode_word)
    mix_letters = ''.join(encode_word)
    return mix_letters


def write_history(filename: str, name_user: str, score_user) -> None:
    """
    Функция записи истории игр.
    :param filename: имя файла для записи.
    :param name_user: имя юзера.
    :param score_user: количество набранных очков.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(f'{name_user} {score_user}\n')


def read_history(filename: str) -> str:
    """
    Функция чтения файла истории игр.
    :param filename: имя файла.
    :return: вывод статистики.
    """
    max_score = 0
    count = 0

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            count += 1
            score = int(line.split(' ')[1])
            if score > max_score:
                max_score = score

    return f'Всего игр сыграно: {count} \nМаксимальный рекорд: {max_score}'
