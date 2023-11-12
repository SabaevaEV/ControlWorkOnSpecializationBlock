import noteBook as noteBook

import view
from operations import *
from view import View

if __name__ == "__main__":
    # notes = load_notes()
    # notebook = noteApp.NoteApp()
    View()
    notebook = noteBook.NoteOperation()
    while True:
        number = view.menu
        if number == "1":
            notebook.add_note()
        elif number == "2":
            notebook.edit_note_tit()
        elif number == "3":
            notebook.edit_note_body()
        elif number == "4":
            delete_note()
        elif number == "5":
            notes = notebook.read_notes_by_date()
            if notes:
                for note in notes:
                    print(note)
        elif number == "6":
            notebook.view_all_notes()
        elif number == "7":
            notebook.delete_note()
        elif number == "8":
            print("Выход")
            break
        else:
            print("Неверная команда")


def main():
    note_app = noteApp.NoteApp()
    while True:
        num = view.user_input()
        if num == 1:
            title, body = view.input_1()
            note_app.add_note(title=title, body=body)
        elif num == 2:
            note_id, new_title = view.input_2()
            note_app.edit_note_title(note_id=note_id, new_title=new_title)
        elif num == 3:
            note_id, new_body = view.input_3()
            note_app.edit_note_body(note_id=note_id, new_body=new_body)
        elif num == 4:
            selected_note = view.input_4(note_app.notes)
            if selected_note is not None:
                note_app.view_selected_note(selected_note.note_id, selected_note)
            else:
                print("Note not found.")
        elif num == 5:
            notes = note_app.select_notes_by_date()
            if notes:
                for note in notes:
                    print(note)
        elif num == 6:
            note_app.view_all_notes()
        elif num == 7:
            note_id = view.input_7()
            note_app.delete_note(note_id=note_id)
        elif num == 8:
            print('Goodbye')
            break
        else:
            print('Error: Invalid number, choice number is menu.')
            input("Press the key to continue: ")

if __name__ == '__main__':
    main()