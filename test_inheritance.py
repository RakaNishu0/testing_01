# inheritance

# Normal Unit
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print(f"{self.name}: {location}방향으로 {self.speed}속도로 이동 중")

# AttackUnit:
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 공격함. [공격력: {self.damage}]")

    def damaged(self, hit):
        self.hp = self.hp - hit
        print(f"{self.name} : {hit} 만큼 피해받음. [남은 체력: {self.hp}]")


# HealingUnit:
class HealUnit(Unit):
    def __init__(self, name, hp, speed, heal):
        Unit.__init__(self, name, hp, speed)
        self.heal = heal

    def healing(self, target):
        print(f"{self.name} : {target}을 {self.heal}만큼 치료함")


# Flyable attr:
class Flyable:
    def __init__(self, name, f_speed):
        self.f_speed = f_speed
        self.name = name

    def fly(self, location):
        print(f"{self.name} : {location}방향으로 날아감. [속도: {self.f_speed}]")


# Multi inheritance
class FlyAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, f_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, name, f_speed)
        # super().__init__() <- super()도 상속 대상으로부터 생성자를 가져오지만, 다중상속에선 앞의 1개만 가져오기 때문에 이때에는 사용하지 않는다.
        # 단일 상속의 경우에는 동일하게 사용할 수 있다.

# Method Override
    def move(self, location):
        print(f"{self.name} : {location}방향으로 날아감. [속도: {self.f_speed}]")


marine1 = AttackUnit("marine", 40, 4, 5)
marine1.move("3시")
# marine1.damaged(10)
# medic = HealUnit("medic", 30, 12)
# medic.healing("marine1")
wraith = FlyAttackUnit("wraith", 70, 23, 7)
wraith.move("2시")
