# объявление переменных
counter = 0
total_questions = 3
processing_result = 0

# приветствие пользователя
print("Привет! Предлагаю проверить свои знания английского!")

# получение имени пользователя
user_name = input("Расскажи, как тебя зовут! \n")

# приветствие с использованием имени
print(f"\nПривет, {user_name}, начинаем тренировку!")

# блок с вопросами и обработкой ответов пользователя
print("My name ___ Vova")
user_answer = input()

if user_answer == "is":
    print("Ответ верный! \nВы получаете 10 баллов!")
    counter += 1
else:
    print("Неправильно. \nПравильный ответ: is")

print("I ___ a coder")
user_answer = input()

if user_answer == "am":
    print("Ответ верный! \nВы получаете 10 баллов!")
    counter += 1
else:
    print("Неправильно. \nПравильный ответ: am")

print("I live ___ Moscow")
user_answer = input()

if user_answer == "in":
    print("Ответ верный! \nВы получаете 10 баллов!")
    counter += 1
else:
    print("Неправильно. \nПравильный ответ: in")

# вычисление баллов
scored = counter * 10

# вычисление процента правильных ответов
correct_answers_percent = round(counter / total_questions * 100)

# список и обработчик правильных окончаний
list_answers = ['вопрос', 'вопроса', 'вопросов']

if counter == 1:
    processing_result = list_answers[0]
elif counter == 2:
    processing_result = list_answers[1]
else:
    processing_result = list_answers[2]

# вывод результата
print(f"\nВот и все, {user_name}! \nВы ответили на {counter} {processing_result} из 3 верно.")
print(f"\nВы заработали {scored} баллов. \nЭто {correct_answers_percent} процентов.")

