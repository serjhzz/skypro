# импорт библиотек
import random

# объявление глобальных переменных
words_list = ['buffer', 'digitize', 'kludge', 'wired', 'code', 'bit', 'list', 'soul', 'next', 'root', 'merge']
answers = []
counter = 0

# объявление словаря с азбукой Морзе
morse_code = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}


# основные функции для обработки информации
def morse_encode(words: str, code: dict[str, str]) -> str:
    """
    Функция, которая переводит слова на английском языке в азбуку морзе,
    :param words: слово из списка,
    :param code: предаваемый словарь кодировки,
    :return: закодированная строка
    """
    result_morse = ''
    for i in words:
        result_morse += code[i] + " "

    return result_morse


def get_word(list_words: list[str]) -> str:
    """
    Функция которая получает случайное слово из списка words_list,
    :return: слово из списка words_list
    """
    return random.choice(list_words)


def print_statistics(answers_user: list[bool]) -> None:
    """
    Функция вывода статистики,
    :param answers_user: ответы пользователя,
    :return: статистика
    """
    correct_answers = answers_user.count(True)
    incorrect_answers = answers_user.count(False)

    print(f'Всего задачек: {counter} \nОтвечено верно: {correct_answers} \nОтвечено неверно: {incorrect_answers}')


# приветствие пользователя
hello_user = input('Сегодня мы потренируемся расшифровывать морзянку. \nНажмите Enter и начнем ')

# цикл с вопросами
while counter <= 4:
    random_word = get_word(words_list)
    # print('случайное слово:', random_word)
    print(morse_encode(random_word, morse_code))
    user_answer = (input('Введите расшифровку слова: ')).lower()
    counter += 1

# обработка ответа пользователя
    if user_answer == random_word:
        print('Ответ верный!\n')
        answers.append(True)
    else:
        print(f'Увы, но нет. Верный ответ: {random_word}\n')
        answers.append(False)

# вывод статистики
print_statistics(answers)

exit()
