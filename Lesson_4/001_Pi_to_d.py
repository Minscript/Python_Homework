# Вычислить число π c заданной точностью d

# Очистка консоли
from os import system
system("cls")

d = int(input("Введите точность определения числа π: "))


def pi_to_d(d):
    pi = 3 # Целое число π
    sign = 1 # Символ
    m = 2
    while abs(pi - (pi + sign * 4 / ( m ** 3 + 3 * m ** 2 + 2 * m))) > 10 ** (-d - 1): # Абсолютное значение числа (определяем число π)
        pi = pi + sign * 4 / (m ** 3 + 3 * m ** 2 + 2 * m)
        sign = -1 * sign
        m = m + 2
    return round((pi + (pi + sign * 4 / (m ** 3 + 3 * m ** 2 + 2 * m))) / 2, d) # Вернём число π c заданной точностью d


pi = pi_to_d(d)
print(f"\nС точностью до d = {d}, число π = {pi}\n")

# ИМХО: Вообще мне кажется что было бы гораздо проще импортировать "math pi" и просто вывести π с кол-во знаков после запятой до d.
# И да, она работает только с целыми числами, сломал голову пока искал и писал формулу числа π, так что возможно решения либо не верное либо не полное.