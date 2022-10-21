from typing import List
import file_editor as f_edit

# Получаем кол-во контактов
def count_contact():
    lst = f_edit.file_read()
    n = 0
    for i in lst:
        if i == "\n":
            n += 1
    if n == 0:
        return 0
    else:
        return n
# Это не лучший метод проверки кол-во контактов, так как если она будет с открытым кодом и пользователь
#   поставит дополнительный пропуск или уберёт его при редактировании контактов, программа сломается.
#   Но для решения данной задачи думаю вполне достаточно!


# Формируем список из контактов
def contact_formating():
    lst = f_edit.file_read()
    n = count_contact()

    new_lst = []
    pos = 0
    for i in range(n):
        new_lst.append(f"{lst[pos]}{lst[pos+1]}{lst[pos+2]}{lst[pos+3]}") # Индекс листа на 1 контакт
        pos += 5
    return new_lst


# Выводим список контактов в консоль
def print_contact(method = "return"): # На всякий случай сделал 2 метода вывода
    lst = contact_formating()
    n = count_contact()
    if method == "return":
        temp = []
        for i in range(n):
            temp.append(lst[i])
        return temp

    elif method == "print":
        for i in range(n):
            print(lst[i])