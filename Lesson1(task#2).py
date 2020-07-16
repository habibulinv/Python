ourTime = int(input("Введите количество секунд: "))

h = ourTime // 3600
m = int((ourTime % 3600) / 60)
s = ourTime % 60

print(f"{h:02} : {m:02} : {s:02}")




