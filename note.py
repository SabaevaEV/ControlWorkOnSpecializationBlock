from datetime import datetime

class Note:

    def __init__(self, note_id, body, title, create_time):

        self.note_id = note_id
        self.title = title
        self.body = body
        self.create_time = create_time
