import datetime


def filter_by_relevance(news):
    relevant_news = []
    for i in news.iterator():
        if not i.get_deleted() and date_in_past(i.get_date()):
            relevant_news.append(i)
    return relevant_news


def date_in_past(news_date):
    current = datetime.datetime.now().replace(microsecond=0).isoformat()

    news_date = datetime.datetime.strptime(news_date, "%Y-%m-%dT%H:%M:%S")
    current_date = datetime.datetime.strptime(current, "%Y-%m-%dT%H:%M:%S")

    delta = current_date - news_date
    return delta.days > 0
