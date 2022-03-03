class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 80


    def attack(self, robot):
        self.attack_power -= 10
        
