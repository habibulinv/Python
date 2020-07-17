"""
summator - запрашивает у пользователя строку чисел, разделенных пробелом.

Enter - вывести сумма чисел.

После нажатия Enter вод чисел можно продолжить и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.

"""


def summator():
    sum = 0
    close = False
    while close == False:
        num = input("Введите число или нажмите Q для выхода: ").split()

        arg = 0
        for el in range(len(num)):
            if num[el].upper() == "Q":
                close = True
                break
            else:
                arg = arg + int(num[el])
        sum = sum + arg
        print(f'Current sum is {sum}')
    print(f'Your final sum is {sum}')


summator()
