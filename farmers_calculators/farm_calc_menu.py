#!/usr/bin/env python3

"""
Programmer: Ammishaddai Jacobus
Date: Oct 6, 2021, 2021
Description: This is a menu application, which lets the user pick 4 different farm calculators to do different
calculations related to farming.
"""

import break_even_calculator as bc # This imports the break even calculator module and assign it the namespace of bc
import cover_crop_calculator as ccc # This imports cover_crop_calculator module and assign it the namespace of ccc
import stocking_rate_calc as src # This imports stocking_rate_calc module and assign it the namespace of src
import water_allocation_calc as wac # This imports water_allocation_calc module and assign it the namespace of wac

#Authorship metadata
__author__ = 'Ammishaddai Jacobus and Rushandy Andrea'
__version__ = '2.0'
__date__ = 'Oct 6, 2021'
__status__ = 'Development'


LINE_LENGTH = 50 # ling length, declared here to be used all over the program when needed


def display_menu():
    """
    This function displays the menu, also displays the different calculator options for the user. Allows them to choose
    from a menu option. Has options from 0-5, 4 calculator options, help option (that display the menu again) and a
    exit program option. It imports calculator modules to run the program.
    :return: n/a
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
    This function calls the function display_menu
    Takes the user input, makes it an integer.
    Also runs the if, elif, else code to call verify the user's command input and call the calculator asigned to that
    command. If they choose 0, it will exit the application completely, if they choose 5, it will open the help menu
    again for them.

    It also asks the user after the new opened calculator has completed it's cycle if they want to press any key
    to continue to the original menu to choose another calculator or exit the program.
    :return: n/a
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


if __name__ == "__main__":  # Basically if the name of the module is equal to main
    main() # Run this specific program.


