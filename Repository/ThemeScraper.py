import requests
from bs4 import BeautifulSoup
import random

import config


class ThemeScraper:
    def __init__(self, src_url=config.THEME_SOURCE_URL):
        self.__src_url = src_url
        self.__event_class = 'masonry-item'
        self.__event_end = 'Читать полностью'
        self.__events = []

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
        return random.choice(self.__get_themes())
