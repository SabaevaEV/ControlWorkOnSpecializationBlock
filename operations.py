import json
from datetime import datetime
from note import Note

class NoteOperations:
    def __init__(self):
        self.notes = []
        self.load_notes()

    def add_note(self, title, body):
        note_id = len(self.notes) + 1
        create_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        note = Note(note_id, title, body, create_time)
        self.notes.append(note)
        self.save_notes()
        print('Заметка успешно сохранена')

    def read_notes_by_date(self):
        date = input("Введите дату (ГГГГ-ММ-ДД): ")
        filter_notes = []
        for note in self.notes:
            if note.date.split()[0] == date:
                filter_notes.append(note)
        if not filter_notes:
            print("Заметок нет")
        return filter_notes

    def view_filter_note(self, note_id, note):
        print(f"ID: {note.note_id}")
        print(f"Title: {note.title}")
        print(f"Body: {note.body}")
        print(f"Date: {note.date}")

    def view_all_notes(self):
        if self.notes:
            print("Все заметки")
            for note in self.notes:
                print(note)
            input("Нажмите номер для продолжения")
        else:
            print("Заметки не найдены")
    def edit_note_tit(self, note_id, new_title):
        for note in self.notes:
            if note.note_id == note_id:
                note.title = new_title
                note.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                print("Заголовок заметки успешно отредактирована")
                return
        print(f"Заметка с id {note_id} не найдена")

    def edit_note_body(self, note_id, new_body):
        for note in self.notes:
            if note.note_id == note_id:
                note.body = new_body
                note.create_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_notes()
                print("Заметка успешно отредактирована")
                return
        print(f"Заметка с id {note_id} не найдена")

    def delete_note(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                self.notes.remove(note)
                self.save_notes()
                print("Заметка удалена")
                return
        print(f"Заметка с id {note_id} не найдена")

    def save_notes(self):
        data = []
        for note in self.notes:
            note_data = {'note_id': note.note_id, 'title': note.title, 'body': note.body,
                         'create_time': note.create_time}
            data.append(note_data)
        with open("notes.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_notes(self):
        try:
            with open("notes.json", "r") as file:
                data = json.load(file)
                for note_data in data:
                    note = Note(note_data['note_id'], note_data['title'], note_data['body'], note_data['create_time'])
                    self.notes.append(note)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            self.notes = []
