import requests
from bs4 import BeautifulSoup
import random


class ThemeScraper:
    def __init__(self, src_url='https://www.denvistorii.ru/'):
        self.__src_url = src_url
        self.__event_class = 'masonry-item'
        self.__event_end = 'Читать полностью'
        self.__events = []
        self.__theme = None
        self.has_not_theme = True

    def __get_events(self) -> None:
        try:
            html = requests.get(self.__src_url).text
            soup = BeautifulSoup(html, 'lxml')
            self.__events = soup.find_all("div", {"class": self.__event_class})
        except Exception as e:
            print(f'smth wrong {e.message, e.args}')

    def __get_themes(self) -> list:
        themes = []
        if len(self.__events) == 0:
            self.__get_events()
        for event in self.__events:
            theme = event.text.rstrip().replace("\n", "").split(self.__event_end)[0]
            themes.append(theme)
        return themes

    def get_theme(self):
        self.has_not_theme = False
        self.__theme = random.choice(self.__get_themes())
        return self.__theme
