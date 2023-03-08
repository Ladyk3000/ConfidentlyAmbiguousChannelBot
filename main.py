import time

from Repository.ThemeScraper import ThemeScraper
from Repository.Prompter import Prompter
from Repository.ChatGPT import ChatGPT
from Repository.TgBot import TgBot
from Repository.Timer import Timer


def main():
    scraper = ThemeScraper()
    prompter = Prompter()
    gpt = ChatGPT()
    bot = TgBot()
    timer = Timer()

    while True:
        if timer.should_post():
            if timer.is_get_theme_time() and scraper.has_not_theme:
                theme = scraper.get_theme()
                query = prompter.generate_query(theme)
                post = gpt.get_post(theme, query)
            if timer.is_post_time():
                bot.send_post(post)
                timer.posted_today += 1
        time.sleep(600)


if __name__ == '__main__':
    main()
