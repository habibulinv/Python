goods_list = []
features = {"название": "", "цена": "", "количество": "", "ед": ""}
analytics = {"название": [], "цена": [], "количество": [], "ед": []}
i = 1

while True:
    if input("Для выхода из программы нажмите 'Q' для продолжения 'Enter': ").upper() == "Q":
        break
    i += 1
    for f in features.keys():
        _ = input(f"Введите значения свойства '{f}': ")
        features[f] = int(_) if( f == "цена" or f == "количество") else _
        analytics[f].append(features[f])
    goods_list.append((i, features))

    for key, value in analytics.items():
        print(f"{key[:10]:>30}: {value}")
    print("*" *40)

# for g in goods_list2:
#    types = g("название")
#    prices = g("цена")
#    qun = g("количество")
#    measures = g("eд")

#  print(goods_list2)
