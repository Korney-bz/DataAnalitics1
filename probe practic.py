from random import randint

from termcolor import cprint


class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.food = 50
        self.money = 0

    def __str__(self):
        return (
            'Я - {}, '
            'Сытость - {}, '
            'Осталось еды - {}, '
            'Осталось денег - {}'.format(self.name, self.fullness, self.food, self.money))

    def eat(self):
        if self.food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 10
            self.food -= 10
        else:
            print('{} нет еды'.format(self.name))

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='grey')
        self.money += 50

    def play_APEX(self):
        cprint('{} играет в Apex Legends'.format(self.name), color='green')
        self.fullness -= 15

    def shopping(self):
        if self.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='white')
            self.money -= 50
            self.food += 50
        else:
            print('{} деньги закончились'.format(self.name))

    def act(self):
        if self.fullness <= 0:
            print('{} еды нет, Вася отъехать может'.format(self.name))
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.food < 10:
            self.shopping()
        elif self.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play_APEX()


dima = Man(name='Dima')
for day in range(1, 21):
    cprint('================== день {} ================='.format(day), color='yellow')
    dima.act()
    print(dima)
