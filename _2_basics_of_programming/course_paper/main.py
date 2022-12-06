from _2_basics_of_programming.course_paper.player_class import Player
from _2_basics_of_programming.course_paper.utils import load_random_word

if __name__ == '__main__':

    user_name = input('Ввведите имя игрока: ')
    user = Player(user_name)
    word = load_random_word()

    print(f'Привет, {user_name}!\nСоставьте 8 слов из слова {word.original_word}'
          f'\nСлова должны быть не короче 3 букв'
          f'\nЧтобы закончить игру, угадайте все слова или напишите "stop"'
          f'\nПоехали, ваше первое слово?')

    while user.get_number_used_words() < word.counting_subwords():
        user_answer = input('Введите слово: ').lower()
        word_check = user.checking_use_word_before(user_answer)

        if user_answer in ['stop', 'стоп']:
            break
        else:
            if len(user_answer) < 3:
                print('слишком короткое слово')
            elif user_answer not in word.acceptable_subwords:
                print('неверно')
            elif user_answer in user.used_words:
                print('уже использовано')
            else:
                print('верно')
                user.adding_word_to_used_words(user_answer)
    print(f'Игра завершена, вы угадали {user.get_number_used_words()} слов!')
