def b1:
    n = int(input('Введите N'))
    b = 0
    i = ''
    while n != b:
        a = input('Введите слово') + ' '
        i += ' ' + a
        b += 1
    print(i)

def b2():
    i = ''
    a = ''
    while a != 'stop':
        a = input('Введите слово')
        i += ' ' + a
    print(i)

def b3():
    i = str(input('Введите слово'))
    if 'ф' in i or 'Ф' in i:
        print('Ого! Это редкое слово')
    else:
        print('Эх, это не очень редкое слово')

def b4():
    from random import randint
    n = 0
    while n != 3:
        a = randint(0, 11)
        b = randint(0, 11)
        print(a, ' + ', b, ' = ')
        i = int(input())
        if a + b == i:
            print('Правильно!')
        else:
            n += 1
            print('Ответ неверный')
    if n == 3:
        print('Игра закончена')