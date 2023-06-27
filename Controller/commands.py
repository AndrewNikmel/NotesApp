import Repository.loadFromFile as lF
import Repository.writeToFile as wF
import note as nT


def add_note():
    title = input("Введите заголовок Вашей заметки:\n")
    body = input("Введите описание Вашей заметки:\n")
    note = nT.Note(title=title, body=body)
    array_notes = lF.read_file()
    for i in array_notes:
        if nT.Note.get_id(note) == nT.Note.get_id(i):
            nT.Note.set_id(note)
    array_notes.append(note)
    wF.write_file(array_notes, 'a')
    print("Ваша заметка добавлена в журнал!")


def show(txt):
    array_notes = lF.read_file()

    if array_notes:
        if txt == "все":
            print("ЖУРНАЛ ЗАМЕТОК:")
            for i in array_notes:
                print(nT.Note.map_note(i))

        elif txt == "ID":
            for i in array_notes:
                print("ID: ", nT.Note.get_id(i))
            id = input("\nВведите ID нужной Вам заметки: ")
            flag = True
            for i in array_notes:
                if id == nT.Note.get_id(i):
                    print(nT.Note.map_note(i))
                    flag = False
            if flag:
                print("Данный ID отсутствует")

        elif txt == "дата":
            date = input("Введите дату в формате: дд.мм.гггг: ")
            flag = True
            for i in array_notes:
                date_note = str(nT.Note.get_date(i))
                if date == date_note[:10]:
                    print(nT.Note.map_note(i))
                    flag = False
            if flag:
                print("Такой даты нет")
        else:
            print("Журнал заметок пустой!")


def del_notes():
    id = input("Введите ID удаляемой заметки: ")
    array_notes = lF.read_file()
    flag = False

    for i in array_notes:
        if id == nT.Note.get_id(i):
            array_notes.remove(i)
            flag = True

    if flag:
        wF.write_file(array_notes, 'a')
        print("Заметка с ID: ", id, " успешно удалена")
    else:
        print("Данный ID не обнаружен")


def change_note():
    id = input("Введите ID изменяемой заметки: ")
    array_notes = lF.read_file()
    flag = True
    array_notes_new = []
    for i in array_notes:
        if id == nT.Note.get_id(i):
            i.title = input("измените заголовок:\n")
            i.body = input("измените описание:\n")
            nT.Note.set_date(i)
            logic = False
        array_notes_new.append(i)

    if flag:
        wF.write_file(array_notes_new, 'a')
        print("Заметка с ID: ", id, " успешно изменена!")
    else:
        print("Данный ID не обнаружен")

