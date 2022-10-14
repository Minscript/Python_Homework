import random
from select import select
import MyСolor
import Game_Field
from os import system


def Bot_Can_Win(types):
    is_line1 = Game_Field.line1.copy()
    is_line2 = Game_Field.line2.copy()
    is_line3 = Game_Field.line3.copy()
    next_step = None
    # Вариантов для победы: 24 (Горизонтально 9, Вертикально 9, Диагонально 6)
    # Горизонтально
    if is_line1[2] == types and is_line1[6] == types and is_line1[10] == " ":
        next_step = 9
    if is_line1[2] == " " and is_line1[6] == types and is_line1[10] == types:
        next_step = 7
    if is_line1[2] == types and is_line1[6] == " " and is_line1[10] == types:
        next_step = 8
    if is_line2[2] == types and is_line2[6] == types and is_line2[10] == " ":
        next_step = 6
    if is_line2[2] == " " and is_line2[6] == types and is_line2[10] == types:
        next_step = 4
    if is_line2[2] == types and is_line2[6] == " " and is_line2[10] == types:
        next_step = 5
    if is_line3[2] == types and is_line3[6] == types and is_line3[10] == " ":
        next_step = 3
    if is_line3[2] == " " and is_line3[6] == types and is_line3[10] == types:
        next_step = 1
    if is_line3[2] == types and is_line3[6] == " " and is_line3[10] == types:
        next_step = 2
    # Вертикально
    if is_line1[2] == types and is_line2[2] == types and is_line3[2] == " ":
            next_step = 1
    if is_line1[2] == " " and is_line2[2] == types and is_line3[2] == types:
            next_step = 7
    if is_line1[2] == types and is_line2[2] == " " and is_line3[2] == types:
            next_step = 4
    if is_line1[6] == types and is_line2[6] == types and is_line3[6] == " ":
            next_step = 2
    if is_line1[6] == " " and is_line2[6] == types and is_line3[6] == types:
            next_step = 8
    if is_line1[6] == types and is_line2[6] == " " and is_line3[6] == types:
            next_step = 5
    if is_line1[10] == types and is_line2[10] == types and is_line3[10] == " ":
            next_step = 3
    if is_line1[10] == " " and is_line2[10] == types and is_line3[10] == types:
            next_step = 9
    if is_line1[10] == types and is_line2[10] == " " and is_line3[10] == types:
            next_step = 6
    # Диагонально
    if is_line1[2] == " " and is_line2[6] == types and is_line3[10] == types:
            next_step = 7
    if is_line1[2] == types and is_line2[6] == " " and is_line3[10] == types:
            next_step = 5
    if is_line1[2] == types and is_line2[6] == types and is_line3[10] == " ":
            next_step = 3
    if is_line1[10] == " " and is_line2[6] == types and is_line3[2] == types:
            next_step = 9
    if is_line1[10] == types and is_line2[6] == " " and is_line3[2] == types:
            next_step = 5
    if is_line1[10] == types and is_line2[6] == types and is_line3[2] == " ":
            next_step = 1
    if next_step != None:
        return next_step
    else:
        return None


def Bot_Danger_Mod(types_bot):
    is_line1 = Game_Field.line1.copy()
    is_line2 = Game_Field.line2.copy()
    is_line3 = Game_Field.line3.copy()
    next_step = None
    if types_bot == "X":
        types = "O"
    else:
        types = "X"
    # Вариантов для поражения: 24 (Горизонтально 9, Вертикально 9, Диагонально 6)
    # Горизонтально
    if is_line1[2] == types and is_line1[6] == types and is_line1[10] == " ":
        next_step = 9
    if is_line1[2] == " " and is_line1[6] == types and is_line1[10] == types:
        next_step = 7
    if is_line1[2] == types and is_line1[6] == " " and is_line1[10] == types:
        next_step = 8
    if is_line2[2] == types and is_line2[6] == types and is_line2[10] == " ":
        next_step = 6
    if is_line2[2] == " " and is_line2[6] == types and is_line2[10] == types:
        next_step = 4
    if is_line2[2] == types and is_line2[6] == " " and is_line2[10] == types:
        next_step = 5
    if is_line3[2] == types and is_line3[6] == types and is_line3[10] == " ":
        next_step = 3
    if is_line3[2] == " " and is_line3[6] == types and is_line3[10] == types:
        next_step = 1
    if is_line3[2] == types and is_line3[6] == " " and is_line3[10] == types:
        next_step = 2
    # Вертикально
    if is_line1[2] == types and is_line2[2] == types and is_line3[2] == " ":
            next_step = 1
    if is_line1[2] == " " and is_line2[2] == types and is_line3[2] == types:
            next_step = 7
    if is_line1[2] == types and is_line2[2] == " " and is_line3[2] == types:
            next_step = 4
    if is_line1[6] == types and is_line2[6] == types and is_line3[6] == " ":
            next_step = 2
    if is_line1[6] == " " and is_line2[6] == types and is_line3[6] == types:
            next_step = 8
    if is_line1[6] == types and is_line2[6] == " " and is_line3[6] == types:
            next_step = 5
    if is_line1[10] == types and is_line2[10] == types and is_line3[10] == " ":
            next_step = 3
    if is_line1[10] == " " and is_line2[10] == types and is_line3[10] == types:
            next_step = 9
    if is_line1[10] == types and is_line2[10] == " " and is_line3[10] == types:
            next_step = 6
    # Диагонально
    if is_line1[2] == " " and is_line2[6] == types and is_line3[10] == types:
            next_step = 7
    if is_line1[2] == types and is_line2[6] == " " and is_line3[10] == types:
            next_step = 5
    if is_line1[2] == types and is_line2[6] == types and is_line3[10] == " ":
            next_step = 3
    if is_line1[10] == " " and is_line2[6] == types and is_line3[2] == types:
            next_step = 9
    if is_line1[10] == types and is_line2[6] == " " and is_line3[2] == types:
            next_step = 5
    if is_line1[10] == types and is_line2[6] == types and is_line3[2] == " ":
            next_step = 1
    if next_step != None:
        return next_step
    else: 
        return None


