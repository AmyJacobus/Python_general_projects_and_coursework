#!/usr/bin/env python3

import validation as v
import student_mtnc as sm


def display_menu():
    print('Student Menu')
    print('='*50)
    print('1 - List all students')
    print('2 - Add a student')
    print('3 - Update a student')
    print('4 - Delete a student')
    print('0 - Exit program')
    print()


def main():
    students = [] # start empty
    next_student_id = 1  # Starting student ID at 1

    display_menu()
    while True:
        command = v.get_range(prompt='Please enter a Menu #(Valid 0-4): ', low=0, high=4, data_type='int')
        if command == 1:
            sm.list(students)
        elif command == 2:
            sm.add(students, next_student_id)
        elif command == 3:
            sm.delete(students)
        elif command == 4:
            sm.update(students)
        elif command == 0:
            break
        else:
            print("Not a valid command. Please try again.\n")


    enter = input('Press the entre key to continue...')

    print("Bye!")


if __name__ == "__main__":
    main()
