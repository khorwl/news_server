class Comment:
    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.news_id = kwargs["news_id"]
        self.title = kwargs["title"]
        self.date = kwargs["date"]
        self.comment = kwargs["comment"]

    def get_news_id(self):
        return self.news_id
