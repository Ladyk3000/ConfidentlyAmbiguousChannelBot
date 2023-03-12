import time

from Repository.ThemeScraper import ThemeScraper
from Repository.Prompter import Prompter
from Repository.ChatGPT import ChatGPT
from Repository.TgBot import TgBot
from Repository.Timer import Timer

from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def home():
    return "I'm alive"


def run():
    app.run(host='0.0.0.0', port=80)


def keep_alive():
    t = Thread(target=run)
    t.start()


def main():
    scraper = ThemeScraper()
    prompter = Prompter()
    gpt = ChatGPT()
    bot = TgBot()
    timer = Timer()
    keep_alive()
    while True:
        bot.send_alive()
        if timer.should_post():
            if timer.is_get_theme_time() and scraper.has_not_theme:
                theme = scraper.get_theme()
                bot.send_theme(theme)
                query = prompter.generate_query(theme)
                post = gpt.get_post(theme, query)
            if timer.is_post_time():
                bot.send_post(post)
                timer.posted_today += 1
        time.sleep(600)


if __name__ == '__main__':
    main()
