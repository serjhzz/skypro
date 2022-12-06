import random

import requests

from _2_basics_of_programming.course_paper.basic_word_class import BasicWord


def load_random_word():
    """
    Функция получения слов для игры.
    :return: Экземпляр класса BasicWord.
    """
    url = 'https://jsonkeeper.com/b/T5GR'

    req = requests.get(url, verify=False)
    data = req.json()
    random.shuffle(data)

    for item in data:
        words = BasicWord(item['word'], item['subwords'])
        return words
