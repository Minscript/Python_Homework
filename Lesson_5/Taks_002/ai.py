from os import system
import random


def step_bot(candy_bag):
    # Для удобства создаём два режима - Опасность и Победа.
    warn_mod = False
    win_mod = False

    if candy_bag <= 56:
        warn_mod = True
        # Отладка
        # input("Бот напрягается!")

    if candy_bag <= 28:
        win_mod = True
        # Отладка
        # input("Бот чует победу!")

    # Обрабатываем дальнейший ход
    # При 28 конфетах бот выйграет, даже если их будет <28
    if win_mod == True:
        i_think = 28
        temp = i_think - candy_bag
        if temp == 0:
            system("cls")
            input("🤖 Бот забирает 28 конфет!")
            return 28
        elif temp !=0:
            system("cls")
            input(f"🤖 Бот забирает {candy_bag} конфет!")
            return candy_bag

    # Включает режим опасности. Сделает всё, чтобы выиграть!
    if warn_mod == True:
        i_think = 27
        if candy_bag - i_think == 29:
            system("cls")
            input(f"\n🤖 Бот забирает {i_think} конфет!")
            return i_think
        for i in range(1, 28):
            if candy_bag - i == 29:
                system("cls")
                input(f"🤖 Бот забирает {i} конфет!")
                return i
    # Режим отладки для проверки. Если при игре будет видно это сообщение, то это означает что что-то пошло не так!
        input("\nБот начинает волноваться и искрить. Он может взорваться!")

    # Или бот просто сделает ход
    # Создадим симуляцию того, что это играет человек. Глупо будет если бот будет всегда ходить по 28. Шанс 30% взять рандомное кол-во конфет!
    choice_type = random.randint(1, 100)
    if choice_type < 30:
        take_random_candy = random.randint(1, 28)
        system("cls")
        input(f"🤖 Бот забирает {take_random_candy} конфет!")
        return take_random_candy
    else:
        system("cls")
        input(f"🤖 Бот забирает 28 конфет!")
        return 28