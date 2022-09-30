# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Очистка консоли
from os import system
system("cls")


def number_is_day (): # Функция вывода числа
    day = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    number = int(input("Введите число: "))
    if number < 1 or number > 7:
        print(f"Число {number} не является днём недели!")
    elif number >= 1 and number <= 5:
        print(f"Число {number} - {day[number-1]}. Не является выходным!")
    else:
        print(f"Число {number} - {day[number-1]}. Выходной день!")


number_is_day()