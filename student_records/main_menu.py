#!/usr/bin/env python3


"""
Programmers: Ammishaddai Jacobus
Date: October 31, 2021
Description: This is the main that runs different functions from the module students_mtnc. It basically displays a menu
to the user, and they can choose from 5 different options, add, delete, update, or list students, or exit the program.
"""


import validation as v  # Imports validation.py as v, so you can use functions from the validation module
import student_mtnc as sm  # Imports validation.py as sm, so you can use functions from the student_mtnc module


# Authorship
__author__ = 'Ammishaddai Jacobus'
__version__ = '1.0'
__date__ = 'Oct 31, 2021'
__status__ = 'Development'


def display_menu():
    """
    Display menu to the user.
    :return: n/a
    """
    print()
    print('Student Menu')
    print('='*50)
    print('1 - List all students')
    print('2 - Add a student')
    print('3 - Delete a student')
    print('4 - Update a student')
    print('0 - Exit program')
    print()


def main():
    """
    This function basically runs different functions from the validation module and the student_mtnc module, in a while
    loop, until the user decided that they no longer want to continue to use the program and exit.
    :return: n/a
    """

    students = []  # start empty
    next_student_id = 1  # Starting student ID at 1

    while True:

        display_menu()

        command = v.get_range(prompt='Please enter a Menu #(Valid 0-4)', low=-1, high=4, data_type='int')
        if command == 1:
            sm.list(students)
        elif command == 2:
            sm.add(students, next_student_id)
            next_student_id += 1
        elif command == 3:
            sm.delete(students)
        elif command == 4:
            sm.update(students)
        elif command == 0:
            print()
            print('='*50)
            print("You have securely and successfully exited the student record database!")
            exit()
        else:
            print("Not a valid command. Please try again.\n")

        print()
        input('Press Enter to continue...')
        print()


if __name__ == "__main__":  # Basically if the name of the module is equal to main
    main()  # Run this specific program.
