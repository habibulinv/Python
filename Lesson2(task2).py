n = input("Задайте любой произвольный список значений ").split()
i = 0

for el in range(1, len(n), 2):
    n[i - 1], n[i] = n[i], n[i - 1]
    i += 2

print(' '.join(n))

# 2, 2.34, False
