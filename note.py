from datetime import datetime

class Note:

    def __init__(self, body, title):  # Инициализация класса с полями (Конструктор Заметки)
        self.date = datetime.now()  # Присваивание текущей даты и времени заметке
        self.note_id = id(self.date)  # Присваивание ID (по дате) заметке
        self.body = body  # Ввод тела заметки
        self.title = title  # Ввод заголовка заметки

    def __init__(self, note_id, title, body, created_time, modified_time):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.created_time = created_time
        self.modified_time = modified_time