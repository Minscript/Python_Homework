# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Очистка консоли
from os import system
system("cls")

x = int(input("Введите значение Х: "))
y = int(input("Введите значение Y: "))

if x > 0 and y > 0:
    print(f"\nX:{x}, Y:{y}\nНомер четверти плоскости: 1\n")
elif x < 0 and y > 0:
    print(f"\nX:{x}, Y:{y}\nНомер четверти плоскости: 2\n")
elif x < 0 and y < 0:
    print(f"\nX:{x}, Y:{y}\nНомер четверти плоскости: 3\n")
elif x > 0 and y < 0:
    print(f"\nX:{x}, Y:{y}\nНомер четверти плоскости: 4\n")
else:
    print("\nX и Y ≠ 0!\n")