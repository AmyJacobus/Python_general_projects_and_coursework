#!/usr/bin/env python3


"""
Programmers: Ammishaddai Jacobus
Date: Dec 16, 2021
Description: This is the validation, basically it validates the user input
"""


# Authorship information # Done by Amy
__author__ = 'Ammishaddai Jacobus'
__version__ = '1.0'
__date__ = 'NEED TO BE DONE'
__status__ = 'Development'


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
