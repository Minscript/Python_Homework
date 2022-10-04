# Реализуйте алгоритм перемешивания списка.

# Очистка консоли
from os import system
from random import randint
system("cls")

length = int(input("Задайте длинну списка: ")) # Не задавайте большие значения, их придётся писать в ручную!
print("") # Доп отступ для красоты

def create_lists(lenght):
    new_list = []
    for i in range(1, lenght+1):
        new_list.append(input(f"Добавьте {i} элемент в лист: "))
    return new_list


lists = create_lists(length)


def swap_lists():
    old_lists = lists.copy()
    new_lists = []
    for i in range(len(lists)):
        rand_number = randint(0, len(old_lists)-1)
        new_lists.append(old_lists[rand_number])
        old_lists.pop(rand_number)
    return new_lists


print(f"\nБыло: {lists}")
print(f"Стало: {swap_lists()}\n")