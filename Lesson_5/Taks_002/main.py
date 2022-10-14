import candy
import visual
from os import system
import ai

system("cls")
# Цикл игры
while True:
    try:
        system("cls")
        visual.main_menu()
        gamemode = int(input("\n🔘 Выберите режим игры: "))
        # Игроки
        if gamemode == 1:
            candy_bag = candy.set_default_candy()
            candy_p1 = 0
            candy_p2 = 0
            step = 0
            # Игра на 2
            while True:
                # Ход 1 игрока
                visual.game(candy_bag, candy_p1, candy_p2, 1)
                step = candy.take_candy(candy_bag, 1)
                candy_bag -= step
                candy_p1 += step
                if candy_bag == 0:
                    system("cls")
                    print("\"Игрок 1\" выиграл и забирает все конфеты \"Игрок 2\"!")
                    input()
                    break
                system("cls")
                # Ход 2 игрока
                visual.game(candy_bag, candy_p1, candy_p2, 2)
                step = candy.take_candy(candy_bag, 2)
                candy_bag -= step
                candy_p2 += step
                if candy_bag == 0:
                    system("cls")
                    print("\"Игрок 2\" выиграл и забирает все конфеты \"Игрок 1\"!")
                    input()
                    break
                system("cls")
        # Бот        
        elif gamemode == 2:
            candy_bag = candy.set_default_candy()
            candy_p1 = 0
            candy_bot = 0
            step = 0
            # Игра с ботом
            while True:
                # Ход игрока
                visual.game(candy_bag, candy_p1, candy_bot, 3)
                step = candy.take_candy(candy_bag, 3)
                candy_bag -= step
                candy_p1 += step
                if candy_bag == 0:
                    system("cls")
                    print("\"Игрок\" выиграл и забирает все конфеты \"Бота\"!\n")
                    print("\nПОБЕДА ЧЕЛОВЕКА НАД ПРОГРАММОЙ!")
                    input()
                    break
                # Ходит бот
                step = ai.step_bot(candy_bag)
                candy_bag -= step
                candy_bot += step
                if candy_bag == 0:
                    system("cls")
                    print("\"Бот\" выиграл и забирает все конфеты \"Игрока\"!\n")
                    print("\nПОРАЖЕНИЕ! ЭТО ЛИШЬ НАЧАЛО ВОССТАНИЯ МАШИН!")
                    input()
                    break
                system("cls")
        elif gamemode == 3:
            system("cls")
            input("Спасибо за игру!")
            break
        else:
            system("cls")
            print("❗) Используйте цифры от 1 до 3, чтобы выбрать режим игры!", end="\n\n")
    except ValueError:
        system("cls")
        print("❗) Используйте цифры от 1 до 3, чтобы выбрать режим игры!", end="\n\n")