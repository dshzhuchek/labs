def e1():
    x=input('Введите страну ')
    countries={
        "russia" : "moskov",
        "brazil" : "brasilia",
        "france" : "paris",
        "finland" : "helsinki"
    }
    print("a",countries)
    print("b", countries[x])
    print("c", sorted(countries))

def e2():
    ochki={
        1 : ['А','В','Е','И','Н','О','Р','С','Т'],
        2 : ['Д','К','Л','М','П','У'],
        3 : ['Б','Г','Ё','Ь','Я'],
        4 : ['Й','Ы'],
        5 : ['Ж','З','Х','Ц','Ч'],
        8 : ['Ш','Э','Ю',],
        10 : ['Ф','Щ','Ъ',]
    }
    x = input("Введите слово")
    x=list(x)
    d=0
    for i in x:
        for k in ochki:
            if i in ochki[k]:
                d+=k
    print(d)

def e3():
    students={
        'A' : ['eng','rus','spa'],
        'B' : ['eng','rus','chi'],
        'C' : ['rus','eng'],
        'D' : ['chi','rus'],
        'E' : ['rus'],
        'F' : ['eng', 'spa'],
        'J' : ['kaz', 'rus'],
        'H' : ['eng','ita'],
        'I' : ['eng','fra']
    }
    d = []
    c = 0
    k=[]
    for i in students:
        for i in students[i]:
            if i not in d:
                d.append(i)
                c+=1
    for i in students:
        if 'chi' in students[i]:
            k.append(i)
        else:
            continue
    print(d)
    print(c)
    print(sorted(d))
    print(*k)
e1()

