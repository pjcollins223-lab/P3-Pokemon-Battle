# Jason Marks 
# Creating the Move classes for the Pokemon 

import random


class Move:
    """
    Blueprint for a Move object.
    Every move has a name, a type, and a damage range.
    """
    def __init__(self, move_name, elemental_type, low_attack_points, high_attack_points):
        self.move_name = move_name
        self.elemental_type = elemental_type
        self.low_attack_points = low_attack_points
        self.high_attack_points = high_attack_points

    def get_info(self):
        # Returns a formatted string describing this move
        return f"{self.move_name} (Type: {self.elemental_type}): {self.low_attack_points} to {self.high_attack_points} Attack Points"

    def generate_attack_value(self):
        # Returns a random integer between low and high (both ends inclusive)
        return random.randint(self.low_attack_points, self.high_attack_points)
