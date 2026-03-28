#Porter Collins
#Part 2: Creating the Pokemon objects for P3 Pokemon Battle (Team Project)

def create_pokemon() :
    lstPokemon = []
    oBulbasaur = Pokemon("Bulbasaur", "Grass", 60)
    oCharmander = Pokemon("Charmander", "Fire", 55)
    oSquirtle = Pokemon("Squirtle", "Water", 65)

    print(oCharmander.get_info())
    oCharmander.heal()
    print(oCharmander.get_info())

    lstPokemon.append(oBulbasaur)
    lstPokemon.append(oCharmander)
    lstPokemon.append(oSquirtle)

    for pokemon in lstPokemon :
        print(pokemon.get_info)()
