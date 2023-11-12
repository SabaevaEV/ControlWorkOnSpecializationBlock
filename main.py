from Operations import *
from View import View

if __name__ == "__main__":
    notes = load_notes()
    while True:
        View()
        command = View.menu
        if command == "1":
            add_note()
        elif command == "2":
            read_notes()
        elif command == "3":
            edit_note()
        elif command == "4":
            delete_note()
        elif command == "5":
            break
        else:
            print("Неверная команда")
