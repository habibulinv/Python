"""Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке."""

lines = 0
words = 0

with open("text_2.txt", "r+", encoding="utf-8") as text_file:
    for line in text_file.readlines():
        lines += 1
        line_split = line.split(" ")
        word = len(line_split)
        print(f"{line}" + ("*"*5) + f" Количество слов {len(line_split)}")


print(f"\nОбщее воличество строк {lines}")



