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

def obrabotchik_kommand():

    print('Введите команду для продолжения рабты:')
    print('p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит')
    print('s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;')
    # Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
    print(
        'l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";')
    print(
        'a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.')
    # Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.

    command = input("Введите команду...")

    if command == 'p':
        p_command()
    elif command == 's':
        s_command()
    elif command == 'l':
        l_command()
    elif command == 'a':
        a_command()
    else:
        print('Unexpected command. \nTry again.')
        obrabotchik_kommand()

def p_command():

def s_command():


def l_command():


def a_command():