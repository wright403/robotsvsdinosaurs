
from herd import Herd
from fleet import Fleet

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
      
        
        

    def run_game(self):
        self.display_welcome()
        self.battle()
        self.dino_turn = []
        self.robo_turn = []
        


    



    def display_welcome(self):
        print("welcome to rvd")


    
    def battle(self):
        while (self.fleet.fleet_list != [] and self.herd.herd_list != []):
            self.chosen_dinosaur_index = self.show_dino_opponent_options
            self.chosen_robot_index = self.show_robo_opponent_options
            self.dino_turn(self.chosen_dinosaur_index)
            self.robo_turn(self.chosen_robot_index)

       
          
          
        

    def dino_turn(self, dinosaur):
        self.herd.herd_list [dinosaur].attack (self.fleet.fleet_list[self.chosen_robot_index])
        if (self.fleet.fleet_list[self.chosen_robot_index].health <= 0):
            self.fleet.fleet_list.remove(self.chosen_robot_index)
            
            # remove from self.fleet.fleet_list[chosen_robo_index]
    
    def robo_turn(self,robot):
        self.fleet.fleet_list[robot].attack(self.herd.herd_list[self.chosen_dinosaur_index])
        if (self.herd.herd_list[self.chosen_dinosaur_index].healh <= 0):
            self.herd.herd_list.remove(self.chosen_dinosaur_index)
            

        

    def show_dino_opponent_options(self):
        print(f'press 0 to select {self.herd.herd_list[0].name}')
        print(f'press 1 to select {self.herd.herd_list[1].name}')
        print(f'press 2 to select {self.herd.herd_list[2].name}')
        self.chosen_dinosaur_index = input("Choose your dino: ")
        

    def show_robo_opponent_options(self):
        print(f'press 0 to select {self.fleet.fleet_list[0].name}')
        print(f'press 1 to select {self.fleet.fleet_list[1].name}')
        print(f'press 2 to select {self.fleet.fleet_list[2].name}')
        self.chosen_robot_index = input('choose your robo:')
        
        



    def display_winner(self):
        pass







    
# self.fleet.fleet_list[0].attack(self.herd.herd_list[0])    