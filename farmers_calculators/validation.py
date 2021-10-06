#!/usr/bin/env python3

"""
Programmer: Ammishaddai Jacobus
Date: Oct 06, 2021
Description: This validation module consinsts of 3 different functions:
get_range: To be able to validate if the user's input is between the two ranges allowed
get_positive: To see if the user's input is a positive numbers or not
get_num: To see if the user has input a number at all or not
"""


# Authorship information
__author__ = 'Ammishaddai Jacobus'
__version__ = '2.0'
__date__ = 'Oct 6, 2021'
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

        if data_type == 'int':
            number = int(user_input)
        else:
            number = float(user_input)

        if number > low and number <= high:
            return number

        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high)


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
        user_input = input(f'{prompt} greater than or equal to {limit}: ')

        if data_type == 'int':
            number = int(user_input)
        else:
            number = float(user_input)

        if number > limit:
            return number
        else:
            print(f'The number cannot be below {limit}')


def get_num():
    """
    This function checks if the user has typed in a number or not, and does this by using a try and except valueError.
    :return: n/a
    """
    while True:

        value = input('Write a number: ')
        try:
            value = int(value)
            break
        except ValueError:
            print('That is not a number,enter a number, please')
            continue


def main():
    choice = "y"
    while choice.lower() == "y":
        # TO TEST FUNCTION get_range()
        # get input
        # valid_number = get_range(prompt="Enter float", low=0, high=1000, data_type='float')
        # print("Valid number = ", valid_number)
        # print()
        # valid_number = get_range(prompt="Enter int", low=0, high=1000, data_type='int')
        # print("Valid integer = ", valid_number)
        # print()

        # TEST FUNCTION get_positive()
        # # get input
        # valid_number = get_positive(prompt="Enter a number greater than ", limit=0, data_type='int')
        # print("Valid number = ", valid_number)
        # print()

        # TEST FUNCTION get_num()
        # Get input
        # get_num()

        # see if the user wants to continue
        choice = input("Repeat? (y/n): ")
        print()

    print("Bye!")


if __name__ == "__main__":  # Basically if the name of the module is equal to main
    main()  # Run this specific program.
