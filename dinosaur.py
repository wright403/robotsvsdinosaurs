class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 80


    def attack(self, robot):
        robot.health -= self.attack_power
        print(f'{robot.name} was attacked by {self.name} and did {self.attack_power} damage, leaving {robot.name} with {robot.health} health')
    
    
    
