from herd import Herd
from fleet import Fleet

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()

    def run_game(self):
        self.display_welcome()
# when calling an attack we must identify 1 robot to attack 1 dino
# self.fleet.fleet_list[0].attack(self.herd.herd_list[0])

    def display_welcome(self):
        print("welcome to rvd")