from googletrans import Translator


class Prompter:
    def __init__(self):
        self.__translator = Translator()
        self.__start_q = 'write a short under 1000 symbols essay in an informal style on the topic: '
        self.__end_q = '.'

    def generate_query(self, theme: str) -> str:
        theme_q = self.__translator.translate(text=theme, src='ru', dest='en')
        query = self.__start_q + theme_q.text
        if query[-1] != '.':
            query += self.__end_q
        return query
