'''Лабораторная работа №1. Введение в Python
    Федоров Д.А., задание 1, вариант 2'''

import math

def equation_1(): #1 способ
    x = int(input('Введите x\n')) #можно без переноса строки, но мне кажется, что так красивее
    y = int(input('Введите y\n')) #можно инпутки засунуть в парамерты, но мне кажется, что это некрасиво

    d = (2*math.cos(x - math.pi/6))/(1/2 + math.sin(y)**2) + (abs(y - x))/3
    return d


def equation_2(x,y): #2 способ
    d = (2 * math.cos(x - math.pi / 6)) / (1 / 2 + math.sin(y) ** 2) + (abs(y - x)) / 3
    return d

print(equation_1())
print(equation_2(2,1))
