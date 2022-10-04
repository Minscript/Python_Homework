# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму, округлённую до трёх знаков после точки.

# Очистка консоли
from os import system
system("cls")

n = int(input("Введите число n: "))
lists = [round((1+1/i)**i, 3) for i in range(1, n+1)]

print(f"\nПоследовательность (1+1/n)^n, где n = {n}: {lists}")
print(f"Сумма последовательности от {n}: {round(sum(lists), 3)}\n")

# Функция Python - sum()
# Позволяет суммировать значение в листе.
# Решение без использования данной функции выглядит так:
#
#   result = 0
#   for i in range(len(lists)):
#       result += lists[i]
#   print(result)