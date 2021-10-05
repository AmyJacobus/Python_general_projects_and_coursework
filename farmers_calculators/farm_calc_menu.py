#!/usr/bin/env python3

"""
DOCSTRING COMES HERE
"""

import break_even_calculator as bc
import cover_crop_calculator as ccc
import stocking_rate_calc as src
import water_allocation_calc as wac

__author__ = 'Ammishaddai Jacobus and Rushandy Andrea'
__version__ = '1.0'
__date__ = 'Oct 6, 2021'
__status__ = 'Development'


LINE_LENGTH = 50


def display_menu():
    """
    DOCSTRING
    :return:
    """

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
    """

    :return:
    """

    while True:
        display_menu()
        command = int(input('Command: '))

        if command == 1:
            bc.break_even_calculator()
        elif command == 2:
            ccc.cover_crop_calculator()
        elif command == 3:
            src.stocking_rate_calculator()
        elif command == 4:
            wac.water_allocation_calculator()
        elif command == 5:
            print('Help Menu')
        elif command == 0:
            break
        else:
            print("Not a valid command. Please try again.\n")

        print()

        print('=' * LINE_LENGTH)
        input('Press any key to continue....')
        print('=' * LINE_LENGTH)


    print("Bye!")

# DOCUMENT IN YOUR OWN WORDS
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
