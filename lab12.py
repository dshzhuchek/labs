def g1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print('Имя ресторана: ', self.restaurant_name)
            print('Тип кухни: ', self.cuisine_type)
            print('Рейтинг ', self.rating)

        def open_restaurant(self):
            print('Ресторан открыт!')

        def rating(self,new_rating):
            self.rating = new_rating

    class IceCreamStand(Restaurant):

        def __init__(self, restaurant_name, cuisine_type, rating, flavors):
            super().__init__(restaurant_name, cuisine_type, rating)
            self.flavors = flavors

        def showflavors(self):
            k=1
            print("Сорта мороженого: ")
            for flavor in self.flavors:
                print(k, '.0', flavor)
                k += 1


    restaurant1 = Restaurant('Пекарня', "Выпечка", 4.7)
    restaurant2 = Restaurant("Amur", "Французская", 5)
    restaurant3 = Restaurant('Мак', "ФастФуд", 3.9)
    newIceCreamStand = IceCreamStand('Creamy','Мороженое',5, ['Шоколадное',"Пломбир","Ржаное", "Мятное", "Крем-Брюле"])

    restaurant1.describe_restaurant()
    print('\n')
    restaurant2.describe_restaurant()
    print('\n')
    restaurant3.describe_restaurant()
    print('\n')
    newIceCreamStand.describe_restaurant()
    newIceCreamStand.showflavors()

def g2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print('Имя ресторана: ', self.restaurant_name)
            print('Тип кухни: ', self.cuisine_type)
            print('Рейтинг: ', self.rating)
            print('Местонахождение: ', self.location)
            print('Время работы: ', self.time)

        def open_restaurant(self):
            print('Ресторан открыт!')

        def rating(self,new_rating):
            self.rating = new_rating
    class IceCreamStand(Restaurant):

        def __init__(self, restaurant_name, cuisine_type,flavors, rating, location, time):
            super().__init__(restaurant_name, cuisine_type, rating)
            self.flavors = flavors
            self.location = location
            self.time = time
        def addflavors(self):
            self.flavors.append(input('Введите новый вкус: '))

        def killflavors(self):
            self.flavors.remove(input("Введите вкус, чтобы удалить: "))

        def checkflavor(self):
            if input("Какой сорт интересует? ") in self.flavors:
                print('Такой сорт есть')
            else:
                print('Такого сорта нет')

        def showflavors(self):
            k=1
            print("Сорта мороженого: ")
            for flavor in self.flavors:
                print(k, '.', flavor)
                k += 1
    class palochka(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, rating, location, time, palochka):
            super().__init__(restaurant_name, cuisine_type, rating, location, time)
            self.palochka = palochka
        def palochka(self):
            print('Материал палочки: ', self.palochka)

    class promyagkost(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, rating, location, time, property):
            super().__init__(restaurant_name, cuisine_type, rating, location, time, property)
            self.property=property
        def myagkost(self):
            print('Мягкость мороженого:', self.property)

    ice=IceCreamStand('icee', 'мороженое',["ваниль","шоко","карамель"],"7","NY",'7-10')
    ice.describe_restaurant()
    ice.addflavors()
    ice.killflavors()
    ice.checkflavor()
    ice.showflavors()

    p=promyagkost('icee', 'мороженое',"7","NY",'7-10',"очень мягкое")
    p.myagkost()

def g3():
    import tkinter as tk
    class IceCreamStand:
        def __init__(self):
            self.flavors = ['Ваниль',"Шоко","Карамель","Манго","Киви"]
            self.prices = [1.00 ,2.00 ,3.00 ,4.00 ,5.00]
        def getflavors(self):
            return self.flavors
        def getprices(self):
            return self.prices
    class IceTable:
        def __init__(self, okno):
            self.okno=okno
            okno.title("Стенд с мороженым")

            self.ics = IceCreamStand()
            self.flavors_label = tk.Label(okno, text='Сорта', font = 'Arial 12 bold')
            self.flavors_listbox=tk.Listbox(okno, font='Arial 12', height=len(self.ics.getflavors()))

            for flavor in self.ics.getflavors():
                self.flavors_listbox.insert(tk.END, flavor)

            self.prices_label = tk.Label(okno,text='Цены',font='Arial 12 bold')
            self.prices_listbox=tk.Listbox(okno,font="Arial 12", height=len(self.ics.getprices()))

            for price in self.ics.getprices():
                self.prices_listbox.insert(tk.END, price)

            self.flavors_label.grid(row=0, column=0)
            self.flavors_listbox.grid(row=1, column=0)
            self.prices_label.grid(row=0, column=1)
            self.prices_listbox.grid(row=1, column=1)

    root = tk.Tk()
    i = IceTable(root)
    root.mainloop()
