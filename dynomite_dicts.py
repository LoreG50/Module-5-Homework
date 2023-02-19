if __name__ == "__main__":
    

    pokedex = {}
    pokemon_types = (('Venosaur', ['Grass', 'Poisen']), ('Charizard', ['Fire', 'Flying']), ('Blastoise', ['Water']))
    pokedex = dict(pokemon_types)
    print(pokedex)
    del(pokedex['Blastoise'])
    print(pokedex)
    