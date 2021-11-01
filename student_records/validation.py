#!/usr/bin/env python3


"""
Programmers: Ammishaddai Jacobus
Date: October 31, 2021
Description:Description: This module is used to validate several inputs in different modules and functions. It validates
user input range, positive number input, number input, string input and yes/no input and if they do not input the
right value or data type, outputs an error message and asks the user to try again.
"""


# Authorship
__author__ = 'Ammishaddai Jacobus'
__version__ = '1.0'
__date__ = 'Oct 31, 2021'
__status__ = 'Development'


def get_range(prompt, low, high, data_type='int'):
    """
    This function prompts a message to the user, takes the user input, checks if its a float or an integer, and if
    the number is higher than the low variable and less or equal to the high variable, it will return a number, other-
    wise it will output a message to the user, to let them known that the integer range that they should input, and
    because of a while loop, it will loop until the meets the requirements.
    :param prompt: Ask the user for input, with a message
    :param low: paramater to store in the low number in the range
    :param high: paramter to store in the high number in the range
    :param data_type: this paramater is set to int
    :return: number
    """

    while True:
        user_input = input(f'{prompt} (Range = {low}-{high}): ')

        try:
            if data_type == 'int':
                number = int(user_input)
            else:
                number = float(user_input)

            if number > low and number <= high:
                return number
            else:
                print("Entry must be greater than", low,
                      "and less than or equal to", high)

        except ValueError:
            print('Invalid Input: Please enter a positive number')


def get_positive(prompt, limit, data_type='int'):
    """
    This function takes user input and check if it meets the int data type, if the int is bigger than a certain limit
    otherwise it will tell the user that the number cannot be below 0, basically to try again, it will continue to ask
    the user, until they enter the correct int, based on the requirement of positive number, and the use of a while
    loop.
    :param prompt: Prompts the user for a message
    :param limit: this parameters outputs the limit
    :param data_type: data type is set to int, to verify if user input is a integer or not
    :return: number
    """

    while True:
        user_input = input(f'{prompt} must be greater than [{limit}]: ')

        if data_type == 'int':
            number = int(user_input)
        else:
            number = float(user_input)

        if number > limit:
            return number
        else:
            print(f'The number cannot be below {limit}')


def get_num(prompt):
    """
    This function checks if the user has typed in a number or not, and does this by using a try and except valueError.
    :param prompt: Here to take in the user input
    :return: n/a
    """
    while True:

        value = input(f'{prompt}: ')
        try:
            value = int(value)
            break
        except ValueError:
            print('That is not a number,enter a number, please')
            continue


def get_string(prompt):
    """
    This function basically checks if the user has typed in a value or not.
    :param prompt:
    :return: It returns user_input back to the main program so other functions can make use of it.
    """
    while True:
        user_input = input(f'{prompt}: ')

        if user_input > '':
            return user_input
        else:
            print(f'Invalid Input: Please enter a value.')


def get_yes_no(prompt):
    """
    This function checks if the user types in a yes or not, otherwise it will tell the user that there it outputs
    a message telling the user that they should type in a yes or no.
    :param prompt: Here so you can call this function, add a string for input
    :return: True or False, to be used by the while loop
    """

    while True:
        choice = input(f'{prompt}').lower()
        if choice in ['yes', 'y', 'n', 'no']:
            return choice
        else:
            print('There has been an error, please type in a yes or no')


def main():
    """
    This is the main function where you can call different of these functions to use them, or since this is a validation
    module, to test them.
    :return: n/a
    """
    get_num(prompt='Type in a number: ')
    get_string(prompt='Please type in a string: ')


if __name__ == "__main__":  # Basically if the name of the module is equal to main
    main()  # Run this specific program.


