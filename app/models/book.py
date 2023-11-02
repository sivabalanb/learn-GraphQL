class Book:
    def __init__(self, title, author_id):
        self.id = str(uuid.uuid4())
        self.title = title
        self.author_id = author_id