def d1():
    s = [1, 2, 3, 4, 5]
    x =int(input('Введите число'))
    if x in s:
        print('Вы угадали')
    else:
        print('Вы не угадали')

def d2():
    d = []
    s = [1 ,3 ,5 ,3 ,5 ,2 ,6]
    for x in s:
        if s.count(x) > 1:
            if x not in d:
                d.append(x)
    print(*d)

def d2_2():
    s = [1, 3, 5, 3, 5, 2, 6]
    d = {x for x in s if s.count(x)>1}
    print(*d)

def d3():
    days = ('Пн','Вт','Ср','Чт','Пт' ,'Сб','Вс')
    s = int(input('Введите количество выходных'))
    for i in days:
        print('Рабочие', *days[:-s])
        print('Выходные', *days[-s:])
        break

def d4_1():
    import random
    gr1=('Аб','Дн','Ке','Си','Ле','Жи','Ве','Ба','Гу','Зе')
    gr2=('Еп', 'Уз','Оп','Ан','Ид','Ык','Эо','Юс','Яр','Ой')
    a1=[]
    a2=[]
    a=[]
    a1.append(random.sample(gr1,5))
    a2.append(random.sample(gr2,5))
    a.extend(*a1)
    a.extend(*a2)
    a=tuple(a)
    print('a', *gr1)
    print('a', *gr2)
    print('a', *a)
    print('b', len(a))
    print('d', *sorted(a))
    print('e', 'Иванов' in a)
    print('e', a.count('Иванов)'))