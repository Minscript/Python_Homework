import MyСolor
import Game_Field


def IsWin (is_cross):
    is_line1 = Game_Field.line1.copy()
    is_line2 = Game_Field.line2.copy()
    is_line3 = Game_Field.line3.copy()
    is_win = False

    # Победа 8 вариантов (Горизонтально: верхняя, центральная, нижняя; Вертикальная: левая, центральная, правая; Диагональная: слева "\", справа "/")
    # 2, 6, 10
    # Для "X"
    if is_cross == True:
        # Горизонтально
        if is_line1[2] == "X" and is_line1[6] == "X" and is_line1[10] == "X":
            is_win = True
        if is_line2[2] == "X" and is_line2[6] == "X" and is_line2[10] == "X":
            is_win = True
        if is_line3[2] == "X" and is_line3[6] == "X" and is_line3[10] == "X":
            is_win = True
        # Вертикально
        if is_line1[2] == "X" and is_line2[2] == "X" and is_line3[2] == "X":
            is_win = True
        if is_line1[6] == "X" and is_line2[6] == "X" and is_line3[6] == "X":
            is_win = True
        if is_line1[10] == "X" and is_line2[10] == "X" and is_line3[10] == "X":
            is_win = True
        # Диагонально
        if is_line1[2] == "X" and is_line2[6] == "X" and is_line3[10] == "X":
            is_win = True
        if is_line1[10] == "X" and is_line2[6] == "X" and is_line3[2] == "X":
            is_win = True
    # Для "O"
    else:
        if is_line1[2] == "O" and is_line1[6] == "O" and is_line1[10] == "O":
            is_win = True
        if is_line2[2] == "O" and is_line2[6] == "O" and is_line2[10] == "O":
            is_win = True
        if is_line3[2] == "O" and is_line3[6] == "O" and is_line3[10] == "O":
            is_win = True
        # Вертикально
        if is_line1[2] == "O" and is_line2[2] == "O" and is_line3[2] == "O":
            is_win = True
        if is_line1[6] == "O" and is_line2[6] == "O" and is_line3[6] == "O":
            is_win = True
        if is_line1[10] == "O" and is_line2[10] == "O" and is_line3[10] == "O":
            is_win = True
        # Диагонально
        if is_line1[2] == "O" and is_line2[6] == "O" and is_line3[10] == "O":
            is_win = True
        if is_line1[10] == "O" and is_line2[6] == "O" and is_line3[2] == "O":
            is_win = True
    # Кто победил?
    if is_win == True and is_cross == True:
        print(" "*2, end="")
        MyСolor.SelectColorText("зелёный")
        MyСolor.SelectStyleText("жирный")
        print("Победил ", end="")
        MyСolor.SelectColorText("желтый")
        print("X", end="")
        MyСolor.SelectColorText("зелёный")
        print("!")
        MyСolor.SelectStyleText("сброс")
        return True
    elif is_win == True and is_cross == False:
        print(" "*2, end="")
        MyСolor.SelectColorText("зелёный")
        MyСolor.SelectStyleText("жирный")
        print("Победил ", end="")
        MyСolor.SelectColorText("красный")
        print("O", end="")
        MyСolor.SelectColorText("зелёный")
        print("!")
        MyСolor.SelectStyleText("сброс")
        return True
    else:
        return False