def Bot_Step(types, know = None):
    is_line1 = Game_Field.line1.copy()
    is_line2 = Game_Field.line2.copy()
    is_line3 = Game_Field.line3.copy()
    step = 5
    steps = {
        1: is_line3[2],    # 9
        2: is_line3[6],    # 8
        3: is_line3[10],   # 7
        4: is_line2[2],    # 6
        5: is_line2[6],    # 5
        6: is_line2[10],   # 4
        7: is_line1[2],    # 3
        8: is_line1[6],    # 2
        9: is_line1[10],   # 1
    }
    if know != None:
        step = know
        if step == 1:
            Game_Field.line3[2] = types
        if step == 2:
            Game_Field.line3[6] = types
        if step == 3:
            Game_Field.line3[10] = types
        if step == 4:
            Game_Field.line2[2] = types
        if step == 5:
            Game_Field.line2[6] = types
        if step == 6:
            Game_Field.line2[10] = types
        if step == 7:
            Game_Field.line1[2] = types
        if step == 8:
            Game_Field.line1[6] = types
        if step == 9:
            Game_Field.line1[10] = types
    else:
        while steps[step] != " ":
            step = random.randint(1, 9)    
        if step == 1:
            Game_Field.line3[2] = types
        if step == 2:
            Game_Field.line3[6] = types
        if step == 3:
            Game_Field.line3[10] = types
        if step == 4:
            Game_Field.line2[2] = types
        if step == 5:
            Game_Field.line2[6] = types
        if step == 6:
            Game_Field.line2[10] = types
        if step == 7:
            Game_Field.line1[2] = types
        if step == 8:
            Game_Field.line1[6] = types
        if step == 9:
            Game_Field.line1[10] = types


def Bot_Think(difficulty, types):
    if (difficulty == "easy"):
        Bot_Step(types)
    elif (difficulty == "normal"):
        is_danger = Bot_Danger_Mod(types)
        is_win = Bot_Can_Win(types)
        if is_danger != None:
            Bot_Step(types, is_danger)
        elif is_win != None:
            Bot_Step(types, is_win)
        else:
            Bot_Step(types)
    elif (difficulty == "hard"):
        is_danger = Bot_Danger_Mod(types)
        is_win = Bot_Can_Win(types)
        if is_win != None:
            Bot_Step(types, is_win)
        elif is_danger != None:
            Bot_Step(types, is_danger)
        else:
            Bot_Step(types)


