#!/usr/bin/env python3

"""
Programmer: Ammishaddai Jacobus
Date:
Description: This program will help determine how many cow-calf pairs a pasture can support per acre of forage.
"""

# Authorship
__author__ = 'Ammishaddai Jacobus'
__version__ = '1.0'
__date__ = 'Sept 12, 2021'
__status__ = 'Development'

# Welcome message to user

# The calc program
while True:

    i = 0
    forage_sample = 0

    forage_sample = int(input("Please enter the # of forage samples taken (Valid 1-20):"))
    if forage_sample in range(1, 21):
        break
    else:
        print("Invalid Value! Please type in a number between 1 and 20")


print("Please type in per every sample dry clipping in gram")

# For loop to get the number of each and every input from user, about the dry grass in grams
i = 1
sample_total = 0
for i in range(forage_sample):
    sample_total += int(input(f"Type in the total grams for sample # {i+1}: "))

# Calculations for the average in pounds and per acre
square_foot_avg_pounds = round((sample_total / (i+1)) / 453.592, 3)
forage_per_acre = round(square_foot_avg_pounds * 43560)

# Output sqaure foot average per round and forage per acre
print(f"Square foot avg per round = {square_foot_avg_pounds}")
print(f"Forage per acre in pounds = {forage_per_acre}")

# While loop to take user input
while True:
    utilization_rate_input = int(input(" Please enter the utilization rate (Valid 1-100): "))
    if utilization_rate_input in range(1, 101):
        break
    else:
        print("Invalid Value! Please type in a number between 1 and 100!")
        print("Please try again below.")

# While loop to take user input
while True:
    animal_unit_month = int(input("Please enter the animal unit month, anywhere from 1 to 2000 (.lbs): "))
    if animal_unit_month in range(1, 2001):
        break
    else:
        print("Invalid Value! Please type in a number between 1 and 2000.")
        print("Please try again below.")

# Calculate the stocking rate and print the stocking rate result for the user
stocking_rate = round(forage_per_acre * (utilization_rate_input / 100) / animal_unit_month, 2)
print(f"The stocking rate is: {stocking_rate}")


# Testing calculations
# print(f"This is the total from your samples: {sample_total}")
# print(f"total rounds was: {i+1}")
# print(square_foot_avg_pounds)
# print(forage_per_acre)






