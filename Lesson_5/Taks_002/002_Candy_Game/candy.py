from os import system
import random


def set_default_candy():
    system("cls")
    # Выбираем сложность игры (кол-во конфет)
    while True:
        try:
            print("Укажите начальную сумму конфет: ", end="\n\n")

            print("1) К чаю (300) 🍬")
            print("2) На новый год (1000) 🍬🍬")
            print("3) Хеллоуин (2021) 🍬🍬🍬")
            print("4) Сахарное безумие (Кол-во конфет будет рандомным) 🍡")
            print("5) Кастомное кол-во конфет 🍭", end="\n\n")
            
            # Проверяем ввод игрока
            set_candy = int(input("Ввод: "))
            # Сложность: Легко
            if set_candy == 1:
                system("cls")
                return 300
            # Сложность: Средне
            elif set_candy == 2:
                system("cls")
                return 1000
            # Сложность: Тяжело
            elif set_candy == 3:
                system("cls")
                return 2021
            # Сложность: Рандом
            elif set_candy == 4:
                temp_candy = random.randint(300, 2021)
                print(f"\nНа столе теперь {temp_candy} 🍬 конфет.\nНамжите \"Enter\", чтобы продолжить! ", end="")
                input()
                system("cls")
                return temp_candy
            # Сложность: Задаётся игроком
            elif set_candy == 5:
                system("cls")
                while True:
                    try:
                        temp_candy = int(input("Введите нужное вам кол-во конфет на столе: "))
                        # Минимум 30 конфет
                        if temp_candy < 30:
                            system("cls")
                            print("❗) Минимальное кол-во конфет должно быть не ниже 30", end="\n\n")
                            continue
                        else:
                            print(f"\nНа столе теперь {temp_candy} 🍬 конфет.\nНамжите \"Enter\", чтобы продолжить! ", end="")
                            input()
                            system("cls")
                            return temp_candy
        # При ошибочном вводе будем выводить игроку подсказки
                    except ValueError:
                        system("cls")
                        print("❗) Используйте цифры, чтобы указать кол-во конфет", end="\n\n")
            else:
                system("cls")
                print("❗) Выберите из списка, указав цифру от 1 до 5", end="\n\n")
        except ValueError:
            system("cls")
            print("❗) Выберите из списка, указав цифру от 1 до 5", end="\n\n")


def take_candy(candy_bag, step):
    while True:
        try:
            # Проверка ввода
            i_take = int(input("\nВведите кол-во конфет: "))
            if i_take < 1:
                system("cls")
                print("❗) Вы должны взять минимум 1 конфету!", end="\n\n")
                continue
            elif i_take > 28:
                system("cls")
                print("❗) Вы можете взять не более 28 конфет!", end="\n\n")
                continue
            # Есть ли в мешке столько конфет?
            if i_take > candy_bag:
                system("cls")
                print(f"❗) В мешке {candy_bag} конфет!\nВозьмите все конфеты или меньше!", end="\n\n")
                continue
            # Если всё хорошо
            return + i_take
        except ValueError:
            system("cls")
            print("❗) Укажите кол-во конфет от 1 до 28!", end="\n\n")