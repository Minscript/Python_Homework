# Предложить улучшения кода для четырёх уже решённых задач из семинаров №2-5 с помощью использования: lambda, filter, map, zip, enumerate, list comprehension
#   Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на позициях a и b. Значения N, a и b вводит пользователь с клавиатуры.

from os import system
system("cls")

n = int(input("Введите число N: "))
lst = [i for i in range(-n, n+1)] # Создаём лист от -n до n

a = int(input("Введите 1 позицию элемента: "))
b = int(input("Введите 2 позицию элемента: "))

sum_index = lambda x, y, lst_: lst_[x] + lst_[y] # Функция суммирования позиций в листе по индексу
sum_ = sum_index(a, b, lst)

print(f"\nСумма элементов а: {a} и b: {b}\nв списке: {lst} = {sum_}")
print(f"\n({lst[a]}) + ({lst[b]}) = {sum_}\n")

# Старое решение:
'''

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

'''