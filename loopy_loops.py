
if __name__ == "__main__":

    pokemon = 'picachu', 'charmander', 'bulbasaur'
    print(pokemon[1])
    starter1, starter2, starter3 = pokemon
    print(pokemon)
    print(starter1)
    print(starter2)
    print(starter3)


    name_tuple = tuple('Lorena')
    print(name_tuple)
    print('i' in name_tuple)


    for i in range(2, 11):
        print(i)


    numbers = ('2', '3', '4', '5', '6', '7', '8', '9','10')
    i = 0
    while i < len(numbers):
        print(numbers[i])
        i += 1


    simple_string = ('This is a simple string')
    for string in simple_string:
        print(string)


    simple_set = ('this', 'is', 'a', 'simple', 'set')
    for string in simple_set:
        for string in simple_set:
            for string in simple_set:    
                print(string)

    
        
        

  