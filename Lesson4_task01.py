"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
def sal():
    try:
        time = float(input('Выработка в часах "hh" '))
        salary = int(input('Ставка сотрудника $ '))
        bonus = int(input('Премия сотрудника $ '))
        res = time * salary + bonus
        print(f'заработная плата сотрудника  {res}')
    except ValueError:
        return print('Допустим только числовой ввод!')
sal()
