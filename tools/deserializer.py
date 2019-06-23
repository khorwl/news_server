import datetime
import json
import time

from pool.news_pool import NewsPool
from primitives.comment import Comment
from primitives.news import News


def _read_file(filename):
    with open(filename, mode='r') as f:
        return f.read()


def deserialize_pool() -> NewsPool:
    news = deserialize_news(_read_file("news.json"))
    comments = deserialize_comments(_read_file("comments.json"))
    pool = NewsPool(news, time.time())

    for comment in comments:
        pool.get_news_by_id(comment.news_id).add_comment(comment)

    for news in pool:
        news.comments = list(sorted(news.comments, key=lambda n: datetime.datetime.fromisoformat(n.date)))

    return pool


def deserialize_news(data):
    news = deserialize(data, "news", "news_count", News)
    return news


def deserialize_comments(data):
    comments = deserialize(data, "comments", "comments_count", Comment)
    return comments


def deserialize(data_to_deserialize, elements_name, elements_count_name, elements_class):
    data = json.loads(data_to_deserialize)
    count = data[elements_count_name]
    elements = data[elements_name]
    result = []

    for i in range(count):
        result.append(elements_class(**elements[i]))

    return result
