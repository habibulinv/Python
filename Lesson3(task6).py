"""int_func - получает строку из слов, разделенных пробелом. Выводит эти слова с заглавной буквы

print(int_func(‘text message’)) -> Text Message
"""

def int_func(*args):
    word = input("Input words ")
    print(word.title())


int_func()
