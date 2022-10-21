import contact_editor as c_edit # Файл со всеми возможными изменениями контактов через консоль (добавления, удаление, поиск и изменения записи)
import file_editor as f_edit # Файл с измениями файлов
import contact_format as c_format # Файл с работой контактов внутри программы (кол-во контактов, вывод контактов в консоль)
import ui # Визуальная часть программы
import sync_for_md as s_md # Синхронизация с форматом MarkDown
from os import system


system("cls")
while True:
    select = 0
    c_edit.fix_id() # Сразу фиксим ID, так как пользователь может поломать программу или она будет работать не корректно
    s_md.sunc_md() # Синхронизируем файл на входе в программу
    select = ui.menu()
    # Просмотр в консоли
    if select == 1:
        system("cls")
        c_edit.fix_id() # Фиксим ID на тот случай, если пользователь сначала покапался в файлах а потом решил проверить их в программе
        print("📔 Телефонный справочник:\n")
        c_format.print_contact("print")
        input("\nНажмите \"Enter\", чтобы вернуться в меню...")
    # Добавление нового контакта
    if select == 2:
        c_edit.add_contact()
        s_md.sunc_md() # Синхронизируем изменения в MD
    # Изменить контакт
    if select == 3:
        c_edit.edit_contact()
        s_md.sunc_md() # Синхронизируем изменения в MD
    # Удалить контакт
    if select == 4:
        c_edit.remove_contact()
        s_md.sunc_md() # Синхронизируем изменения в MD
    # Поиск контактов
    if select == 5:
        person = c_format.count_contact()
        if person == 0:
            system("cls")
            input("У вас ещё нет контактов!\nНажмите \"Enter\", чтобы продолжить!")
            continue
        select_sear = ui.search_menu()
        if select_sear == 1:
            c_edit.search_contact("name")
        if select_sear == 2:
            c_edit.search_contact("phone_number")
        else: 
            continue
    if select == 6:
        system("cls")
        print("Программа завершена корректно")
        break