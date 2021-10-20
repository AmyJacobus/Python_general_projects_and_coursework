#!/usr/bin/env python3

"""
Programmer: Ammishaddai Jacobus
Date: Oct 15, 2021
Description: This module is used to validate several inputs in different modules and functions. It validates the user
input for day of the week, for number input, positive input and range input and lastly their choice input.
"""


# authorship
__author__ = 'Ammishaddai Jacobus'
__version__ = '1.0'
__date__ = 'Oct 15, 2021'
__status__ = 'Development'


def get_dow(prompt):
    """
    THis functions basically validates if the user input is a day of the week or not, if not, it will display an ERROR.
    :param prompt: There to be used by other functions to create a message to ask the user
    :return: n/a
    """
    while True:
        dow = input(f'{prompt}').upper()
        if dow in ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY','SUNDAY']:
            return dow
        else:
            print('Error! Please type in a day of the week.')

def get_num(prompt, data_type='int'):
    """
    A function the makes use of an while to ask the user for input, it checks with the user an if else if the user
    has inserted an integer or a float, if not, it will tell the user that they must enter a number and try again.
    :param prompt: There to be used by other functions to create a message to ask the user
    :param data_type: assigns the data_type as integer, can be changed once the function is called in other modules.
    :return: user_input.
    """

    while True:

        user_input = input(prompt)

        if data_type == 'int':
            user_input = int(user_input)
            return user_input
        elif data_type == 'float':
            user_input = float(user_input)
            return user_input
        else:
            print("Entry must be a number")


def get_pos(prompt, limit, data_type='int'):
    """
    This function makes use of a while loop to ask the user for their input that it
    has to be a positive number, so cannot be below 0. It makes sure the user input is an integer or a float, and
    it only returns number if the user input is higher than 0. Otherwise it will tell the user that the number cannot
    be below 0 and get them to insert the input again, until they do it right.
    :param prompt: to prompt the user for input in other functions
    :param limit: to be able to assign a limit
    :param data_type: to be able to assign the input a data type
    :return: number
    """

    while True:

        user_input = input(f'{prompt} input must be greater than or equal to {limit}: ')

        if data_type == 'int':
            number = int(user_input)
        else:
            number = float(user_input)

        if number > limit:
            return number
        else:
            print(f'The number cannot be below {limit}')


def get_range(prompt, low, high, data_type='int'):
    """
    THis function uses a while loop to check if they user has input a number between a certain low and high, other
    it will display an error and exit the program.
    :param prompt:
    :param low:
    :param high:
    :param data_type:
    :return:
    """
    while True:
        user_input = input(f'{prompt} (Range = {low}-{high}): ')

        if data_type == 'int':
            number = int(user_input)
        else:
            number = float(user_input)

        if number >= low and number <= high:
            return number

        else:
            print("ERROR")
            exit()


def get_choice(prompt):
    """
    This function validates if the user has input, yes, y, n, or no, makes it all lowercase, and returns choice to the
    main program to be used by other functions later. If not it will tells the user that there has been an error, that
    they have not inserted yes or no, and to try again.
    :param prompt: to be used to write a message for input when calling this function in other modules/functions.
    :return: choice
    """

    while True:
        choice = input(f'{prompt}').lower()
        if choice in ['yes', 'y', 'n', 'no']:
            return choice
        else:
            print('There has been an error, please type in a yes or no')


def main():
    print('WE USE THIS TO TEST')


if __name__ == "__main__": # Basically if the name of the module is equal to main
      main()  # It calls mains
