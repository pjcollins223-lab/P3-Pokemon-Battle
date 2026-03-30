#Porter Collins
#Part 2: Creating the Pokemon objects for P3 Pokemon Battle (Team Project)

import pokemon_class as pc

def create_pokemon() :
    lstPokemon = []
    oBulbasaur = pc.Pokemon("Bulbasaur", "Grass", 60)
    oCharmander = pc.Pokemon("Charmander", "Fire", 55)
    oSquirtle = pc.Pokemon("Squirtle", "Water", 65)

    print(oCharmander.get_info())
    oCharmander.heal()
    print(oCharmander.get_info())

    lstPokemon.append(oBulbasaur)
    lstPokemon.append(oCharmander)
    lstPokemon.append(oSquirtle)

    for pokemon in lstPokemon :
        print(pokemon.get_info())
