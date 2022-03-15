from dinosaur import Dinosaur
class Herd:
    def __init__(self):
        self.herd_list = []
        self.create_herd()

    def create_herd(self):
        first_dinosaur = Dinosaur('niko the dinosaur',50)
        second_dinosaur = Dinosaur('daisy the dinosaur',50)
        third_dinosaur = Dinosaur('thor the dinosaur',50)
        self.herd_list.append(first_dinosaur)
        self.herd_list.append(second_dinosaur)
        self.herd_list.append(third_dinosaur)






