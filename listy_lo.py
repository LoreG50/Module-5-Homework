if __name__ == "__main__":
    
    food = ['rice', 'beans']
    food.append('broccoli')
    print(food)
    food.extend(['bread', 'pizza'])
    print(food)
    print(food[0:2])
    print(food[4])

    breakfast = ("eggs, fruit, orange juice")
    print(breakfast)
    print(type(breakfast))
    breakfast = breakfast.split(',')
    print(breakfast)
    print(type(breakfast))
    print(len(breakfast))


    number_list = []
    while True:
        inp = input('Enter a number: ')
        if inp == 'stop':
            break
        value = float(inp)
        number_list.append(value)
    average = sum(number_list) / len(number_list)
    print(f'Average: {average}')
    min = min(number_list)
    print(f'Min: {min}')
    max = max(number_list)
    print(f'Max: {max}')
