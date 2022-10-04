# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на позициях a и b. Значения N, a и b вводит пользователь с клавиатуры.

# Очистка консоли
from os import system
system("cls")

n = int(input("Введите число N: "))


def fill_list(n):
    lists = []
    for i in range(-n, n+1):
        lists.append(i)
    return lists


lists = fill_list(n)


def input_index(comment, lists):
    while True:
        try:
            print(f"\nТекущий список: {lists}")
            temp = int(input(comment))
            if (temp <0 or temp >len(lists)-1):
                system("cls")
                print(f"Укажите целое число от 0 до {len(lists)-1}!")
                continue
            return temp
        except ValueError:
            system("cls")
            print("Укажите целое число!")


a = input_index("Введите 1 позицию элемента: ", lists)
b = input_index("Введите 2 позицию элемента: ", lists)


def sum_index(a, b, lists):
    result = lists[a] + lists[b]
    return result


print(f"\nСумма элементов а: {a} и b: {b}\nв списке: {lists} = {sum_index(a, b, lists)}")
print(f"\n({lists[a]}) + ({lists[b]}) = {sum_index(a, b, lists)}\n")