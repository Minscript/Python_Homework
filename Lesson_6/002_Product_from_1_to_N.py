# Предложить улучшения кода для четырёх уже решённых задач из семинаров №2-5 с помощью использования: lambda, filter, map, zip, enumerate, list comprehension
#   Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

from os import system
system("cls")

n = int(input("Введите число N: "))

factorial = lambda x: 1 if x == 0 else x * factorial(x - 1) # Высчитываем факториал рекурсией

lst = [factorial(i) for i in range(1, n+1)] # Добавляем в лист рекурсию от 1 до N
print(f"\nПроизведение чисел от 1 до {n}: {lst}\n")

# Старое решение:
'''

n = int(input("Введите число N: "))

def factorial(n):
    result = 1
    lists = []
    for i in range(1, n+1):
        result *= i
        lists.insert(i, result)
    return lists


print(f"\nПроизведение чисел от 1 до {n}: {factorial(n)}\n")

'''