"""Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

finalSum = 0

with open("text_5.txt", "w+", encoding="utf-8") as num_file:
    num_file.write(input("Введите несколько чисел через пробел: "))

with open("text_5.txt", "r", encoding="utf-8") as num_file:
    for str_num in num_file.readlines():
        str_num = str_num.split(" ")
        for num in str_num:
            num = int(num)
            finalSum += num

print(f"Сумма чисел в файле: {finalSum}")
