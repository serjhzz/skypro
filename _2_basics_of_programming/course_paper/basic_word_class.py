class BasicWord:

    def __init__(self, original_word, acceptable_subwords):
        self.original_word = original_word
        self.acceptable_subwords = acceptable_subwords

    def __repr__(self):
        return f"BasicWord(word={self.original_word}, sub_words={self.acceptable_subwords})"

    def checking_word_in_subwords(self, word: str) -> bool:
        """
        Метод проверки введенного пользователем слова в списке допустимых подслов.
        :param word: Слово введенное пользователем.
        :return: Bool
        """
        return word in self.acceptable_subwords

    def counting_subwords(self) -> int:
        """
        Метод подсчета количества подслов.
        :return: Число подслов.
        """
        return len(self.acceptable_subwords)
