import operations
import view


def main():
    notebook = operations.NoteOperations()
    while True:
        number = view.Menu()
        if number == "1":
            notebook.add_note()
        elif number == "2":
            notebook.edit_note_tit()
        elif number == "3":
            notebook.edit_note_body()
        elif number == "4":
            notebook.view_filter_note()
            # if selected_note is not None:
            #     notebook.view_filter_note(filter_note.note_id, filter_note)
            # else:
            #     print("Заметка не найдена")
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


if __name__ == '__main__':
    main()