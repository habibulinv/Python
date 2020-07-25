"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл"""

translate = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("text_4.txt", "r", encoding="utf-8") as file:
    for str_num in file.readlines():
        str_num = str_num.split(" ")
        for eng_num in translate:
            if str_num[0] == eng_num:
                str_num[0] = translate[eng_num]
        with open("text_4(new).txt", "a+", encoding="utf-8") as new_file:
            new_file.writelines(str_num)
