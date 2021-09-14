"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""
user_list = [11, 9, 7, 5, 3, 2, 1]
print(f"Рейтинг - {user_list}")
number = int(input("Введите число (111 - выход): "))
while number != 000:
    for el in range(len(user_list)):
        if user_list[el] == number:
            user_list.insert(el + 1, number)
            break
        elif user_list[0] < number:
            user_list.insert(0, number)
        elif user_list[-1] > number:
            user_list.append(number)
        elif user_list[el] > number and user_list[el + 1] < number:
            user_list.insert(el + 1, number)
    print(f"текущий список - {user_list}")
    number = int(input("Введите число: "))
