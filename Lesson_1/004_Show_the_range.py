# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# Очистка консоли
from os import system
system("cls")

quart = int(input("Введите четверть плоскости: "))

if quart == 1:
    print("\nX: 0 -> +∞\nY: 0 -> +∞\n")
elif quart == 2:
    print("\nX: 0 -> -∞\nY: 0 -> +∞\n")
elif quart == 3:
    print("\nX: 0 -> -∞\nY: 0 -> -∞\n")
elif quart == 4:
    print("\nX: 0 -> +∞\nY: 0 -> -∞\n")
else:
    print("\nНужно указать четверть (числа от 1 до 4)!\n")