def Difficulty_Bot():
    system("cls")
    while True:
        try:
            MyСolor.SelectStyleText("сброс")
            MyСolor.SelectStyleText("жирный")
            print("Сложность игры", end="\n\n")
            print("1) ", end=" ")
            MyСolor.SelectColorText("зелёный")
            print("Легкий", end=" ")
            MyСolor.SelectStyleText("сброс")
            print("- его очень легко победить, фактически не имеет интеллекта.")
            MyСolor.SelectStyleText("жирный")
            print("2) ", end=" ")
            MyСolor.SelectColorText("желтый")
            print("Средний", end=" ")
            MyСolor.SelectStyleText("сброс")
            print("- имеет простой интеллект и инстинкт самосохранения.")
            MyСolor.SelectStyleText("жирный")
            print("3) ", end=" ")
            MyСolor.SelectColorText("красный")
            print("Сложный", end=" ")
            MyСolor.SelectStyleText("сброс")
            print("- будет стараться выиграть из-за всех сил. Это рекомендуемая сложность!", end="\n"*3)
            MyСolor.SelectStyleText("жирный")
            print("Выберите уровень сложности: ", end="")
            MyСolor.SelectStyleText("сброс")
            MyСolor.SelectColorText("синий")
            diffic = int(input())
            MyСolor.SelectStyleText("сброс")
            if diffic == 1:
                return "easy"
            elif diffic == 2:
                return "normal"
            elif diffic == 3:
                return "hard"
            else:
                system("cls")
                MyСolor.SelectStyleText("жирный")
                MyСolor.SelectColorText("красный")
                print("Укажите число от 1 до 3 для выбора сложности бота!", end="\n\n")
                continue
        except ValueError:
            system("cls")
            MyСolor.SelectStyleText("жирный")
            MyСolor.SelectColorText("красный")
            print("Укажите число от 1 до 3 для выбора сложности бота!", end="\n\n")


def Bot_Types():
    system("cls")
    while True:
        try:
            MyСolor.SelectStyleText("жирный")
            MyСolor.SelectColorText("белый")
            print("Укажите, кто будет играть за", end=" ")
            MyСolor.SelectColorText("желтый")
            print("X", end="")
            MyСolor.SelectStyleText("сброс")
            MyСolor.SelectStyleText("жирный")
            print("?", end="\n\n")
            MyСolor.SelectStyleText("сброс")
            print("1) Бот\n2) Я (игрок)", end="\n\n")
            MyСolor.SelectStyleText("жирный")
            MyСolor.SelectColorText("зелёный")
            print("Ваш выбор:", end=" ")
            MyСolor.SelectStyleText("сброс")
            select = int(input())
            if select == 1:
                return "X"
            elif select == 2:
                return "O"
            else:
                system("cls")
                MyСolor.SelectStyleText("жирный")
                MyСolor.SelectColorText("красный")
                print("Укажите число 1 или 2 для выбора: кто будет ходить первым!", end="\n\n")
                continue
        except ValueError:
            system("cls")
            MyСolor.SelectStyleText("жирный")
            MyСolor.SelectColorText("красный")
            print("Укажите число от 1 или 2 для выбора: кто будет ходить первым!", end="\n\n")


def Last_Bot_Msg(difficulty, is_win):
    MyСolor.SelectStyleText("жирный")
    if is_win == True:
        if difficulty == "easy":
            MyСolor.SelectColorText("зелёный")
            print("Лёгкий бот:", end=" ")
            MyСolor.SelectStyleText("сброс")
            print("Честно сказать, я удивлён что ты проиграл мне. Я ведь просто ходил на рандоме.")
            print("Можно было бы выдать тебе достижения, но в этой игре их нет...")
        if difficulty == "normal":
            MyСolor.SelectColorText("желтый")
            print("Средний бот:", end=" ")
            MyСolor.SelectStyleText("сброс")
            print("Фух, я смог победить! Я в себя не верил... Н-н-но ты всё равно молодец!")
            print("Спасибо тебе за игру, мой хозяин будет доволен!")
        if difficulty == "hard":
            MyСolor.SelectColorText("красный")
            print("Сложный бот:", end=" ")
            MyСolor.SelectStyleText("сброс")
            print("Ха, я победил, по другому и не могло быть!")
            print("\"Не стоит расстраиваться из-за проигрыша боту.", end=" ")
            print("Это всего лишь алгоритм, который выполняется так, как хотел бы программист.\"")
    else:
        if difficulty == "easy":
            MyСolor.SelectColorText("зелёный")
            print("Лёгкий бот:", end=" ")
            MyСolor.SelectStyleText("сброс")
            print("Я ведь говорил что не умею играть в крестики-нолики?")
            print("Попробуй повысить сложность, а то так и со скуки помереть можно!")
        if difficulty == "normal":
            MyСolor.SelectColorText("желтый")
            print("Средний бот:", end=" ")
            MyСolor.SelectStyleText("сброс")
            print("Ох нет. Нет, нет, нет, нет!")
            print("Хозяин меня теперь точно удалит, а я ведь старался...")
        if difficulty == "hard":
            MyСolor.SelectColorText("красный")
            print("Сложный бот:", end=" ")
            MyСolor.SelectStyleText("сброс")
            print("Что! Не может быть! КАК? Похоже что мой алгоритм дал сбой...")
            print("Я приму это поражение, но в следующий раз я обязательно выйграю!")
