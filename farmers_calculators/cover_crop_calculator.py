#!/usr/bin/env python3

"""
Programmer: Ammishaddai Jacobus
Date: Oct 6, 2021, 2021
Description: This is a crop coverage calculator. It asks the user for the area length, the area width and it seeding
rate. The calculator takes that data, and inserts it into an algorithm and that calculates the crop coverage needed
and outputs the result to the user.
"""

import validation as v  # importing the module validation with the namespace v

# Authorship information
__author__ = 'Ammishaddai Jacobus'
__version__ = '2.0'
__date__ = 'Oct 6, 2021'
__status__ = 'Development'


def cover_crop_calculator():
    """
    This function display the name of the calculator. Then takes the user input as float, calculates the data with
    algorithms for cover crop calculation and outputs the total needed cover crop needed.
    :return: n/a
    """

    # displays a welcome message
    print('++' * 50)
    print(" ")
    print("                           The crop cover calculator version 1")
    print(" ")
    print("Instructions: You will need the following data: (area Length, area width, and seeding rate)")
    print("to use this calculator.This calculator will provide you with both the general rounded up total")
    print("coverage needed and the exact, most accurate, up to the last decimal total coverage needed.")
    print(" ")
    print('++' * 50)
    print(" ")

    # gets input from the user
    area_length = v.get_positive(prompt='Please type in the area length (.ft) ', limit=1, data_type='float')
    area_width = v.get_positive(prompt='Please type in the area width (.ft) ', limit=1, data_type='float')
    seeding_rate = v.get_positive(prompt='Please type in the seeding rate (lbs) ', limit=1, data_type='float')

    # calculations
    acreage = (area_length * area_width) / 43560
    cover_crop_needed_exact = float(acreage * seeding_rate)
    cover_crop_needed_rounded = round(acreage * seeding_rate, 2)

    # Display results to user
    print(" ")
    print(f"Your total needed crop coverage is: {cover_crop_needed_rounded} lbs (rounded up)")
    print(f"Or {cover_crop_needed_exact} lbs to be exact.")

    # Goodbye message
    print(" ")
    print('++' * 50)
    print(" ")
    print("Thank you for making use of our crop coverage calculator!")
    print(" ")


if __name__ == "__main__":  # Basically if the name of the module is equal to main
    cover_crop_calculator()  # Run this specific program.
