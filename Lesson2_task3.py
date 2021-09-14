"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
season_list = ['winter/зима', 'spring/весна', 'summer/лето', 'autumn/осень']
season_dictionary = {1: 'winter/зима', 2: 'spring/весна', 3: 'summer/лето', 4: 'autumn/осень'}
month = int(input('Введите числовое значения мемсяца от 1 до 12: '))
if month == 1 or month == 2 or month == 12:
    print(season_dictionary.get(1))
    print(season_list[0])
elif month == 3 or month == 4 or month == 5:
    print(season_dictionary.get(2))
    print(season_list[1])
elif month == 6 or month == 7 or month == 8:
    print(season_dictionary.get(3))
    print(season_list[2])
elif month == 9 or month == 10 or month == 11:
    print(season_dictionary.get(3))
    print(season_list[3])
else:
    print('Внимательно прочитайте параметры ввода значения')

