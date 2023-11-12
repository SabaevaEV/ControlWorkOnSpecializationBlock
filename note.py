from datetime import datetime

class Note:

    def __init__(self, body, title):
        self.date = datetime.now()
        self.note_id = id(self.date)
        self.title = title
        self.body = body
