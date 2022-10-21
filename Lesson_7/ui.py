from os import system
from select import select


# Главное меню приложения
def menu():
    while True:
        system("cls")
        print("                                📔 Приложение - Телефонный справочник 📔")
        print("\n\n                                          Выберите действие:\n")

        print("[1. 📱 Посмотреть справочник]", end="     ")
        print("[2. ➕ Добавить новый контакт]", end="     ")
        print("[3. 👤 Изменить контакт]", end="\n\n   ")
        print("[4. ➖ Удалить контакт]", end="             ")
        print("[5. 🔍 Найти контакт]", end="        ")
        print("[6. 🚪 Выйти из приложения]", end="\n\n")
        select = input("Ввод: ")
        if select == "1":
            return 1
        if select == "2":
            return 2
        if select == "3":
            return 3
        if select == "4":
            return 4
        if select == "5":
            return 5
        if select == "6":
            return 6
        else:
            continue


# Меню выбора критерия поиска
def search_menu():
    while True:
        system("cls")
        print("-"*90 + "\n")
        print("                          🔍 | Поиск в телефонном справочнике\n")
        print("                      Выберите, по какому критерию провести поиск:\n")
        print("-"*90)
        print("[1. 👤 Поиск по имени]", end="     ")
        print("[2. 📱 Поиск по номеру телефона]", end="     ")
        print("[3. 🚪 Вернуться назад]\n\n")
        select = input("Ввод: ")
        if select == "1":
            return 1
        elif select == "2":
            return 2
        elif select == "3":
            return 3
        else:
            continue