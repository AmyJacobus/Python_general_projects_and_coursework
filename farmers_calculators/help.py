"""
DOCSTRING
"""

# Imports
import break_even_calculator as bc # This imports the break even calculator module and assign it the namespace of bc
import cover_crop_calculator as ccc # This imports cover_crop_calculator module and assign it the namespace of ccc
import stocking_rate_calc as src # This imports stocking_rate_calc module and assign it the namespace of src
import water_allocation_calc as wac # This imports water_allocation_calc module and assign it the namespace of wac

# Authorship

LINE_LENGTH = 50 # ling length, declared here to be used all over the program when needed

def help_menu():

    while True:
        print()
        print('The Help Menu')
        print('=' * LINE_LENGTH)
        print("COMMAND MENU")
        print('1 - Help for Break even calculator')
        print('2 - Help for Cover crop calculator')
        print('3 - Help for Stocking rate calculator')
        print('4 - Help f0r Water allocation calculator')
        print('5 - Exit help menu')
        print()

        command = int(input('Command: '))

        if command == 1:
            help(bc)
        elif command == 2:
            help(ccc)
        elif command == 3:
            help(src)
        elif command == 4:
            help(wac)
        elif command == 5:
            break
        else:
            print("Not a valid command. Please try again.\n")

        print()

        print('=' * LINE_LENGTH)
        input('Press any key to continue....')
        print('=' * LINE_LENGTH)


    print("Exited the help menu")


if __name__ == "__main__":  # Basically if the name of the module is equal to main
    help_menu() # Run this specific program.