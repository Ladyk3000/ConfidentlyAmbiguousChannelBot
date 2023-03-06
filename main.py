from Repository.ThemeScraper import ThemeScraper
from Repository.Prompter import Prompter
from Repository.ChatGPT import ChatGPT
from Repository.TgBot import TgBot


def main():
    scraper = ThemeScraper()
    prompter = Prompter()
    bot = TgBot()

    theme = scraper.get_theme()
    query = prompter.generate_query(theme)
    post = ChatGPT.get_post(query)
    print(post)
    #result = bot.send_post(post)
    # return result


if __name__ == '__main__':
    main()
