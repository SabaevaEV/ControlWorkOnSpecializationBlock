import operations
import view

def main():
    notebook = operations.NoteOperations()
    while True:
        num = view.Menu()
        if num == 1:
            title = input("Введите Заголовок заметки")
            body = input("Введите заметку")
            notebook.add_note(title=title, body=body)
        elif num == 2:
            note_id = int(input('Введите номер заметки'))
            new_title = input('Введите новый заголовок заметки')
            notebook.edit_note_tit(note_id=note_id, new_title=new_title)
        elif num == 3:
            note_id = int(input('Введите номер заметки'))
            new_body = input('Введите новую заметку')
            notebook.edit_note_body(note_id=note_id, new_body=new_body)
        elif num == 4:
            selected_note = view.input_4(notebook.notes)
            if selected_note is not None:
                notebook.view_filter_note(selected_note.note_id, selected_note)
            else:
                print("Заметка не найдена")
        elif num == 5:
            notes = notebook.read_notes_by_date()
            if notes:
                for note in notes:
                    print(note)
        elif num == 6:
            notebook.view_all_notes()
        elif num == 7:
            note_id = int(input('Введите номер заметки'))
            notebook.delete_note(note_id=note_id)
        elif num == 8:
            print('Выход')
            break
        else:
            print('Ошибка, неверная команда')
            # input("Press the key to continue: ")

if __name__ == '__main__':
    main()

