# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Очистка консоли и рандом
from os import system
import random
system("cls")


# Указать размер и заполнить лист рандомом
def fill_list():
    lst = []
    len_lst = int(input("Задайте длинну списка: "))
    for i in range(len_lst):
        # Рандомизируем значения, округляем до 2х знаков после точки, переводим из str в float
        rand = float(format(random.uniform(1, 2), ".2f"))
        lst.append(rand)
    return lst


lists = fill_list()
print(lists, end="\n\n")


# Находим минимальное число
def find_min():
    lst = lists.copy()
    min = 1
    for i in lst:
        if (i - int(i)) <= min:
            min = i - int(i)
    min = float(format(min, ".2f"))
    print(f"Минимальное значение: {min}")
    return min


# Находим максимальное число
def find_max():
    lst = lists.copy()
    max = 0
    for i in lst:
        if (i - int(i)) >= max:
            max = i - int(i)
    max = float(format(max, ".2f"))
    print(f"Максимальное значение: {max}\n")
    return max

minimal = find_min()
maximal = find_max()

res = maximal - minimal
res = format(res, ".2f")

print(f"Разница между максимальным и минимальным значением дробной части: {res}\n")

# Решение не самое оптимальное, но зато у нас есть 2 функции по нахождению максимального и минимального числа, которое можно использовать в других программах