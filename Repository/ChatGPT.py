import openai

from Repository.Prompter import Prompter
import config


class ChatGPT:
    def __init__(self):
        openai.api_key = config.OPENAI_API_KEY
        self.__prompter = Prompter()

    def get_post(self, theme, query):
        eng_post = self.__get_chat_gpt_answer(query)
        post = self.__prompter.generate_channel_post(theme, eng_post)
        return post

    @staticmethod
    def __get_chat_gpt_answer(query):
        openai.api_key = config.OPENAI_API_KEY
        response = openai.Completion.create(
            engine="davinci",
            prompt=query,
            temperature=0.3,
            max_tokens=512,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0)
        return response['choices'][0]['text']
