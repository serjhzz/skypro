# объявление переменных
words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

answers = {}
words = {}
right_answers = 0

# выбор уровня сложности
user_level = input('Выберите уровень сложности (легкий, средний, сложный): ')

if user_level.lower() == 'легкий':
    words = words_easy
elif user_level.lower() == 'средний':
    words = words_medium
elif user_level.lower() == 'сложный':
    words = words_hard
else:
    print('\nНет такого значения, попробуйте снова')
    exit()

print(f'\nВыбран {user_level} уровень сложности, мы предложим 5 слов, подберите перевод')

# цикл вопросов
for key, value in words.items():
    tab_enter = input('\nНажмите Enter.')
    user_response = input(f'{key}, {len(value)}, начинается на {value[0]}...')
    if user_response.lower() == value:
        print(f'\nВерно, {key.title()} — это {value}.')
    else:
        print(f'\nНеверно. {key.title()} — это {value}.')
    answers[key] = user_response.lower() == value

# вывод статистики
print('\nПравильно отвеченные слова: ')
for word, bool_value in answers.items():
    if bool_value is True:
        print(word)
        right_answers += 1

print('\nНеправильно отвеченные слова: ')
for word, bool_value in answers.items():
    if bool_value is False:
        print(word)

# подсчет и вывод ранга
print(f'\nВаш ранг: \n{levels[right_answers]}')
