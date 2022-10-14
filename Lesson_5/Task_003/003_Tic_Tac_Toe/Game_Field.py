import MyСolor
from os import system

hor_line = "-"

line1 = ["|", " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "|",]
line2 = ["|", " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "|",]                          # Игровое поле
line3 = ["|", " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "|",]

mask1 = ["|", " ", "7", " ", "|", " ", "8", " ", "|", " ", "9", " ", "|",]
mask2 = ["|", " ", "4", " ", "|", " ", "5", " ", "|", " ", "6", " ", "|",]                          # Маска - подсказка
mask3 = ["|", " ", "1", " ", "|", " ", "2", " ", "|", " ", "3", " ", "|",]

def_line = ["|", " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "|",]


def Show_Game_Map(type = "game_map"):

    # Процесс игры (визуализация)
    if type == "game_map":
        MyСolor.SelectColorText("зелёный")
        print(hor_line*len(line1))
        for i in range(len(line1)):
            if line1[i] == "X":
                MyСolor.SelectColorText("желтый")
                MyСolor.SelectStyleText("жирный")
                print(line1[i], end="")
                MyСolor.SelectStyleText("сброс")
                MyСolor.SelectColorText("зелёный")
            elif line1[i] == "O":
                MyСolor.SelectColorText("красный")
                MyСolor.SelectStyleText("жирный")
                print(line1[i], end="")
                MyСolor.SelectStyleText("сброс")
                MyСolor.SelectColorText("зелёный")
            else:
                print(line1[i], end="")
        print("\n"+hor_line*len(line1))
        for j in range(len(line2)):
            if line2[j] == "X":
                MyСolor.SelectColorText("желтый")
                MyСolor.SelectStyleText("жирный")
                print(line2[j], end="")
                MyСolor.SelectStyleText("сброс")
                MyСolor.SelectColorText("зелёный")
            elif line2[j] == "O":
                MyСolor.SelectColorText("красный")
                MyСolor.SelectStyleText("жирный")
                print(line2[j], end="")
                MyСolor.SelectStyleText("сброс")
                MyСolor.SelectColorText("зелёный")
            else:
                print(line2[j], end="")
        print("\n"+hor_line*len(line1))
        for k in range(len(line3)):
            if line3[k] == "X":
                MyСolor.SelectColorText("желтый")
                MyСolor.SelectStyleText("жирный")
                print(line3[k], end="")
                MyСolor.SelectStyleText("сброс")
                MyСolor.SelectColorText("зелёный")
            elif line3[k] == "O":
                MyСolor.SelectColorText("красный")
                MyСolor.SelectStyleText("жирный")
                print(line3[k], end="")
                MyСolor.SelectStyleText("сброс")
                MyСolor.SelectColorText("зелёный")
            else:
                print(line3[k], end="")
        print("\n"+hor_line*len(line1))
        MyСolor.SelectColorText("нет")
    # Помощь - маска
    elif type == "game_step":
        print(hor_line*len(mask1))
        for i in range(len(mask1)):
            if mask1[i].isdigit():
                if line1[i] != "X" and line1[i] != "O":
                    MyСolor.SelectColorText("зелёный")
                    MyСolor.SelectStyleText("жирный")
                    print(mask1[i], end="")
                    MyСolor.SelectStyleText("сброс")
                else:
                    MyСolor.SelectStyleText("пустой")
                    print(mask1[i], end="")
                    MyСolor.SelectStyleText("сброс")
            else:
                print(mask1[i], end="")
        print("\n"+hor_line*len(mask1))

        for j in range(len(mask2)):
            if mask2[j].isdigit():
                if line2[j] != "X" and line2[j] != "O":
                    MyСolor.SelectColorText("зелёный")
                    MyСolor.SelectStyleText("жирный")
                    print(mask2[j], end="")
                    MyСolor.SelectStyleText("сброс")
                else:
                    MyСolor.SelectStyleText("пустой")
                    print(mask2[j], end="")
                    MyСolor.SelectStyleText("сброс")
            else:
                print(mask2[j], end="")
        print("\n"+hor_line*len(mask1))

        for k in range(len(mask3)):
            if mask3[k].isdigit():
                if line3[k] != "X" and line3[k] != "O":
                    MyСolor.SelectColorText("зелёный")
                    MyСolor.SelectStyleText("жирный")
                    print(mask3[k], end="")
                    MyСolor.SelectStyleText("сброс")
                else:
                    MyСolor.SelectStyleText("пустой")
                    print(mask3[k], end="")
                    MyСolor.SelectStyleText("сброс")
            else:
                print(mask3[k], end="")
        print("\n"+hor_line*len(mask1))
        

# Ход
def Step(is_cross):
    cells = {
        1: line3[2],    # 9
        2: line3[6],    # 8
        3: line3[10],   # 7
        4: line2[2],    # 6
        5: line2[6],    # 5
        6: line2[10],   # 4
        7: line1[2],    # 3
        8: line1[6],    # 2
        9: line1[10],   # 1
    }
    if is_cross == True:
        MyСolor.SelectColorText("синий")
        MyСolor.SelectStyleText("жирный")
        print(f"Ход игрока: ", end="")
        MyСolor.SelectColorText("желтый")
        print("X")
    else:
        MyСolor.SelectColorText("синий")
        MyСolor.SelectStyleText("жирный")
        print(f"Ход игрока: ", end="")
        MyСolor.SelectColorText("красный")
        print("O")
    while True:
        try:
            MyСolor.SelectColorText("зелёный")
            MyСolor.SelectStyleText("жирный")
            print("Введите число:", end=" ")
            
            MyСolor.SelectStyleText("сброс")
            MyСolor.SelectColorText("зелёный")
            MyСolor.SelectStyleText("курсив")
            cell = (int(input()))

            if cells[cell] != " ":
                system("cls")
                Show_Game_Map("game_map")
                Show_Game_Map("game_step")
                MyСolor.SelectColorText("красный")
                MyСolor.SelectStyleText("жирный")
                print("Выранная клетка ( ", end="")

                MyСolor.SelectColorText("голубой")
                print(cell, end="")

                MyСolor.SelectColorText("красный")
                MyСolor.SelectStyleText("жирный")
                print(" ) уже занята ( ", end="")

                MyСolor.SelectColorText("пурпурный")
                print(cells[cell], end="")

                MyСolor.SelectColorText("красный")
                print(" )", end="\n")

                MyСolor.SelectStyleText("сброс")
            else: 
                MyСolor.SelectStyleText("сброс")
                break
        except ValueError:
            system("cls")
            Show_Game_Map("game_map")
            Show_Game_Map("game_step")
            MyСolor.SelectStyleText("жирный")
            MyСolor.SelectColorText("красный")
            print("Пожалуйста, введите целое число!\n")
        except KeyError:
            system("cls")
            Show_Game_Map("game_map")
            Show_Game_Map("game_step")
            MyСolor.SelectStyleText("жирный")
            MyСolor.SelectColorText("красный")
            print("Пожалуйста, введите число в диапазоне от 1 до 9!\n")
    if is_cross == True:
        if cell == 1:
            line3[2] = "X"
        if cell == 2:
            line3[6] = "X"
        if cell == 3:
            line3[10] = "X"
        if cell == 4:
            line2[2] = "X"
        if cell == 5:
            line2[6] = "X"
        if cell == 6:
            line2[10] = "X"
        if cell == 7:
            line1[2] = "X"
        if cell == 8:
            line1[6] = "X"
        if cell == 9:
            line1[10] = "X"
    else:
        if cell == 1:
            line3[2] = "O"
        if cell == 2:
            line3[6] = "O"
        if cell == 3:
            line3[10] = "O"
        if cell == 4:
            line2[2] = "O"
        if cell == 5:
            line2[6] = "O"
        if cell == 6:
            line2[10] = "O"
        if cell == 7:
            line1[2] = "O"
        if cell == 8:
            line1[6] = "O"
        if cell == 9:
            line1[10] = "O"