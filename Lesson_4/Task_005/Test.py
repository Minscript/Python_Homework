# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.

# Очистка консоли и рандом
from os import system
from random import randint
system("cls")

# Функция сохранения в файл
def write_file(string):
    with open('Lesson_4/Task_005/poly1.txt', 'w') as data:
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
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0 or lst[i+2] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

# Получение степени многочлена
def sq_poly(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

# Получение коэффицента члена многочлена
def k_poly(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

# разбор многочлена и получение его коэффициентов
def calc_poly(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if sq_poly(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1
    index = l-1
    while index >= 0:
        if sq_poly(st[index]) != -1 and sq_poly(st[index]) == i:
            lst.append(k_poly(st[index]))
            index -= 1
            i += 1
        else:
            lst.append(0)
            i += 1
        
    return lst
    


# Cоздание двух файлов

k1 = int(input("Введите натуральную степень для 1 файла\nk = "))
k2 = int(input("Введите натуральную степень для 2 файла\nk = "))
koef1 = create_polynominal(k1)
koef2 = create_polynominal(k2)

write_file("Lesson_4/Task_005/poly1.txt", create_string(koef1))
write_file("Lesson_4/Task_005/poly2.txt", create_string(koef2))

# Нахождение суммы многочлена

with open('Lesson_4/Task_005/poly1.txt', 'r') as data:
    st1 = data.readlines()
with open('Lesson_4/Task_005/poly2.txt', 'r') as data:
    st2 = data.readlines()

print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")

lst1 = calc_poly(st1)
lst2 = calc_poly(st2)

ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)

lst_new = [lst1[i] + lst2[i] for i in range(ll)]

if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll,mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll,mm):
        lst_new.append(lst2[i])

write_file("Lesson_4/Task_005/res.txt", create_string(lst_new))

with open('Lesson_4/Task_005/res.txt', 'r') as data:
    st3 = data.readlines()

print(f"Результат: {st3}")