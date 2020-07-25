"""Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран."""


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

all_objects = {}
one_object = {}


with open("text_6.txt", "r", encoding="utf-8") as num_file:

    for str_num in num_file.readlines():
        hourSum = 0
        str_num = str_num.split(" ")
        all_objects.update(one_object)
        for el in str_num:
            if is_number(el):
                el = int(el)
                hourSum += el
        one_object = {str_num[0]: hourSum}


print(all_objects)
