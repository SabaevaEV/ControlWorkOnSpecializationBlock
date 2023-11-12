from datetime import datetime

class Note:

    def __init__(self, body, title):
        self.note_id = id(self.date)
        self.body = body
        self.title = title
        self.date = datetime.now()