from typing import List

from primitives.news import News


class NewsPool:
    def __init__(self, news: List[News], load_time):
        self.news = {n.id: n for n in news}
        self.load_time = load_time

    def get_news_by_id(self, id_) -> News:
        if id_ not in self.news:
            raise KeyError(f'No any news with given id {id_}')

        return self.news[id_]

    def __iter__(self):
        return iter(self.news.values())
