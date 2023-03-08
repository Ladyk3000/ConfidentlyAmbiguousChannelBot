import datetime
from random import randrange


class Timer:
    def __init__(self,
                 theme_time='7:00',
                 start_post_time='11:00',
                 end_post_time='14:00',
                 max_post_count=1):

        self.__theme_time = self.__transform_time(theme_time)
        self.__post_time = self.__get_post_time(start_post_time, end_post_time)
        self.posted_today = 0
        self.__day_post_count = max_post_count

    def __get_post_time(self, start_time, end_time):
        start = self.__transform_time(start_time)
        end = self.__transform_time(end_time)
        delta = end - start
        random_second = randrange(delta.seconds)
        return start + datetime.timedelta(seconds=random_second)

    @staticmethod
    def __transform_time(str_time: str):
        time_obj = datetime.datetime.strptime(str_time, '%H:%M')
        time_to_eq = datetime.datetime(datetime.datetime.today().year,
                                       datetime.datetime.today().month,
                                       datetime.datetime.today().day,
                                       time_obj.hour,
                                       time_obj.minute, 0)
        return time_to_eq

    @staticmethod
    def __is_greater_than_now(eq_time: datetime) -> bool:
        if datetime.datetime.now() > eq_time:
            return True
        return False

    def is_get_theme_time(self):
        if self.__is_greater_than_now(self.__theme_time):
            return True
        return False

    def is_post_time(self):
        if self.__is_greater_than_now(self.__post_time) and self.posted_today < self.__day_post_count:
            return True
        return False

    def should_post(self):
        self.__get_posted_today()
        if self.posted_today < self.__day_post_count:
            return True
        return False

    def __get_posted_today(self):
        if self.posted_today > 0 and self.__is_greater_than_now(self.__theme_time) == False:
            self.posted_today = 0
