import sys

def input_numbers():
    try:
        a = int(input('Введите первое число\n'))
        b = int(input('Введите второе число\n'))
        return a, b
    except ValueError:
        print('Нужно ввести число или цифру')
        sys.exit(1)

def calc_type_input():
    calc_type = input('Как считаем НОД, вычитанием (-) или делением (/)? \n')
    return calc_type

def calc_Euclid(a, b, calc_type):

    """Функция расчёта НОД по теореме Евклида"""

    if a <= 0 or b <= 0:
        return ('Числа должны быть больше нуля')
    elif calc_type != '-' and calc_type != '/':
        return ('Вы выбрали неправильное действие')
    else:
        if calc_type == '-': #Расчёт НОД вычитанием
            while a != 0 and b != 0:  # пока оба числа не 0 цикл не закончится
                result = abs(a - b)
                if result == 0:
                    return b  # возвращает НОД, если результат равен нулю
                else:
                    if a > b:  # ставит большее число вместо результата
                        a = result
                    else:
                        b = result

        elif calc_type == '/':  #Расчёт НОД делением
            while a != 0 and b != 0:
                if a > b:
                    a = a % b  # делим большее число на меньшее и перезаписываем остаток в переменную
                else:
                    b = b % a  # делим большее число на меньшее и перезаписываем остаток в переменную
            return a + b



a, b = input_numbers()
calc_type = calc_type_input()
print(calc_Euclid(a,b, calc_type))
