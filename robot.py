from dinosaur import Dinosaur
from weapon import Weapon
class Robot:
    def __init__(self, name):
      self.name = name
      self.health = 80
      self.weapon = Weapon('sword', 30)


    def attack(self, dinosaur): 
        dinosaur.heath -= self.weapon.attack_power
        print(f'{dinosaur.name} was attacked by {self.name} and did {self.weapon.attack_power} damage, leaving {dinosaur.name} with {dinosaur.heath} health remaining')