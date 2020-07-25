"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников"""


def midSalary(sumSalar, qty):
    return sumSalar / qty


sumSalar = 0
qty = 0

print("Зарплата ниже 20000$ у следующих сотрудников:")
with open("text_3.txt", "r", encoding="utf-8") as salary:
    for employ in salary.readlines():
        person = employ.split(" ")
        if int(person[1][0:5]) < 20000:
            print(f"{person[0]:>20}")
        sumSalar += int(person[1][0:5])
        qty += 1

print("*" * 20)
print(f"Средняя зарплата: {midSalary(sumSalar, qty)}")
