from datetime import datetime

class Note:

    def __init__(self, note_id, body, title):
        self.date = datetime.now()
        self.note_id = note_id
        self.title = title
        self.body = body
