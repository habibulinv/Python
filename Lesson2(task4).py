words = input("введите несколько слов через пробел ").split()

for ind, i in enumerate(words):
    print(ind+1, i[0:10])

