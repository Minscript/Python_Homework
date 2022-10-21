import contact_format as c_form
import file_editor as f_edit
from os import system

# Добавить новый контакт (на стороне терминала)
def write_contact():
    id = c_form.count_contact() + 1 # Простое решение добавлять ID по кол-ву контактов - не лучшее решение, но более оптимизированное, т.к. не придётся писать систему выдачи ID.
    # Имя
    system("cls")
    print("➕ | Добавление нового контакта\n")
    name = input("Введите имя контакта: ")
    if name == "":
        name = "Без имени"
    # Номер
    system("cls")
    while True:
        try:
            print(f"➕ | Добавление нового контакта: {name}\n")
            phone_number = int(input("Введите номер телефона: ")) # Так как номера бывают разные по длинне, регионам, типам и пр, я не буду делать провеку записи на длинну.
            break
        except:
            system("cls")
            print(f"➕ | Добавление нового контакта: {name}\n")
            print("Номер телефона должен состоять из цифр!")
    # Описание
    system("cls")
    print(f"➕ | Добавление нового контакта: {name} | +{phone_number}\n")
    disc = input("Введите описание: ")
    text = (f"ID: {id}\nИмя: {name}\nТелефон: +{phone_number}\nОписание: {disc}\n")
    return text


# Добавить новый контакт (изменяя файл)
def add_contact():
    text = write_contact()
    f_edit.file_add(text)
    system("cls")
    input("Контакт успешно добавлен.\nНажмите \"Enter\", чтобы продолжить!")


# Обновления ID после изменений
def fix_id():
    person = c_form.count_contact()
    if person == 0:
        return
    lst = f_edit.file_read()
    point = 2
    lst[0] = "ID: 1\n" # Насильно заменяем первый ID на 1 для дальнейшей работы
    for i in range(5, len(lst)):
        if i % 5 == 0: # Каждый 5 элемент обозначает ID. Мы заменяем его на указаннай номер
            lst[i] = (f"ID: {point}\n")
            point += 1
    # Изменяем сам документ
    lst.pop(-1) # Программа почему-то в конце добавляет "\n". Исправим это недоразумение
    new_lst = "".join(lst)
    f_edit.file_write(new_lst)


# Удаление контактов
def remove_contact():
    max_id = c_form.count_contact()
    if max_id == 0:
        system("cls")
        input("У вас ещё нет контактов!\nНажмите \"Enter\", чтобы продолжить!")
        return
    system("cls")
    print(f"➖ | Удаление контакта:\n")
    while True:
        try:
            id = int(input("Введите ID контакта: "))
            if id < 1 or id > max_id:
                system("cls")
                print(f"➖ | Удаление контакта:\n")
                print(f"Укажите ID контакта от 1 до {max_id}!")
                continue
            break
        except:
            system("cls")
            print(f"➖ | Удаление контакта:\n")
            print("ID контакта должен состоять из цифр!")
    # Ищем данный контакт в списке...
    lst = c_form.print_contact("return") # Получаем весь список контактов
    system("cls")
    print(f"➖ | Удаление контакта:\n")
    print(f"Вы хотите удалить этот контакт:\n\n {lst[id-1]}\n\n")
    while True:
        confirmation = input("Вы уверенны что хотите удалить данный контакт?\nВведите \"Да\" или \"Нет\": ").lower() # Делаем не чувствительный регистр на ответ
        if confirmation == "да":
            lst.pop(id-1)
            new_lst = "\n".join(lst)
            f_edit.file_write(new_lst)
            fix_id() # Сразу фиксим ID после удаления контакта
            system("cls")
            input("Контакт успешно удалён.\nНажмите \"Enter\", чтобы продолжить!")
            break
        elif confirmation == "нет":
            system("cls")
            return
        else:
            system("cls")
            print(f"➖ | Удаление контакта:\n")
            print(f"Вы хотите удалить этот контакт:\n\n {lst[id-1]}\n\n")
            continue


