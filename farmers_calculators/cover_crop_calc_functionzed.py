"""
# Programmer: Ammishaddai Jacobus
# Date: September 6, 2021
# Description: This is a crop coverage calculator. It asks the user for the area length, the area width and it seeding
# rate. The calculator takes that data, and inserts it into an algorithm and that calculates the crop coverage needed
# and outputs the result to the user.
"""

# Authorship
__author__ = 'Ammishaddai Jacobus and Rushandy Andrea'
__version__ = '1.0'
__date__ = 'TYPE IN THE DATE IN HERE' # THIS PART STILL NEEDS EDITING, FIX THIS AMY
__status__ = 'Development'

def welcome_msg():
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

def user_input():
    area_length = float(input("Please type in the area length (.ft):  "))
    area_width = float(input("Please type in the area width (.ft):   "))
    seeding_rate = float(input("Please type in the seeding rate (lbs): "))


def calculations(area_length, area_width, seeding_rate): # calculations
    acreage = (area_length * area_width) / 43560
    cover_crop_needed_exact = float(acreage * seeding_rate)
    cover_crop_needed_rounded = round(acreage * seeding_rate, 2)


def result_output(): # Display results to user
    print(" ")
    print(f"Your total needed crop coverage is: {cover_crop_needed_rounded} lbs (rounded up)")
    print(f"Or {cover_crop_needed_exact} lbs to be exact.")


def goodbye_msg():
    print(" ")
    print('++' * 50)
    print(" ")
    print("Thank you for making use of our crop coverage calculator!")
    print(" ")

def main():

if __name__ == "__main__":
    main()