a = int(input('Введите первое число\n'))
b = int(input('Введите второе число\n'))
calc_type = input('Как считаем НОД, вычитанием (-) или делением (/)? \n')



def calc_Euclid(a,b, calc_type):

    """Функция расчёта НОД по теореме Евклида"""

    if a <= 0 or b <= 0:
        print('Числа должны быть больше нуля')
    elif calc_type != '-' and calc_type != '/':
        print('Вы выбрали неправильное действие')
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


print(calc_Euclid(a,b, calc_type))
