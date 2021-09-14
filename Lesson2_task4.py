"""
4.  Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""
some_str = input("Введите строку: ")
random_word = []
num = 1
for el in range(some_str.count(' ') + 1):
    random_word = some_str.split()
    if len(str(random_word)) <= 10:
        print(f" {num} {random_word [el]}")
        num += 1
    else:
        print(f" {num} {random_word [el] [0:10]}")
        num += 1
