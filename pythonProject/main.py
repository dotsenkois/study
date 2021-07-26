documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def command_handler():

    print('Введите команду для продолжения рабты:')
    print('h - для отображения подсказки, exit - для выхода из программы')
    command = input("Введите команду...")

    if command == 'p':
        p_command()
    elif command == 's':
        s_command()
    elif command == 'l':
        l_command()
    elif command == 'a':
        a_command()
    elif command == 'h':
        h_command()
    elif command == 'exit':
        e_command()
    elif command == 'd':
        delete()
    elif command == 'm':
        move()
    elif command == 'as':
        add_shelf()
    else:
        print('Unexpected command. \nTry again.')
        command_handler()

def p_command():
    print('***Для выхода из комманды введите "exit"***')
    document_number = input('Введите номер документа для опредениея владельца:...')
    if document_number != 'exit':
        for document in documents:
            if document_number == document["number"]:
                print(f"Документ с номером {document['number']} принадлежит {document['name']}")
                p_command()
                return
        print('Документ с указанным номером не найден.')
        p_command()
    else:
        command_handler()
        return

def s_command():
    print('***Для выхода из комманды введите "exit"***')
    print('Сипосок сущестующих документов:')
    for d in documents:
        print(d)
    document_number = input('Введите номер документа для определения местанахождения документа на полке:')
    if document_number != 'exit':
        for key, directory in directories.items():
            if document_number in directory:
                print(f'Документ с номером {document_number} находится на полке {key}')
                s_command()
                return
        print(f'Документа с номером {document_number} не обнаружено')
        s_command()
    else:
        command_handler()
        return

def l_command():
    for i in documents:
        print(f'{i["type"]}\t"{i["number"]}"\t"{i["name"]}" ')
    command_handler()
    return

def check_directory(document_number):
    directory = input('Введите номер полки для хранения:')
    if directory in directories.keys():
        directories[directory].append(document_number)
        print(f'документ с номером {document_number} добавлен на полку {directory}')
    else:
        print('Такой полки нет! Номера полок: ', end='')
        for i in directories.keys():
            print(f'{i}'.join('. '), end='')
        print()
        check_directory(document_number)

def a_command():
    document_type = input('Введите тип документа:')
    document_number = input('Введите номер документа:')
    document_owner_name = input('Введите имя владельца документа:')
    n_list={"type": document_type, "number": document_number, "name": document_owner_name}
    documents.append(n_list)
    print(f'Документ {documents[-1]["type"]} с номером {documents[-1]["number"]} владельца {documents[-1]["name"]} создан')
    check_directory(document_number)
    want_exit = input('Для продолжения нажмите Enter. Для выхода введите "exit"')
    if want_exit != 'exit':
        a_command()
    else:
        command_handler()
        return

def h_command():
    print('h - help')
    print('p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит')
    print('s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;')
    # Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
    print('l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";')
    print('a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.')
    # Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
    print('d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.')
    print('m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. ')
    print('as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.')
    print('exit for exit')
    command_handler()
    return

def e_command():
    return

def exit_message():
    print('Документ с таким номером не обнаружен. Попробуйте еще раз, либо введите "exit" для выхода из комманды')
    return

def delete():
    print('***Для выхода из комманды введите "exit"***')
    print(f'Список документов и их расположение: {directories}')
    document_number = input('Введите номер документа для для удаления:...')
    if document_number != 'exit':
        for document in documents:
            if document_number == document["number"]:
                if want_delete(document) == "y":
                    for key, directory in directories.items():
                        if document_number in directory:
                            directory.remove(document_number)
                delete()
                return
        delete()
        return
    else:
        command_handler()
        return

def want_delete(document):
    w_delete = input('Вы действительно хотите удалить эдемент{} y/n ?'.format(document))
    if w_delete == "y":
        print('Элемент{} удален'.format(document))
        documents.remove(document)
        return "y"
    elif w_delete == "n":
        print('Операция отменена')
        return 'n'
    else:
        print()
        want_delete(document)

def move():
    print('***Для выхода из комманды введите "exit"***')
    document_number = input('Введите номер документа для пермещения: ')
    if (document_number != 'exit'):
        for document in documents:
            if document_number == document["number"]:
                for key, directory in directories.items():
                    if document_number in directory:
                        new_directory = input('Введите номер полки для хранения:')
                        if new_directory in directories.keys():
                            directory.remove(document_number)
                            directories[new_directory].append(document_number)
                            print((directories))
                            move()
                            return
                        else:
                            print(f'полки с таким номером не обнаружено')
                            move()
                            return
    else:
        command_handler()
        return

def add_shelf():
    print('***Для выхода из комманды введите "exit"***')
    shelf_number = input('введите номер полки для ее создания:...')
    if shelf_number != 'exit':
        if not (shelf_number.isdigit()):
            print("Введитче число!")
            add_shelf()
        else:
            if directories.setdefault(shelf_number,[]) == []:
                print(f'Полка с номером {shelf_number} создана')
                print(directories)
                add_shelf()
            else:
                print(f'Полка с номером {shelf_number} уже существует. Введите другой номер.')
                print(directories)
                add_shelf()
    else:
        command_handler()
        return

def document_is_exist():
    return

def shelf_is_exist():
    return



command_handler()