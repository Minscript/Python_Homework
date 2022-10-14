# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

from os import system
system("cls")

text = "abaa111z22qwerrrtt"
print(f"Вводный текст: {text}\n")

def zipping(f_or_t, type):
    simbol = []
    amount = []
    current_simbol = f_or_t[0]
    counter = 0
    for i in range(len(f_or_t)):
        if current_simbol != f_or_t[i]:
            simbol.append(f_or_t[i-1])
            amount.append(counter)
            counter = 1
            current_simbol = f_or_t[i]
        else:
            counter += 1
        if i == len(f_or_t)-1:
            simbol.append(f_or_t[i-1])
            amount.append(counter)
    if type == "simbol":
        return simbol
    if type == "amount":
        return amount


simbol = zipping(text, "simbol")
amount = zipping(text, "amount")


def print_zipping(si, am):
    print("Итоги сжатия [символ, кол-во]: ", end="")
    for i in range(len(si)):
        print(f"{si[i]}:{am[i]} ", end="")


print_zipping(simbol, amount)


def unzipping(si, am):
    print("\n\nИтог восстановления данных: ", end="")
    for i in range(len(si)):
        print(f"{si[i]*am[i]}", end="")

unzipping(simbol, amount)