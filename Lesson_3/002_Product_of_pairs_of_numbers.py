# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Очистка консоли и рандом
from os import system
from random import randint
system("cls")


# Указать размер и заполнить лист рандомом
def fill_list():
    lst = []
    len_lst = int(input("Задайте длинну списка: "))
    for i in range(len_lst):
        rand = randint(1, 9)
        lst.append(rand)
    return lst


lists = fill_list()
print(f"Задан лист: {lists}\n")


def multi_pairs():
    lst = lists.copy()
    new_lst = []

    # Проверяем длинну листа на чётность (нужно для цикла for)
    if len(lst)%2==0: 
        length = int(len(lst)/2)
    else:
        length = int((len(lst)/2)+1)

    for i in range (length):
            first = lst[i]
            last = lst[-i -1]
            # Можно раскомментировать для провеки
            #print(f"Программа выполнила {i+1} итерацию: {first} * {last} = {first*last}\n")
            new_lst.append(first*last)
    return new_lst


new_lists = multi_pairs()

print(f"Результат произведения пар: {new_lists}\n")