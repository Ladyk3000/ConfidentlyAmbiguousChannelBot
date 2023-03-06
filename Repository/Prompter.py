from googletrans import Translator


class Prompter:
    def __init__(self):
        self.__translator = Translator()
        self.__start_q = 'write a very short under 300 symbols essay in an informal style on the topic: '
        self.__end_conv = '.'
        self.__start_p = 'Сегодня я бы хотел поговорить о том, как *'

    def generate_query(self, theme: str) -> str:
        theme_q = self.__translator.translate(text=theme, src='ru', dest='en')
        query = self.__start_q + theme_q.text
        if query[-1] != '.':
            query += self.__end_conv
        return query

    def generate_post_query(self, theme: str) -> str:
        theme_q = self.__translator.translate(text=theme, src='ru', dest='en')
        query = self.__start_q + theme_q.text
        if query[-1] != '.':
            query += self.__end_conv
        return query

    def generate_channel_post(self, theme, english_post):
        post = self.__start_p.replace('*', theme)
        post += self.__translator.translate(text=english_post, src='en', dest='ru').text
        if post[-1] != '.':
            post += self.__end_conv
        return post
