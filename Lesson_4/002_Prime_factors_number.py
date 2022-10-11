# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 236 -> [2, 2, 59] -> 2 * 2 * 59

# Очистка консоли
from os import system
system("cls")

n = int(input("Введите натуральное число N: "))


def create_simple_list(n):
    i = 2                       # Минимальное число множителя
    lst = []
    if n == 1 or n == 0:        # Если пользователь введёт 1 или 0
        lst.append(n)
        return lst
    while i <= n:
        if n % i == 0:          # Добавим в лист
            lst.append(i)
            n //= i
            i = 2
        else:                   # Увеличим число на 1
            i += 1
    return lst


lists = create_simple_list(n)
print(f"\nПростые множители числа {n}: {lists}\n")