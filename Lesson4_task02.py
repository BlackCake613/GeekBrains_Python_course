"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
"""
user_list = [37, 17, 44, 5, 2, 13, 22, 11]
another_list = [el for num, el in enumerate(user_list) if user_list[num - 1] < user_list[num]]
print(f'Исходный список {user_list}')
print(f'Новый список {another_list}')
