import json
from datetime import datetime
from note import Note


def __init__(self):
    self.notes = []
    self.load_notes()

def add_note(self, title, body):
    note_id = len(self.notes) + 1
    note = Note(note_id, title, body)
    self.notes.append(note)
    self.save_notes()
    print('Заметка успешно сохранена')

def read_notes():
    filter_date = input("Введите дату для фильтрации (в формате ГГГГ-ММ-ДД): ")
    if not notes:
        print("Заметок нет")
        return
    if not filter_date:
        for note in notes:
            print(f"{note['id']}. {note['title']} ({note['date']})\n{note['msg']}\n")
    else:
        filtered_notes = [note for note in notes if note["date"].startswith(filter_date)]
        if filtered_notes:
            for note in filtered_notes:
                print(f"{note['id']}. {note['title']} ({note['date']})\n{note['msg']}\n")
        else:
            print("Заметок с указанной датой нет")

def edit_note():
    note_id = int(input("Введите id заметки для редактирования: "))
    for note in notes:
        if note["id"] == note_id:
            title = input(f"Введите новый заголовок заметки ({note['title']}): ")
            msg = input(f"Введите новое тело заметки ({note['msg']}): ")
            if title:
                note["title"] = title
            if msg:
                note["msg"] = msg
            note["date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes()
            print("Заметка успешно отредактирована")
            return
    print(f"Заметка с id {note_id} не найдена")

def delete_note():
    note_id = int(input("Введите id заметки для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes()
            print("Заметка успешно удалена")
            return
    print(f"Заметка с id {note_id} не найдена")

def save_notes(self):
    data = []
    for note in self.notes:
        note_data = {'note_id': note.note_id, 'title': note.title, 'body': note.body, 'date': note.date}
        data.append(note_data)
    with open("notes.json", "w") as file:
        json.dump(data, file, indent=4)

def load_notes(self):
    try:
        with open("notes.json", "r") as file:
            data = json.load(file)
            for note_data in data:
                note = Note(note_data['note_id'], note_data['title'], note_data['body'], note_data['data'])
                self.notes.append(note)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        self.notes = []
