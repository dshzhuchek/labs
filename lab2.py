def a1():
    a = input('Введите пароль')
    b = input("Повторите пароль")

    if a == b:
        print("Пароль принят")
    else:
        print("Пароль не принят")

def a2():
    number = int(input("Введите номер места: "))

    if number in range(1, 37):
        if number % 2 == 0:
            print("У Вас верхнее в купе")
        else:
            print("У Вас нижнее в купе")
    if number in range(37, 55):
        if number % 2 == 0:
            print("У Вас верхнее боковое")
        else:
            print("У Вас нижнее боковое")
    if number not in range(1, 55):
        print("Такого места нет")

def a3():
    year = int(input("Введите год"))

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Год", year, "- високосный")
    else:
        print("Год", year, "- не високосный ")

def a4():
    color1 = input("Введите первый цвет")
    color2 = input("Введите второй цвет")

    if (color1 == 'красный' or color1 == 'синий' or color1 == 'желтый') and (
            color2 == 'красный' or color2 == 'синий' or color2 == 'желтый'):
        if color1 == 'красный' and color2 == 'синий':
            print('фиолетовый')
        if color1 == 'красный' and color2 == 'желтый':
            print('оранжевый')
        if color1 == 'синий' and color2 == 'желтый':
            print('зеленый')
    else:
        print('Можно вводить только красный, синий или зеленый')

def a5():
    i = ''
    a = ''
    while a != 'stop':
        a = input('Введите слово')
        i += ' ' + a
    print(i)