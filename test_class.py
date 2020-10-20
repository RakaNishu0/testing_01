# class & method

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} unit generated.".format(name))
        print("hp: {0}, damage: {1}".format(hp, damage))

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 공격ㅇㅇ. [공격력: {self.damage}]")


marine1 = Unit("marine", 40, 5)
marine1.attack("3시")
