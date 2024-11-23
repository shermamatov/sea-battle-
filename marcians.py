import random
import os

locations = [random.randint(1, 7) for i in range(3)]
weights = [269, 333, 111]

def clear_console():
    if os.name == 'nt':  
        os.system('cls')
    else: 
        os.system('clear')

# print(locations)

while True: 
    guesses_locations = list(map(int, input("Enter 3 number of kilometers: ").split()))
    
    if guesses_locations == locations and sum(weights) == 713:
        print('You find your Cargo')
        break
    else :
        locations = [random.randint(1, 7) for _ in range(3)]
        clear_console()
        print('Wrong locations, your cargo carried to another place, try again')


