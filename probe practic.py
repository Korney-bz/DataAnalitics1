class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.food = 50
        self.money = 0

    def __str__(self):
        return (
            'Я - {}, Сытость - {}, '
            'Осталось еды - {}, '
            'Осталось денег - {}'.format(self.name, self.fullness, self.food, self.money))

    def eat(self):
        if self.food > 10:
            print('{} поел'.format(self.name))
            self.fullness += 10
            self.food -= 10
        else:
            print('{} нет еды'.format(self.name))

    def work(self):
        print('{} сходил на работу'.format(self.name))
        self.money += 50

    def play_DOTA(self):
        print('{} слил катку обезьяна'.format(self.name))
        self.fullness -= 15

    def sleep(self):
        print('{} выспался'.format(self.name))
        self.fullness -= 15


vasya = Man(name='Vasya')
print(vasya)
vasya.eat()
print(vasya)
vasya.work()
print(vasya)
vasya.play_DOTA()
print(vasya)
vasya.sleep()
print(vasya)
