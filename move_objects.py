# Sarah Walker
# creating move objects with the class Move and randomly choosing objects to display info for

import random
import move_classes as mc

# create 9 move objects
def create_moves () :
    move1 = mc.Move("Tackle", "Normal", 5, 20)
    move2 = mc.Move("Quick Attack", "Normal", 6, 25)
    move3 = mc.Move("Slash", "Normal", 10, 30)
    move4 = mc.Move("Flamethrower", "Fire", 5, 30)
    move5 = mc.Move("Ember", "Fire", 10, 20)
    move6 = mc.Move("Water Gun", "Water", 5, 15)
    move7 = mc.Move("Hydro Pump", "Water", 20, 25)
    move8 = mc.Move("Vine Whip", "Grass", 10, 25)
    move9 = mc.Move("Solar Beam", "Grass", 18, 27)

    # store in list
    lstMoves = [
                move1, move2, move3, 
                move4, move5, move6, 
                move7, move8, move9
               ]
    
    # print the information for 3 random moves
    for index in range(0, 3, 1) :
        inList = False
        while not inList :
            rand_num = random.randrange(0,len(lstMoves)) 
            inList = True
            print(lstMoves[rand_num].get_info())
            print(f"Generated attack value: { lstMoves[rand_num].generate_attack_value()}")
            lstMoves.pop(rand_num)

    input("Press enter to continue...")
        
