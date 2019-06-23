from primitives.comment import Comment


class News:
    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.title = kwargs["title"]
        self.date = kwargs["date"]
        self.body = kwargs["body"]
        self.deleted = kwargs["deleted"]
        self.comments = []

    def add_comment(self, comment: Comment):
        self.comments.append(comment)
