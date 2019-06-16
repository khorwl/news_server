class NewsPool:
    def __init__(self, news):
        self.news = news

    def get_new_by_id(self, id):
        for i in self.news:
            if i.get_id() == id:
                return i
        return "Not such new"

    def iterator(self):
        return self.news.__iter__()


class CommentsPool:
    def __init__(self, comments):
        self.comments = comments

    def get_comments_count_by_news_id(self, id):
        count = 0
        for i in self.comments:
            if i.get_news_id() == id:
                count += 1
        return count
