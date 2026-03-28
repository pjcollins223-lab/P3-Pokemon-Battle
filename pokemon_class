#Juliana Merkley
#code to implement the pokemon class that the pokemon objects will be created as
#this should be moved to one main program when we're all done so it runs right

class Pokemon:
    #for pokemon objects
    def __init__(self, name, elemental_type, hit_points):
        self.name = name
        self.elemental_type = elemental_type
        self.hit_points = hit_points

    #return info on individual pokemon
    def get_info(self):
        return f"{self.name} - Type: {self.elemental_type} - Hit Points: {self.hit_points}"

    #healing function
    def heal(self):
        self.hit_points += 15
        print(f"{self.name} has been healed to {self.hit_points} hit points.")