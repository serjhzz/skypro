import random

from utils import load_questions, build_statistics

if __name__ == '__main__':

    questions = load_questions()

    random.shuffle(questions)

    for question in questions:
        print(question.build_question())
        user_answer = input('Введите ответ: ')
        question.user_answer = user_answer
        print(question.build_feedback())

    print(build_statistics(questions))
