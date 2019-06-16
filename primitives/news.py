class News:
    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.title = kwargs["title"]
        self.date = kwargs["date"]
        self.body = kwargs["body"]
        self.deleted = kwargs["deleted"]
        self.comments_count = None

    def get_id(self):
        return self.id

    def get_deleted(self):
        return self.deleted

    def get_date(self):
        return self.date

    def set_comments_count(self, count):
        self.comments_count = count

    def __str__(self):
        return 'Id: {},\ntitle: {},\ndate: {},\nbody: {},\ndeleted: {},\ncomments_count: {}' \
            .format(self.id, self.title, self.date, self.body, self.deleted, self.comments_count)
