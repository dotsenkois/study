class animal:
    instance_ref = []


    def __init__(self, name, weight, voice):

        animal.instance_ref.append(self)
        self.__name = name
        self.__weight = weight
        self.__voice = voice

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, w):
        if w > 0:
            self.__weight = w
        else:
            raise ValueError

    @property
    def voice(self):
        return self.__voice

    @voice.setter
    def voice(self, v):
        self.__voice = v

    def feed(self,food_weight):
        self.__weight+=1
        print(f'{self.name} покушола и весит {self.__weight}')

    def say_something(self):
        print(self.__voice)

class milk_animals(animal):
    def __init__(self, name, weight, voice, milk):
        super().__init__(name, weight, voice)
        self.milk = milk

    def milking(self):
        self.milk-=1
        print(f'{self.name} подоилась и молока осталось - {self.milk}')

class birds(animal):
    def __init__(self, name, weight=1, voice='', eggs=20):
        super().__init__(name, weight, voice)
        self.__eggs = eggs

    def give_eggs(self,they_took_our_childeren =1):

        if self.__eggs >= they_took_our_childeren >= 0:
            self.__eggs -= they_took_our_childeren
            print(f'Забрали {they_took_our_childeren} яиц. Яиц осталось - {self.__eggs}')
        else:
            print('Столько яиц нет')

class wooling(animal):
    def __init__(self, name, weight, voice, is_sheared = False):
        super().__init__(name, weight, voice)
        self.is_sheared = is_sheared

    def shearing(self):
        self.say_something()
        if self.is_sheared == False:
            print('Ух, много шерсти сострижем!')
            self.is_sheared = True
        else:
            print('Нечего стричь...')

goose1 = birds('Серый', 10, 'гагагага',0)
goose2 = birds('Белый', 12, 'тегатега',0)

cow1 = milk_animals('Манька', 200, 'Муууууу',10)

sheep1 = wooling('Барашек', 21, 'бееее',False)
sheep2 = wooling('Кудрявый', 22, 'бебебе',True)

sheep1.shearing()

chiken1 = birds('Ко-Ко', 3, 'кококо',10)
chiken2 = birds('Кукареку', 5, 'кукареку',0)

goat1 = milk_animals('Рога', 15, 'Мееееее',2)
goat2 = milk_animals('Копыта', 12, 'меме',3)

duck = birds('Кряква', 3, 'кря-кря',5)

duck.say_something()
sheep1.say_something()
cow1.say_something()

chiken2.feed(1)
chiken1.feed(1)

duck.give_eggs(5)

total_weight = sum([a.weight for a in animal.instance_ref])
print('Вес всех животных составляет {}'.format(total_weight))

max_weight = -1
for a in animal.instance_ref:
    if a.weight > max_weight:
        max_weight = a.weight
        biggest_animal = a.name

print('Больше всего весит {}'.format(biggest_animal))
