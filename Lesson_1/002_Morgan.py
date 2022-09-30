# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# Очистка консоли
from os import system
system("cls")


def Mor_D(x, y, z): # Функция Моргана
    print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} ---> {(not (x or y or z)) == (not x and not y and not z)}")
    return (not (x or y or z)) == (not x and not y and not z)


if (Mor_D(0, 0, 0) and Mor_D(0, 0, 1) and Mor_D(0, 1, 0) and Mor_D(0, 1, 1)
and Mor_D(1, 0, 0) and Mor_D(1, 0, 1) and Mor_D(1, 1, 0) and Mor_D(1, 1, 1)):
    print("\nУтверждение истинно!\n")
else:
    print("\nУтверждение ложно!\n") # Оно не выполнится, но для логики оставлю такой вариант