# Изменение контакта:
def edit_contact():
    max_id = c_form.count_contact()
    if max_id == 0:
        system("cls")
        input("У вас ещё нет контактов!\nНажмите \"Enter\", чтобы продолжить!")
        return
    system("cls")
    print(f"👤 | Изменить контакт:\n")
    while True:
        try:
            id = int(input("Введите ID контакта: "))
            if id < 1 or id > max_id:
                system("cls")
                print(f"👤 | Изменить контакт:\n")
                print(f"Укажите ID контакта от 1 до {max_id}!")
                continue
            break
        except:
            system("cls")
            print(f"👤 | Изменить контакт:\n")
            print("ID контакта должен состоять из цифр!")
    # Ищем данный контакт в списке...
    lst = c_form.print_contact("return") # Получаем весь список контактов
    system("cls")
    print(f"👤 | Изменить контакт:\n")
    print(f"Вы хотите изменить этот контакт:\n\n {lst[id-1]}\n\n")
    while True:
        confirmation = input("Вы уверенны что хотите изменить данный контакт?\nВведите \"Да\" или \"Нет\": ").lower() # Делаем не чувствительный регистр на ответ
        if confirmation == "да":
            system("cls")
            print("👤 | Изменить контакт:\n")
            # Имя
            name = input("Введите новое имя контакта: ")
            if name == "":
                name = "Без имени"
            # Номер
            system("cls")
            while True:
                try:
                    print(f"👤 | Изменить контакт: {name}\n")
                    phone_number = int(input("Введите новый номер телефона: ")) # Так как номера бывают разные по длинне, регионам, типам и пр, я не буду делать провеку записи на длинну.
                    break
                except:
                    system("cls")
                    print(f"👤 | Изменить контакт: {name}\n")
                    print("Номер телефона должен состоять из цифр!")
            # Описание
            system("cls")
            print(f"👤 | Изменить контакт: {name} | +{phone_number}\n")
            disc = input("Введите описание: ")
            text = (f"ID: {id-1}\nИмя: {name}\nТелефон: +{phone_number}\nОписание: {disc}\n")
            # Добавляем новый контакт в список
            lst[id-1] = text
            new_lst = "\n".join(lst)
            f_edit.file_write(new_lst)
            fix_id() # Сразу фиксим ID, на всякий (хотя как по мне это лишнее, мы и так указали ID)
            system("cls")
            input("Контакт успешно изменён.\nНажмите \"Enter\", чтобы продолжить!")
            return
        elif confirmation == "нет":
            system("cls")
            return
        else:
            system("cls")
            print(f"👤 | Изменить контакт:\n")
            print(f"Вы хотите изменить этот контакт:\n\n {lst[id-1]}\n\n")
            continue


# Поиск контактов
def search_contact(category = "name"):
    lst = f_edit.file_read() # Получаем весь список контактов
    if category == "name":
        while True:
            system("cls")
            print("Поиск контактов по имени\n")
            print("Чтобы выйти, введите \"1\"")
            sear = input("Введите имя: ").lower()
            if sear == "1":
                return
            else:
                # Сейчас будет всё намудрёно. Сначала мы ищем кол-во совпадений, потом показываем их
                coincidence = 0
                for i in range(len(lst)):
                    if lst[i].lower() == (f"имя: {sear}\n"):
                        coincidence += 1
                    system("cls")
                # Если совпадений нет - вернёмся к поиску
                if coincidence == 0:
                    input("Совпадений не найдено!\nНажмите \"Enter\" чтобы продолжить...")
                    continue
                # Если совпадения были - покажем их
                else:
                    temp_coincidence = 0
                    for i in range(len(lst)):
                        system("cls")
                        if lst[i].lower() == (f"имя: {sear}\n"):
                            temp_coincidence += 1
                            print(f"Совпадение {temp_coincidence}/{coincidence}:\n")
                            print(f"{lst[i-1]}{lst[i]}{lst[i+1]}{lst[i+2]}\n")
                            if temp_coincidence != coincidence:
                                next = input("Нажмите \"Enter\", чтобы посмотреть следующее совпадение, или введите \"1\" чтобы вернуться в меню: ")
                                if next == "1":
                                    return
                            else:
                                input("Нажмите \"Enter\", чтобы вернуться в меню...")
                                return
    # Поиск по номеру телефона
    elif category == "phone_number":
        while True:
            system("cls")
            print("Поиск контактов по номеру телефона\n")
            print("Чтобы выйти, введите \"1\"")
            sear = input("Введите номер телефона без \"+\": ")
            if sear == "1":
                return
            else:
                # Сейчас будет всё намудрёно. Сначала мы ищем кол-во совпадений, потом показываем их
                coincidence = 0
                for i in range(len(lst)):
                    if lst[i].lower() == (f"телефон: +{sear}\n"):
                        coincidence += 1
                    system("cls")
                # Если совпадений нет - вернёмся к поиску
                if coincidence == 0:
                    input("Совпадений не найдено!\nНажмите \"Enter\" чтобы продолжить...")
                    continue
                # Если совпадения были - покажем их
                else:
                    temp_coincidence = 0
                    for i in range(len(lst)):
                        system("cls")
                        if lst[i].lower() == (f"телефон: +{sear}\n"):
                            temp_coincidence += 1
                            print(f"Совпадение {temp_coincidence}/{coincidence}:\n")
                            print(f"{lst[i-2]}{lst[i-1]}{lst[i]}{lst[i+1]}\n")
                            if temp_coincidence != coincidence:
                                next = input("Нажмите \"Enter\", чтобы посмотреть следующее совпадение, или введите \"1\" чтобы вернуться в меню: ")
                                if next == "1":
                                    return
                            else:
                                input("Нажмите \"Enter\", чтобы вернуться в меню...")
                                return