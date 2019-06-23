import os
import datetime

from aiohttp import web

from tools import serializer
from tools.deserializer import deserialize_pool


def _date_in_past(news_date):
    current = datetime.datetime.now().replace(microsecond=0)

    news_date = datetime.datetime.fromisoformat(news_date)

    return current >= news_date


class NewsServer:
    def __init__(self):
        self.news_pool = deserialize_pool()

    def run(self):
        app = web.Application()
        app.add_routes([web.get('/', self._handle_get_all_news),
                        web.get('/news/{id}', self._handle_get_record)])

        web.run_app(app)

    async def _handle_get_all_news(self, _):
        self._update_pool_if_expired()
        response_text = serializer.serialize_news_list(self._get_relevant_news())

        return web.Response(text=response_text, headers={
            'Content-Type': 'application/json'
        })

    async def _handle_get_record(self, request: web.Request):
        self._update_pool_if_expired()
        id_ = str(request.match_info.get('id', None))
        news = self._get_news_by_id(id_)

        if news is None or not _date_in_past(news.date):
            return web.Response(status=404)

        response_text = serializer.serialize_news(self.news_pool.get_news_by_id(int(id_)))

        return web.Response(text=response_text, headers={
            'Content-Type': 'application/json'
        })

    def _get_news_by_id(self, id_: str):
        try:
            if not id_.isnumeric():
                return None

            return self.news_pool.get_news_by_id(int(id_))
        except KeyError:
            return None

    def _update_pool_if_expired(self):
        if os.path.getmtime('news.json') > self.news_pool.load_time or \
                os.path.getmtime('comments.json') > self.news_pool.load_time:
            self.news_pool = deserialize_pool()

    def _get_relevant_news(self):
        return list(sorted(filter(lambda n: not n.deleted and _date_in_past(n.date), self.news_pool),
                           key=lambda n: datetime.datetime.fromisoformat(n.date)))
