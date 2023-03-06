import time

from Repository.ThemeScraper import ThemeScraper
from Repository.Prompter import Prompter
from Repository.ChatGPT import ChatGPT
from Repository.TgBot import TgBot


def main():
    scraper = ThemeScraper()
    prompter = Prompter()
    gpt = ChatGPT()
    bot = TgBot()
    while True:
        theme = scraper.get_theme()
        query = prompter.generate_query(theme)
        post = gpt.get_post(theme, query)
        bot.send_post(post)
        time.sleep(10)


if __name__ == '__main__':
    main()
