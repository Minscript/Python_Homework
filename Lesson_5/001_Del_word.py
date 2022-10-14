# Напишите программу, удаляющую из текста все слова, содержащие "абв".

# Очистка консоли
from os import system
system("cls")

custom_text = "Алфавит русабвкогоязыка: абвгдеёжзийклмнопрстуфхцчъыьэюя abcdifg... \
    Главная задача: удалить слова содержащие буабвкв абв \"а, б и в\" в абв тексте."

def del_words(read_text, del_text):
    read_text = list(filter(lambda x: del_text not in x, read_text.split()))
    return " ".join(read_text)

my_text = del_words(custom_text, "абв")                                      
print(my_text)