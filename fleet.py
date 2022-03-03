from robot import Robot
class Fleet:
    def __init__(self):
        self.fleet_list = []
        self.create_fleet()

    def create_fleet(self):
        first_robot = Robot("James")
        second_robot = Robot("Nevin")
        third_robot = Robot("Megan")
        self.fleet_list.append(first_robot)
        self.fleet_list.append(second_robot)
        self.fleet_list.append(third_robot)

      
