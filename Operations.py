from datetime import datetime


def add_note():
    title = input("Введите заголовок заметки: ")
    msg = input("Введите тело заметки: ")
    note_id = len(notes) + 1
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes.append({"id": note_id, "title": title, "msg": msg, "date": date})
    save_notes()
    print("Заметка успешно сохранена")

    def add_note(self, title, body):
        note_id = len(self.notes) + 1
        created_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        modified_time = created_time
        note = Note(note_id, title, body, created_time, modified_time)
        self.notes.append(note)
        self.save_notes()
        print('Note added successfully.')