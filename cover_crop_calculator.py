# Header
# Programmer: Ammishaddai Jacobus
# Date: September 6, 2021
# Description: This is a crop coverage calculator. It asks the user for the area length, the area width and it seeding
# rate. The calculator takes that data, and inserts it into an algorithm and that calculates the crop coverage needed
# and outputs the result to the user.

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
"""
This code displays information about the application to the user. Like the name of the application, it's version and
instructions on what information is needed to successfully make use of this application.
"""

# gets input from the user
area_length = float(input("Please type in the area length (.ft): "))
area_width = float(input("Please type in the area width (.ft): "))
seeding_rate = float(input("Please type in the seeding rate (lbs): "))
"""
Here are coded 3 variables to take input from the user. Area length takes the user input for the length of the area,
area width takes input about the area width, and seeding rate takes the input and converts that data into float for 
all 3 variables into a float.
"""

# calculations
acreage = (area_length * area_width) / 43560
cover_crop_needed_exact = float(acreage * seeding_rate)
cover_crop_needed_rounded = round(acreage * seeding_rate, 2)
"""
Here we have 3 variables that calculate the acreage,the total cover crop that is needed exactly 
up to the last decimal number (for more exact and science purposes), and the cover crop needed rounded up in case the
user wants the general total (for the average Joe). Extra, but
more user friendly that way.
"""

# Display results to user
print(" ")
print(f"Your total needed crop coverage is: {cover_crop_needed_rounded} lbs (rounded up)")
print(f"Or {cover_crop_needed_exact} lbs to be exact.")
"""
This prints out some empty space line and prints out the totals of the cover crop that is needed to the user. As a float
total and a rounded up total.
"""

# Goodbye message
print(" ")
print('++' * 50)
print(" ")
print("Thank you for making use of our crop coverage calculator!")
print(" ")
"""
This prints out some empty space lines
Some designs to make the calculator look a bit nicer, when users are using it
And it outputs some thank you message to the user.
"""