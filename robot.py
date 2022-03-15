
from weapon import Weapon
class Robot:
    def __init__(self, name):
      self.name = name
      self.health = 100
      self.weapon = Weapon('sword', 50)


    def attack(self, dinosaur): 
        dinosaur.health -= self.weapon.attack_power
        print(f'{dinosaur.name} was attacked by {self.name} and did {self.weapon.attack_power} damage leaving {dinosaur.name} with {dinosaur.health} health')
    
       