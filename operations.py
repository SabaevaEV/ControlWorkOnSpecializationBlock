import json
from datetime import datetime



def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    note_id = len(notes) + 1
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes.append({"id": note_id, "title": title, "body": body, "date": date})
    save_notes()
    print("Заметка успешно сохранена")

    # def add_note(self, title, body):
    #     note_id = len(self.notes) + 1
    #     created_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    #     modified_time = created_time
    #     note = Note(note_id, title, body, created_time, modified_time)
    #     self.notes.append(note)
    #     self.save_notes()
    #     print('Note added successfully.')

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

def save_notes():
    with open("notes.json", "w") as f:
        json.dump(notes, f)

def load_notes():
    try:
        with open("notes.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []