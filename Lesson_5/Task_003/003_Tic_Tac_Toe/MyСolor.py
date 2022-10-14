from colorama import init, Fore, Back, Style
# init(autoreset=True)


def Text(text, reset = True, color_txt = None, color_bg = None, style = None):
    colors = {
        "чёрный": 30,
        "красный": 31,
        "зелёный": 32,
        "желтый": 33,
        "синий": 34,
        "пурпурный": 35,
        "голубой": 36,
        "белый": 37,
        "сброс": 39,
    }
    bg_colors = {
        "чёрный": 40,
        "красный": 41,
        "зелёный": 42,
        "желтый": 43,
        "синий": 44,
        "пурпурный": 45,
        "голубой": 46,
        "белый": 47,
        "сброс": 49,
    }
    styles = {
        "сброс": 0,
        "жирный": 1,
        "курсив": 3,
        "подчёркнутый": 4,
        "пустой": 8,
        "зачёркнутый": 9,
    }

    if color_txt == None:
        if color_bg == None:
            if style == None:
                print(text, end="")
            else:
                print(f"\033[{styles[style]}m" + text, end="")
        else:
            if style == None:
                print(f"\033[{bg_colors[color_bg]}m" + text, end="")
            else:
                print(f"\033[{bg_colors[color_bg]};{styles[style]}m" + text, end="")
    else:
        if color_bg == None:
            if style == None:
                print(f"\033[{colors[color_txt]}m" + text, end="")
            else:
                print(f"\033[{colors[color_txt]};{styles[style]}m" + text, end="")
        else:
            if style == None:
                print(f"\033[{colors[color_txt]};{bg_colors[color_bg]}m" + text, end="")
            else:
                print(f"\033[{colors[color_txt]};{bg_colors[color_bg]};{styles[style]}m" + text, end="")
    if reset == True:
        print("\033[0m")
    else:
        print("\n")


def SelectColorText(color):
    colors = {
        "чёрный": 30,
        "красный": 31,
        "зелёный": 32,
        "желтый": 33,
        "синий": 34,
        "пурпурный": 35,
        "голубой": 36,
        "белый": 37,
        "сброс": 39,
    }
    if color == "нет":
        print("\033[0m")
    else:
        print(f"\033[{colors[color]}m", end="")

def SelectStyleText(style):
    styles = {
        "сброс": 0,
        "жирный": 1,
        "курсив": 3,
        "подчёркнутый": 4,
        "пустой": 8,
        "зачёркнутый": 9,
    }
    print(f"\033[{styles[style]}m", end="")

#Text("Test")
