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
        user_input = input(f'{prompt} greater than or equal to {limit}: ')

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
    :return: n/a
    """
    while True:

        value = input(f'{prompt}')
        try:
            value = int(value)
            break
        except ValueError:
            print('That is not a number,enter a number, please')
            continue

def get_string(prompt):

    while True:
        user_input = input(f'{prompt}: ')

        if user_input > '':
            return user_input
        else:
            print(f'Invalid Input: Please enter a value')


# def get_yes_no(prompt):
#
#     while True:
#         if prompt='':
#             user_input = input(f'{prompt} (y=yes | n=no): ').lower()
#         else:
#             user_input = input(f'{prompt=''}') # NEED TO FINISH THIS ONE - BIG ERROR
#
#         if user_input in []:
#             return True
#         elif user_input in []:
#             return False
#         else:
#             print('Invalid Input: Please enter a y=yes, n=no')

def main():
    """
    This is the main function, used to test each function in this module separately in a while loop.
    :return: n/a
    """
    # choice = "y"
    # while choice.lower() == "y":
    #     # TO TEST FUNCTION get_range()
    #     # get input
    #     # valid_number = get_range(prompt="Enter float", low=0, high=1000, data_type='float')
    #     # print("Valid number = ", valid_number)
    #     # print()
    #     # valid_number = get_range(prompt="Enter int", low=0, high=1000, data_type='int')
    #     # print("Valid integer = ", valid_number)
    #     # print()
    #
    #     # TEST FUNCTION get_positive()
    #     # # get input
    #     # valid_number = get_positive(prompt="Enter a number greater than ", limit=0, data_type='int')
    #     # print("Valid number = ", valid_number)
    #     # print()
    #
    #     # TEST FUNCTION get_num()
    #     # Get input
    #     # get_num()
    #
    #     # see if the user wants to continue
    #     choice = input("Repeat? (y/n): ")
    #     print()
    #
    # print("Bye!")


if __name__ == "__main__":  # Basically if the name of the module is equal to main
    main()  # Run this specific program.