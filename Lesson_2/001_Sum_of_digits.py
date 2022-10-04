# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Очистка консоли
from os import system
system("cls")

number = str(input("Введите вещественное число: "))


def sum_num_in_number(number):
    if float(number) < 0:
        num = float(num) * (-1)
    num = 0

    for i in str(number):
        if i != '.':
            num += int(i)
    return num


print(f"\nСумма цифр в числе {number}: {sum_num_in_number(number)}\n")