from tools.deserializer import deserialize_news, deserialize_comments

from tools.news_filter import filter_by_relevance


def sort_by_date(relevant_news):
    pass


if __name__ == "__main__":
    news = deserialize_news()
    comments = deserialize_comments()
    relevant_news = filter_by_relevance(news)
    sort_by_date(relevant_news)

    for i in relevant_news:
        count = comments.get_comments_count_by_news_id(i.get_id())
        print(count)
        i.set_comments_count(count)
    for i in relevant_news:
        print(i)
    # print(len(relevant_news))

