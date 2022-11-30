import requests

from question_class import Question


def load_questions() -> list:
    """
    Функция обработки словаря.
    :return: Возвращает список экземпляров класса Question.
    """
    url = 'https://jsonkeeper.com/b/NL8J'

    req = requests.get(url, verify=False)
    data = req.json()
    questions = []
    for item in data:
        text = item['q']
        difficulty = int(item['d'])
        right_answer = item['a']
        question = Question(text, difficulty, right_answer)
        questions.append(question)
    return questions


def build_statistics(questions: list) -> str:
    """
    Функция обработки статистики пользователя.
    :param questions: Список вопросов.
    :return: Возвращает статистику пользователя в виде строки.
    """
    score = 0
    count = 0

    for question in questions:
        if question.is_correct():
            score += question.score
            count = count + 1
    return f'Вот и всё!\n' \
           f'Отвечено {count} вопроса из 5\n' \
           f'Набрано баллов: {score}'
