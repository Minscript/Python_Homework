import MyСolor
import Game_Field
from os import system

def Menu_TTT_Visual ():
    MyСolor.SelectColorText("зелёный")
    print(" "*10, end="")
    print("-"*13, end="")
    print(" "*10, end="")
    MyСolor.SelectColorText("желтый")
    print("-"*13, end="")
    print(" "*10, end="")
    MyСolor.SelectColorText("красный")
    print("-"*13)

    MyСolor.SelectColorText("зелёный")
    MyСolor.SelectStyleText("жирный")
    print(" "*10, end="")
    print("| Против ИИ |", end="")
    print(" "*10, end="")
    MyСolor.SelectColorText("желтый")
    print("| Для двоих |", end="")
    print(" "*10, end="")
    MyСolor.SelectColorText("красный")
    print("|   Выход   |")

    MyСolor.SelectColorText("зелёный")
    print(" "*10, end="")
    print("| <-[ 1 ]-> |", end="")
    print(" "*10, end="")
    MyСolor.SelectColorText("желтый")
    print("| <-[ 2 ]-> |", end="")
    print(" "*10, end="")
    MyСolor.SelectColorText("красный")
    print("| <-[ 3 ]-> |")
    MyСolor.SelectStyleText("сброс")

    MyСolor.SelectColorText("зелёный")
    print(" "*10, end="")
    print("-"*13, end="")
    print(" "*10, end="")
    MyСolor.SelectColorText("желтый")
    print("-"*13, end="")
    print(" "*10, end="")
    MyСolor.SelectColorText("красный")
    print("-"*13, end="\n\n\n")


def Menu_TTT_Select():
    system("cls")
    Menu_TTT_Visual ()
    MyСolor.SelectColorText("белый")
    print("Добро пожаловать в игру \"", end="")
    MyСolor.SelectColorText("голубой")
    MyСolor.SelectStyleText("жирный")
    print("Крестики-нолики", end="")
    MyСolor.SelectStyleText("сброс")
    MyСolor.SelectColorText("белый")
    print("\"!")
    print("Выберите режим игры: ", end="")
    while True:
        try:
            MyСolor.SelectColorText("зелёный")
            type_game = int(input())
            if type_game > 0 and type_game <= 3:
                return type_game
            else:
                system("cls")
                Menu_TTT_Visual ()
                MyСolor.SelectColorText("красный")
                print("Пожалуйста, введите целое число от 1 до 3, в зависимости от желаемого режима игры: ", end="")
                continue
        except ValueError:
            system("cls")
            Menu_TTT_Visual ()
            MyСolor.SelectColorText("красный")
            print("Пожалуйста, введите целое число от 1 до 3, в зависимости от желаемого режима игры: ", end="")
            MyСolor.SelectColorText("зелёный")


def InfoForPlayers2():
    system("cls")
    MyСolor.SelectStyleText("жирный")
    print("Режим игры:", end=" ")
    MyСolor.SelectStyleText("сброс")
    MyСolor.SelectColorText("зелёный")
    print("Для двоих", end="\n\n")
    MyСolor.SelectStyleText("сброс")
    print("- Определите, кто будет играть за \"", end=" ")
    MyСolor.SelectStyleText("жирный")
    MyСolor.SelectColorText("желтый")
    print("X", end="")
    MyСolor.SelectStyleText("сброс")
    print(" \", кто за \"", end=" ")
    MyСolor.SelectStyleText("жирный")
    MyСolor.SelectColorText("красный")
    print("O", end="")
    MyСolor.SelectStyleText("сброс")
    print(" \".", end="\n\n")
    print("- Выбирайте куда поставить свой символ вводя цифры от 1 до 9 в консоль.")
    print("Игра подскажет вам если вы ошибётесь или сходите на уже занятую клетку.", end="\n\n")
    Game_Field.Show_Game_Map("game_step")
    print("- Игра адаптированная к NumPad. Ячейки распологаюся в том-же порядке.", end="\n\n")
    print("Когда вы будете готовы, нажмите на клавишу", end=" ")
    MyСolor.SelectStyleText("жирный")
    MyСolor.SelectColorText("зелёный")
    print("Enter", end="")
    MyСolor.SelectStyleText("сброс")
    print(", чтобы начать игру")
    input()
    system("cls")


# def Status_Session(all_games, all_wins, all_lose, all_draw, x_games, x_wins, x_lose, x_draw, o_games, o_wins, o_lose, o_draw, ez_bot_games, \
#     ez_bot_wins, ez_bot_lose, ez_bot_draw, nm_bot_games, nm_bot_wins, nm_bot_lose, nm_bot_draw, hd_bot_games, hd_bot_wins, hd_bot_lose, hd_bot_draw):
