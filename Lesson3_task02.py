"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""
def user_data (name, surname, birth_year, city, email, phone):
    print(name, surname, birth_year, city, email, phone)

user_data(name='Anna', surname='Visness', birth_year=1992, city='Voscow', email='email@', phone='0232')