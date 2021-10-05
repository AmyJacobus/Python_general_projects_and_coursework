#!/usr/bin/env python3

"""
Programmer: Ammishaddai Jacobus
Date:
Description: This program will help determine how many cow-calf pairs a pasture can support per acre of forage.
This program is based on the following reference: https://www.wikihow.com/Calculate-Stocking-Rates-for-Your-Pastures
"""

# Authorship information
__author__ = 'Ammishaddai Jacobus'
__version__ = '1.0'
__date__ = 'Sept 12, 2021'
__status__ = 'Development'


def stocking_rate_calculator():
    """
    DOCSTRING
    :return:
    """

    # Welcome message to user
    print()
    print('            Stocking Rate Calculator vrs.2021')
    print('To make use of this calculator, you will need the following data:')
    print('(1) The amount of forage samples taken, (2) The amount of grams for each dry clipping.')
    print('(3) The utilization rate, and (4), the animal unit month.')
    print()
    print('*' * 100)
    print()

    # While loop to ask for forage samples taken
    while True:

        forage_sample = int(input("Please enter the # of forage samples taken (Valid 1-20): "))
        if forage_sample in range(1, 21):  # Stars at 1, finish at 21, 21 will not count (1-20)
            break  # gets out of the loop here if the statement is true
        else:   # otherwise it will print out the error, and start the while loop again
            print("Invalid Value! Please type in a number between 1 and 20")
    # While loop ends here

    # Output instruction message to user
    print()
    print('*' * 100)
    print()
    print('Please type in per every sample dry clipping in grams.')

    # For loop to get the number of each and every input from user, about the dry grass in grams
    sample_total = 0
    for i in range(forage_sample):
        sample_total += int(input(f'Type in the total grams for sample # {i+1}: '))

    # Calculations for the average in pounds and per acre
    square_foot_avg_pounds = round((sample_total / forage_sample) / 453.592, 3)
    forage_per_acre = round(square_foot_avg_pounds * 43560)

    # Output square foot average per round and forage per acre
    print()
    print(f'Square foot avg per round = {square_foot_avg_pounds}')
    print(f'Forage per acre in pounds = {forage_per_acre} lbs.')
    print()

    # While loop to take user input for the utilization rate
    while True:
        utilization_rate_input = int(input('Please enter the utilization rate (Valid 1-100): '))
        if utilization_rate_input in range(1, 101):
            print()
            break
        else:
            print('Invalid Value! Please type in a number between 1 and 100.')
    # While loop ends here

    # While loop to take user input of AUM
    while True:
        animal_unit_month = int(input('Please enter the animal unit month, anywhere from 1 to 2000 (.lbs): '))
        if animal_unit_month in range(1, 2001):
            print()
            break
        else:
            print('Invalid Value! Please type in a number between 1 and 2000.')
    # While loops ends here

    # Calculate the stocking rate and print the stocking rate result for the user
    print('*' * 100)
    stocking_rate = round(forage_per_acre * (utilization_rate_input / 100) / animal_unit_month, 2)
    print()
    print(f'The stocking rate (cow-calf per acre) is: {stocking_rate}')

    # Goodbye message to user
    print()
    print('Thank you for making use of the stocking rate calculator.')
    print()
    print('*' * 100)
    print()

    # CODE IN YOUR OWN WORDS
    if __name__ == "__main__":
        stocking_rate_calculator()
