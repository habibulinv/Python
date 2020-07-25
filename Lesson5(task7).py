"""Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Итоговый список сохранить в виде json-объекта в соответствующий файл.
"""
import json


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


"""функция проверки на число"""


def profit(earn, costs):
    return earn - costs


"""функция подсчета прибыли"""


def average(profits_sum, average_qty):
    return profits_sum / average_qty


"""функция подсчета средней прибыли"""

final_list = []
firm_balance = {}
profits_sum = 0
average_qty = 0

with open("text_7.txt", "r", encoding="utf-8") as firm_file:
    for firm in firm_file.readlines():
        firm = firm.split(" ")
        earn = int(firm[2])
        """выделяем из строки выручку"""
        if is_number(firm[3]):
            costs = int(firm[3])
        else:
            costs = int(firm[3][:-2])
        """выделяем из строки издержки.
        Так как последние значения содержат "\n" то заводим условия которое убирает эту часть строки"""
        firm_dict = {firm[0]: profit(earn, costs)}
        firm_balance.update(firm_dict)
        """собираем словарь с фирмами и прибылью. используем фунцию profit"""
        if profit(earn, costs) > 0:
            profits_sum += profit(earn, costs)
            average_qty += 1
        average_profit = {"Средняя прибыль": average(profits_sum, average_qty)}
        """считаем среднюю прибыль с условием, что отрицаиельные показатели в расчет не берутся и создаем словарь"""

final_list.append(firm_balance)
final_list.append(average_profit)
"""Добавляем оба словаря в финальный список"""

print(f"Итоговый список \n {final_list}")

with open("text_7json.json", "w", encoding="utf-8") as firm_json_file:
    json.dump(final_list, firm_json_file, ensure_ascii=False)
