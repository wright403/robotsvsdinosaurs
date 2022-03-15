

from herd import Herd
from fleet import Fleet

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
      
        
        

    def run_game(self):
        self.display_welcome()
        self.battle()
        self.display_winner()
        
        
        
        
    
        


    



    def display_welcome(self):
        print("welcome to rvd")


    
    def battle(self):
        while len(self.fleet.fleet_list) > 0 and  len(self.herd.herd_list) > 0:
            if len(self.fleet.fleet_list) > 0:
                self.robo_turn()
            elif len(self.herd.herd_list) > 0:
                self.dino_turn()
            else:
                self.display_winner()   


            
            
                
            

       
          
          
        

    def dino_turn(self,):
        self.show_dino_opponent_options()
        chosen_dinosaur_index = int(input(f'pick a dinosaur '))
        print('this dinosaur will attack')
        self.show_robo_opponent_options()
        chosen_robot_index = int(input(f'pick a robot '))
        print('this robot will defend itself')
        self.herd.herd_list [chosen_dinosaur_index].attack (self.fleet.fleet_list[chosen_robot_index])
        if (self.fleet.fleet_list[chosen_robot_index].health <= 0):
            print(f'{self.fleet.fleet_list[chosen_robot_index].name} has been defeated')
            self.fleet.fleet_list.remove(self.fleet.fleet_list[chosen_robot_index])
            
            # remove from self.fleet.fleet_list[chosen_robo_index]
    
    def robo_turn(self,):
        self.show_robo_opponent_options()
        chosen_robot_index = int(input(f'pick a robot '))
        print('this robot will attack')
        self.show_dino_opponent_options()
        chosen_dinosaur_index = int(input(f'pick a dinosaur '))
        print('this dinosaur will defend itself')
        self.fleet.fleet_list[chosen_robot_index].attack(self.herd.herd_list[chosen_dinosaur_index])
        if (self.herd.herd_list[chosen_dinosaur_index].health <= 0):
            print(f'{self.herd.herd_list[chosen_dinosaur_index].name} has been defeated')
            self.herd.herd_list.remove(self.herd.herd_list[chosen_dinosaur_index])
            

        

    def show_dino_opponent_options(self):
        index = 0
        for dinosaur in self.herd.herd_list:
          print(f'press {index} to select {dinosaur.name}')
          index += 1
          
    def show_robo_opponent_options(self):
        index = 0
        for robot in self.fleet.fleet_list:
         print(f'press {index} to select {robot.name}')
         index += 1
         
         

    def display_winner(self):
        if len(self.fleet.fleet_list) > len(self.herd.herd_list):
            print('robots win')
        else:
            print('dinosaurs win')    
          
        







    
# self.fleet.fleet_list[0].attack(self.herd.herd_list[0])    