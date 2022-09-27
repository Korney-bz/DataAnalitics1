from random import randint

from termcolor import cprint


class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return (
            'Я - {}, '
            'Сытость - {}'.format(self.name, self.fullness))

    def eat(self):
        if self.house.food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 10
            self.house.food -= 10
        else:
            print('{} нет еды'.format(self.name))

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='cyan')
        self.house.money += 100
        self.fullness -= 10

    def watchtv(self):
        cprint('{} смотрит телевизор'.format(self.name), color='green')
        self.fullness -= 15

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='white')
            self.house.money -= 50
            self.house.food += 50
        else:
            print('{} деньги закончились'.format(self.name))

    def go_in_to_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} заехал в дом'.format(self.name), color='green')

    def act(self):
        if self.fullness <= 0:
            cprint('{} ПОТРАЧЕНО!'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watchtv()


class House:
    def __init__(self):
        self.food = 10
        self.money = 50

    def __str__(self):
        return 'В дома осталось еды {}, Денег осталось {}'.format(self.food, self.money)


beavis = Man(name='Бивис')
butthead = Man(name='Батхет')

my_sweet_home = House()

beavis.go_in_to_house(house=my_sweet_home)
butthead.go_in_to_house(house=my_sweet_home)

for day in range(1, 21):
    cprint('================== день {} ================='.format(day), color='yellow')
    beavis.act()
    butthead.act()
    print('-------------------------')
    print(beavis)
    print(butthead)
    print(my_sweet_home)
