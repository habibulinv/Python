my_list = [9, 9, 8, 5, 4, 3, 3, 1, 1, 1]
newPlace = int(input("Введите новое значение ретинга "))
y = 0

for i in my_list:
    if newPlace <= i:
        y += 1
my_list.insert(y, str(newPlace))

print(my_list)
