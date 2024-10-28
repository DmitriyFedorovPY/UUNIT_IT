'''Лабораторная работа №1. Введение в Python
    Федоров Д.А., задание 2, вариант 2'''

import math

def find_h():
    try:
        x = int(input('Введите x\n'))
        y = int(input('Введите y\n'))
        if x > y :
            h = math.atan(x + abs(y))
        elif x < y:
            h = math.atan(abs(x) + y)
        else:
            h = (x + y) ** 2
        return h
    except ValueError:
        print('Для получения результата нужно ввести переменную x и переменную y. '
              'Переменные должны быть цифрами или числами.')

print(find_h())