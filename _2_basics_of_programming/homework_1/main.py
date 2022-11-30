from utils import file_reading_word, word_encoding, write_history, read_history

point = 10
score = 0
word_txt = 'words.txt'
history_txt = 'history.txt'

if __name__ == '__main__':
    user_name = input('Введите ваше имя: ')
    words = file_reading_word(word_txt)

    for word in words:
        new_word = word_encoding(word)
        user_answer = input(f'Угадайте слово: {new_word}')

        if user_answer.lower().strip(' ') == word:
            print(f'Верно! Вы получаете {point} очков.')
            score += 10
        else:
            print(f'Неверно! Верный ответ – {word}.')

    write_history(history_txt, user_name, score)
    print(read_history(history_txt))
