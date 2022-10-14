import MyСolor
import Game_Logic
import Game_Field
import Game_Menu
import AI_Logic
from os import system

while True:
    select = Game_Menu.Menu_TTT_Select()
    if select == 1:
        Game_Field.line1 = Game_Field.def_line.copy()
        Game_Field.line2 = Game_Field.def_line.copy()
        Game_Field.line3 = Game_Field.def_line.copy()
        score = 0
        bot_dif = AI_Logic.Difficulty_Bot()
        bot_type = AI_Logic.Bot_Types()
        if bot_type == "X":
            while True:
                system("cls")
                AI_Logic.Bot_Think(bot_dif, bot_type)
                is_win = Game_Logic.IsWin(True)
                if (is_win == True):
                    system("cls")
                    Game_Field.Show_Game_Map("game_map")
                    AI_Logic.Last_Bot_Msg(bot_dif, True)
                    input()
                    break
                score +=1
                if score == 9:
                    system("cls")
                    MyСolor.SelectColorText("желтый")
                    MyСolor.SelectStyleText("жирный")
                    print(" "*4, end="")
                    print("Ничья!")
                    MyСolor.SelectStyleText("сброс")
                    Game_Field.Show_Game_Map("game_map")
                    input()
                    break
                Game_Field.Show_Game_Map("game_map")
                Game_Field.Show_Game_Map("game_step")
                Game_Field.Step(False)
                is_win = Game_Logic.IsWin(False)
                if (is_win == True):
                    system("cls")
                    Game_Field.Show_Game_Map("game_map")
                    AI_Logic.Last_Bot_Msg(bot_dif, False)
                    input()
                    break
                score +=1
        else:
            while True:
                system("cls")
                Game_Field.Show_Game_Map("game_map")
                Game_Field.Show_Game_Map("game_step")
                Game_Field.Step(True)
                is_win = Game_Logic.IsWin(True)
                if (is_win == True):
                    system("cls")
                    Game_Field.Show_Game_Map("game_map")
                    AI_Logic.Last_Bot_Msg(bot_dif, False)
                    input()
                    break
                score +=1
                if score == 9:
                    system("cls")
                    MyСolor.SelectColorText("желтый")
                    MyСolor.SelectStyleText("жирный")
                    print(" "*4, end="")
                    print("Ничья!")
                    MyСolor.SelectStyleText("сброс")
                    Game_Field.Show_Game_Map("game_map")
                    input()
                    break
                AI_Logic.Bot_Think(bot_dif, bot_type)
                is_win = Game_Logic.IsWin(False)
                if (is_win == True):
                    system("cls")
                    Game_Field.Show_Game_Map("game_map")
                    AI_Logic.Last_Bot_Msg(bot_dif, True)
                    input()
                    break
                score +=1
    elif select == 2:
        Game_Field.line1 = Game_Field.def_line.copy()
        Game_Field.line2 = Game_Field.def_line.copy()
        Game_Field.line3 = Game_Field.def_line.copy()
        score = 0
        Game_Menu.InfoForPlayers2()
        while True:
            Game_Field.Show_Game_Map("game_map")
            Game_Field.Show_Game_Map("game_step")
            Game_Field.Step(True)
            system("cls")
            is_win = Game_Logic.IsWin(True)
            if (is_win == True):
                Game_Field.Show_Game_Map("game_map")
                input()
                break
            score += 1
            if score == 9:
                MyСolor.SelectColorText("желтый")
                MyСolor.SelectStyleText("жирный")
                print(" "*4, end="")
                print("Ничья!")
                MyСolor.SelectStyleText("сброс")
                Game_Field.Show_Game_Map("game_map")
                input()
                break
            Game_Field.Show_Game_Map("game_map")
            Game_Field.Show_Game_Map("game_step")
            Game_Field.Step(False)
            system("cls")
            is_win = Game_Logic.IsWin(False)
            if (is_win == True):
                Game_Field.Show_Game_Map("game_map")
                input()
                break
            score += 1
            system("cls")
    elif select == 3:
        break