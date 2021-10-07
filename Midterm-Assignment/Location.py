

import random


def current_location_bs():
    location_random_list = ['Nebraska', 'Florida', 'General USA', 'New York', 'Outside USA']
    random.shuffle(location_random_list)
    print(location_random_list)

    print()
    print(f'Your current location is {location_random_list[1]}')
    print()

    if location_random_list[1] == 'Nebraska':
        base_rate = 70
    elif location_random_list[1] == 'Florida':
        base_rate = 80
    elif location_random_list[1] == 'General USA':
        base_rate = 88
    elif location_random_list[1] == 'New York':
        base_rate = 90
    elif location_random_list[1] == 'Outside USA':
        base_rate = 100

    print(f'Your base rate is: {base_rate}')

def main():
    current_location_bs()

if __name__ == "__main__": # Basically if the name of the module is equal to main
      main()