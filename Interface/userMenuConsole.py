import Interface.menuTemplates as m


def menu_console():
        m.printNenuTitle("Главное меню\n           ЖУРНАЛ ЗАМЕТОК")
        print("1 - вывести журнал \n2 - вывести заметку по id \n3 - выбрать заметку по дате\n4 - редактировать заметку"
              " \n5 - добавить заметку\n6 - удалить заметку\n7 - выйти")
        m.printMenuLine()
        print("\n введите пункт из меню ")
