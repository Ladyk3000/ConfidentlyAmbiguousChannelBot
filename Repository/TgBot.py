import telebot
import os
from dotenv import load_dotenv
load_dotenv()


class TgBot:
    def __init__(self, token=os.getenv('TG_API_TOKEN'), channel=os.getenv('TG_CHANNEL')):
        self.__bot = telebot.TeleBot(token)
        self.__channel = channel

    def send_post(self, post) -> bool:
        try:
            self.__bot.send_message(chat_id=self.__channel, text=post)
            return True
        except:
            return False
