class Player:

    def __init__(self, user_name):
        self.user_name = user_name
        self.used_words = []

    def __repr__(self):
        return f"Player: (user_name: {self.user_name}, used_word: {self.used_words})"

    def get_number_used_words(self) -> int:
        """
        Метод получения количества использованных слов.
        :return: Количество слов.
        """
        return len(self.used_words)

    def adding_word_to_used_words(self, word: str) -> None:
        """
        Метод добавления слова в список использованных слов.
        :param word: Слово введенное пользователем.
        :return: None
        """
        self.used_words.append(word)

    def checking_use_word_before(self, word: str) -> bool:
        """
        Метод проверки использования слова введенного пользователем до этого.
        :param word: Слово введенное пользователем.
        :return: Bool
        """
        return word in self.used_words
