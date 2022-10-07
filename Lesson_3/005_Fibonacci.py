# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Очистка консоли
from os import system
system("cls")

k = int(input("Введите число: "))


def fibonacci(num):
    fib = [0, 1]
    for i in range(num - 1):
        fib.append(fib[-2] - fib[-1])
    fib.reverse()
    for j in range(num):
        fib.append(fib[-1] + fib[-2])
    return fib


fib = fibonacci(k)
print(f"\nСписок чисел Фибоначи из числа {k}: {fib}\n")