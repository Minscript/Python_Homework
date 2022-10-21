import file_editor as f_edit


# Удаление лишнего текста (корректировка)
def cur_str(text, before, after):
    if text == "":
        return ""
    else:
        new_text = text[before:-after]
        if text == "":
            return ""
        else:
            return new_text


# Функция оставляет только данные (имя, телефон, описание)
def clear_stats():
    lst = f_edit.file_read()

    index = 0
    new_lst = []
    for i in range(len(lst)):
        if index == 4:
            index = 0
            continue
        if index == 1:
            new_lst.append(cur_str(lst[i],5,1)) # Удаляем: "Имя: " и "\n"
        elif index == 2:
            new_lst.append(cur_str(lst[i],9,1)) # Удаляем: "Телефон: " и "\n"
        elif index == 3:
            new_lst.append(cur_str(lst[i],10,1)) # Удаляем: "Описание: " и "\n"
        index += 1
    return new_lst


# Форматирует текст под MarkDown
def format_md():
    lst = clear_stats()

    index = 0
    new_lst = ["# Телефонный справочник", "---"]
    for i in range (len(lst)):
        if index == 0:
            new_format = (f"👤 **{lst[i]}**\n")
            new_lst.append(new_format)
        if index == 1:
            new_format = (f"* 📞 {lst[i]}\n")
            new_lst.append(new_format)
        if index == 2:
            new_format = (f"> 💬 {lst[i]}\n\n")
            if new_format == (f"> 💬 \n\n"):
                new_format = (f"> ⚠ Описание не указано\n\n")
            new_lst.append(new_format)
        index += 1
        if index == 3:
            new_lst.append("---")
            index = 0
    return new_lst


# Синхронизирует изменения обычного txt с MarkDown
def sunc_md():
    clear = ""
    text = format_md()
    f_edit.file_write(clear, "Lesson_7/Contact/phones.md") # Очистим
    for i in range(len(text)):
        print(text[i])
        f_edit.file_add(text[i], "Lesson_7/Contact/phones.md")