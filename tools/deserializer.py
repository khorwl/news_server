import json

from primitives.comment import Comment
from primitives.news import News
from pools import NewsPool, CommentsPool


def deserialize_news():
    news = deserialize("news.json", "news", "news_count", News)
    return NewsPool(news)


def deserialize_comments():
    comments = deserialize("comments.json", "comments", "comments_count", Comment)
    return CommentsPool(comments)


def deserialize(file_name, elements_name, elements_count_name, elements_class):
    with open(file_name, "r") as read_file:
        data = json.load(read_file)
        count = data[elements_count_name]
        elements = data[elements_name]
        result = []

        for i in range(count):
            result.append(elements_class(**elements[i]))

        return result
