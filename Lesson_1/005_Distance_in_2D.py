# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Очистка консоли
from os import system
system("cls")


def CordInput(cord_name, point_name): # Функция для ввода данных
    temp = float(input(f"Введите координату {cord_name} точки {point_name}: "))
    return temp


x1 = CordInput("X", "A")
y1 = CordInput("Y", "A")
x2 = CordInput("X", "B")
y2 = CordInput("Y", "B")

sqrt = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (0.5), 2)
print(f'\nРасстояние между точками: A - ({x1}, {y1}) и B - ({x2}, {y2}) = {sqrt}\n')