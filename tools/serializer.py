import json

from primitives.comment import Comment
from primitives.news import News


class NewsListEncoder(json.JSONEncoder):
    def default(self, n):
        return {
            'id': n.id,
            'title': n.title,
            'date': n.date,
            'body': n.body,
            'deleted': n.deleted,
            'comments_count': len(n.comments)
        }


class NewsEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Comment):
            return {
                'id': o.id,
                'news_id': o.news_id,
                'title': o.title,
                'date': o.date,
                'comment': o.comment
            }

        if isinstance(o, News):
            return {
                'id': o.id,
                'title': o.title,
                'date': o.date,
                'body': o.body,
                'deleted': o.deleted,
                'comments': o.comments,
                'comments_count': len(o.comments)
            }

        return o


def serialize_news_list(news):
    return json.dumps({
        'news': news,
        'news_count': len(news)
    }, cls=NewsListEncoder, indent=4)


def serialize_news(news):
    return json.dumps(news, cls=NewsEncoder, indent=4)
