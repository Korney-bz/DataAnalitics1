class Pet:
    '''домашнее животное'''
    legs = 4
    has_tail = True

    def inspect(self):
        print('Всего ног:', self.legs)
        print('Хвост присутствует -', 'да' if self.has_tail else 'нет')


class Cat(Pet):
    '''кошка - является домашним животным'''

    def sound(self):
        print('мяу!')


class Dog(Pet):
    '''собака - является домашним животным'''

    def sound(self):
        print('Гав!')


class Hamster(Pet):
    '''Хомячок - является домашним животным'''

    def sound(self):
        print('ЦЦЦЦцццц')


print("Котик")
my_pet = Cat()
my_pet.inspect()
my_pet.sound()

print("Собака")
my_pet = Dog()
my_pet.inspect()
my_pet.sound()

print("Хомячок")
my_pet = Hamster()
my_pet.inspect()
my_pet.sound()
