# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Очистка консоли
from os import system
system("cls")

n = int(input("Введите число N: "))


def factorial(n):
    result = 1
    lists = []
    for i in range(1, n+1):
        result *= i
        lists.insert(i, result)
    return lists


print(f"\nПроизведение чисел от 1 до {n}: {factorial(n)}\n")