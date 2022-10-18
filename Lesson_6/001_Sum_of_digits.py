# Предложить улучшения кода для четырёх уже решённых задач из семинаров №2-5 с помощью использования: lambda, filter, map, zip, enumerate, list comprehension
    # Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

from functools import reduce
from os import system
system("cls")

number = (input("Введите вещественное число: "))

lst = list(map(int, [x for x in number if x != "."])) # Создаём лист из цифр игнорируя точку

sum = reduce(lambda x,y: x + y, lst) 
# И тут я открываю для себя эту прекрасную функцию. Она выполняет заданную функцию последовательно
#   к каждому элементу списка, возращая одно значение, в данном примере сумму всех чисел списка.
#   Узнал что раньше была в Python 2 на равне с lambda, filter и пр... Теперь это часть
#   библиотеки functools. Потрясающе, код из ~10 строк превратился в 3!
# А ещё проще: функция Sum(), суммирующая весь список

print(f"\nСумма цифр в числе {number}: {sum}\n")

# Старое решение:
'''

number = (input("Введите вещественное число: "))


def sum_num_in_number(number):
    if float(number) < 0:
        num = float(num) * (-1)
    num = 0

    for i in str(number):
        if i != '.':
            num += int(i)
    return num


print(f"\nСумма цифр в числе {number}: {sum_num_in_number(number)}\n")

'''