class Question:

    def __init__(self, text, difficulty, right_answer):
        self.text = text
        self.difficulty = difficulty
        self.right_answer = right_answer
        self.is_asked = False
        self.user_answer = None
        self.score = self.difficulty * 10

    def get_points(self) -> int:
        """
        Метод получения баллов.
        :return: Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return self.score

    def is_correct(self) -> bool:
        """
        Метод проверки правильности ответа.
        :return: Возвращает True, если ответ пользователя совпадает с верным ответом иначе False.
        """
        return self.user_answer == self.right_answer

    def build_question(self) -> str:
        """
        Метод построения формы вопроса.
        :return: Возвращает строку с вопросом и сложностью.
        """
        return f'Вопрос: {self.text} \n' \
               f'Сложность: {self.difficulty}/5'

    def build_feedback(self) -> str:
        """
        Метод обработки ответа пользователя.
        :return: Возвращает строку с ответом для пользователя
        """
        if self.is_correct():
            return f'Ответ верный, получено {self.score} баллов'
        return f'Ответ неверный, верный ответ {self.right_answer}'
