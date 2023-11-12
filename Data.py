class Note:
    def create (self, note_id, title, body, created_time, modified_time):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.created_time = created_time
        self.modified_time = modified_time