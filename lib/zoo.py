from lib.animal import Animal
import ipdb
#zoo needs to know about animals that are created and keep track of them 

class Zoo:
    #keeps track of all zoo instances
    all = []

    def __init__(self, name:str, location):
        self.name = name
        self.location = location
        Zoo.all.append(self)

# can put the property decorator up there... this makes it so that we don't need to invoke the method, because this is now a proprty attribute.

    @property
    def animals(self):
        animal_list = []
        for animal in Animal.all:
           if animal.zoo == self:
               animal_list.append(animal)
        return animal_list
    ######## OR ###########
    #  return [a for a in Animal.all if a.zoo == self]
    
    # decorator?? @property
    #what is the list keyword??
    # need a UNIQUE LIST => SET!!!!!!

    def animal_species(self):
        animal_species_set = ([a.species for a in self.animals])
        return list(animal_species_set)
    
    #### OR ######
    # return list({a.species for a in self.animals})
    

    def find_by_species(self, species):
        return [a for a in self.animals if a.species == species ]

    def animal_nicknames (self):
        nickname_list =[]
        for animal in Animal.all:
            if animal.zoo == self:
                nickname_list.append(animal.nickname)
            return nickname_list
    
    @classmethod
    def find_by_location(cls, location):
        return [z for z in cls.all if z.location == location]




# ipdb.set_trace()
