# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Очистка консоли и рандом
from os import system
from random import randint
system("cls")


# Функция сохранения в файл
def write_file(string):
    with open('Lesson_4/Task_004/polynomial.txt', 'w') as data:
        data.write(string)


# Функция рандомизации числа
def rnd():
    return randint(0,100)


# Создание многочлена
def create_polynominal(k):
    lst = [rnd() for i in range(k+1)]
    return lst
    

# Содержание файла
def create_string(sp):
    lst= sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

k = int(input("Введите натуральную степень k = "))
koef = create_polynominal(k)

write_file(create_string(koef))
print("\nФайл обновлён!\n")