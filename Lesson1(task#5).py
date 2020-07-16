revenue = int(input("Выручка "))
costs = int(input("Издержки "))

profit = revenue - costs

if profit > 0:
    profAb = int(revenue / costs)
    print(f"Рентабельность {profAb}%")
    worker = int(input("Количество сотрудников "))
    profitPerWorker = int(profit / worker)
    print(f"Прибыль в расчете на одного сотрудника {profitPerWorker}")
else:
    print("Дела плохи...")

