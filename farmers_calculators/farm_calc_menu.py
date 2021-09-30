#!/usr/bin/env python3

LINE_LENGTH = 50


def display_menu():

    print()
    print('The Farmers calculators')
    print('=' * LINE_LENGTH)
    print("COMMAND MENU")
    print('1 - Break even calculator')
    print('2 - Cover crop calculator')
    print('3 - Stocking rate calculator')
    print('4 - Water allocation calculator')
    print('5 - Help')  # This is so it can display the DOCSTRING
    print('0 - Exit program')
    print()


def main():

    while True:
        display_menu()
        command = int(input('Command: '))

        if command == 1:
            print('break_even_calculator')
        elif command == 2:
            print('cover_crop_calculator')
        elif command == 3:
            print('stocking_rate_calculator')
        elif command == 4:
            print('water_allocation_calculator')
        elif command == 5:
            print('Help Menu')
        elif command == 0:
            break
        else:
            print("Not a valid command. Please try again.\n")

        print()

    print("Bye!")


if __name__ == "__main__":
    main()

# Add a menu for all of the farm calculators named farm_calc_menu.py
# Include a menu option to display docstrings for farm_calc_menu.py
# All imports need to be in the default or named local namespace
# Modify farm calculating modules to be able to be called by a function
#
# Add a validation.py module (Example: solutions\ch04\validation.py)
# get_range(prompt, low, high, data_type='int')
# get_positive_num(prompt, data_type='int')
# get_num(prompt, data_type='int')
# All calculators should use the validation.py functions for data validation
#
# All modules should check if they are the starting point and if so run the appropriate calculator
# Use global constant variable, and named arguments where appropriate
# Add docstrings & authorship attributes (meta data)
