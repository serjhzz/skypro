# объявление переменных
counter = 0
processing_result = 0
scored = 0

questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

# приветствие пользователя
answer = input('Привет! Предлагаю проверить свои знания английского! Наберите \'ready\', чтобы начать! \n')

if answer != 'ready':
    print('Кажется, вы не хотите играть. Очень жаль.')
    quit()
else:
    total_questions = range(len(questions))
    for i in total_questions:
        attempts = 3
        while attempts != 0:
            print(questions[i])
            user_input = input()
            if user_input == answers[i]:
                print('Ответ верный!')
                scored += attempts
                counter += 1
                break
            elif user_input != answers[i]:
                attempts -= 1
                if scored != 0:
                    scored -= 1
                if attempts > 0:
                    print(f'Осталось попыток: {attempts}, попробуйте еще раз!')
                else:
                    print(f'Увы, но нет. Верный ответ: {answers[i]}')

# вычисление процента правильных ответов
correct_answers_percent = round(counter / len(questions) * 100)

# вывод результата
print(f"\nВот и все! Вы ответили на {counter} вопросов из {len(questions)} верно.")
print(f"\nВы заработали {scored} баллов. \nЭто {correct_answers_percent} процентов.")
