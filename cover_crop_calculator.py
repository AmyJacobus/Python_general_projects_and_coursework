# Header
# Name: Ammishaddai Jacobus
# Date: September 6, 2021
# Description: This is a crop coverage calculator. It asks the user for the area lenght, the area width and it seeding
# rate. The calculator takes that data, and inserts it into an algorithm and that calculates the crop coveraged needed
# based on the data that the user inserted.

# display a welcome message
print('++' * 50)
print(" ")
print("The crop cover calculator version 1")
print("Instructions: You will need the following data: (area Length, area width, and seeding rate) to use this calculator.")
print(" ")
print('++' * 50)
print(" ")
"""
This code displays information about the application to the user. Like the name of the application, it's version and
instructions on what information is needed to succesfully make use of this application.
"""

# get input from the user
area_length = float(input("Please type in the are length(.ft): "))
area_width = float(input("Please type in the area width(.ft): "))
"""
These are two variables to take input from the user. Area length takes the user input for the length of the area, and 
area width takes input about the area width and converts that data into float for both variables.

"""

# calculate miles per gallon
acerage = (area_length * area_width) / 43560
seeding_rate = float(input("Please type in the seeding rate (lbs): "))
cover_crop_needed = (acerage * seeding_rate)
"""

"""

print(" ")
print(f"Your total needed crop coverage is: {cover_crop_needed} lbs.")
"""


"""

print(" ")
print('++' * 50)
print(" ")
print("Thank you for making use of our calculator!")
print(" ")
print("Designed by JCBSoftware & Design.BV")
"""


"""

