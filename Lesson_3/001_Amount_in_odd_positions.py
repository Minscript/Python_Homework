# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Очистка консоли и рандом
from os import system
from random import randint
system("cls")


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