from lib.animal import Animal
import ipdb
#zoo needs to know about animals that are created and keep track of them 

class Zoo:
    #keeps track of all zoo instances
    all = []

    def __init__(self, name, location):
        self.name = name
        self.location = location
        Zoo.all.append(self)
        # self.animal_list = []


    def animals(self):
        animal_list = []
        for animal in Animal.all:
           if animal.zoo == self:
               animal_list.append(animal)
        # print(animal_list)
        return animal_list



# ipdb.set_trace()
