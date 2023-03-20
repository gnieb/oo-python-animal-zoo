import ipdb

class Animal:
    #keep track of all animal instances
    all = []

    def __init__(self, nickname, weight, species, zoo_instance ):
        self.nickname = nickname
        self.weight = weight
        self.species = species
        self.zoo = zoo_instance
        Animal.all.append(self)
       
    @classmethod
    def find_by_species(self, species):
        species_list = []
        for animal in Animal.all:
            if animal.species == species:
                species_list.append(animal.nickname)

        print(species_list)





######### Questions ###########
# how to make the name and species unable to change??? I thought that  ._ was only for properties so... should this be made into a property? 