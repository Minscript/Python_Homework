# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Очистка консоли
from os import system
system("cls")

number = int(input("Введите число для преобразовывания его в двоичную систему счисления: "))


def dec_to_bin(num):
    binary = ""
    while num != 0:
        binary = str(num % 2) + binary
        num //= 2
    return binary


binary = dec_to_bin(number)
print(f"\nДесятичное число: {number}, в двоичной системе: {binary}\n")