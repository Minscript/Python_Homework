# Предложить улучшения кода для четырёх уже решённых задач из семинаров №2-5 с помощью использования: lambda, filter, map, zip, enumerate, list comprehension
#   Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

from functools import reduce
from os import system
from random import randint
system("cls")

lst = [randint(1, 9) for i in range(10)] # Создаём лист с 10 рандомными значениями
print(f"Задан лист: {lst}\n")

lst_odd = [lst[i] for i in range (1, len(lst), 2)] # Из листа выше мы берём только нечётные позиции
print(f"Я посчитаю следующие цифры - {lst_odd}\n")

sum_odd = reduce(lambda x,y: x + y, lst_odd) # По принципу 1 задачи, суммируем значения между собой
print(f"Сумма чисел на нечётных позициях: {sum_odd}\n")

# Старое решение:
'''

# Указать размер и заполнить лист рандомом
def fill_list():
    lst = []
    len_lst = int(input("Задайте длинну списка: "))
    for i in range(len_lst):
        rand = randint(1, 10)
        lst.append(rand)
    return lst


lists = fill_list()
print(f"Задан лист: {lists}\n")


# Сумма нечётных позиций в листе
def sum_of_odd():
    lst = lists.copy()
    index = 0
    res = 0
    print("\nПрограмма: Я посчитаю следующие цифры - ", end="")
    for i in range(len(lst)):
        index += 1
        if index % 2 == 0:
            res += lst[i]
            print(f"{lst[i]}", end=" ")
    return res


sum_odd = sum_of_odd()
print(f"\n\nСумма чисел на нечётных позициях: {sum_odd}\n")

'''