# Изменить текст в файле
def file_write(text, file = "Lesson_7/Contact/phones.txt"):
    with open(file, "w", encoding="utf_8") as file:
        file.write(text + "\n")


# Получить весь текст из файла
def file_read(file = "Lesson_7/Contact/phones.txt"):
    with open(file, "r", encoding="utf_8") as file:
        lines = file.readlines()
    return lines


# Добавить текст в файл
def file_add(text, file = "Lesson_7/Contact/phones.txt"):
    with open(file, "a", encoding="utf_8") as file:
        file.write(text + "\n")