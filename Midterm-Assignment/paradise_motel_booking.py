# shabang

# imports
import random
import Location as l

# authorship


print('Welcome to the Paradise Motel Booking System')




day_of_the_week = input('Which day of the week will you be checking in [MON - SUN]: ').lower()
days_of_the_week = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

if day_of_the_week == days_of_the_week[0]:
    print('tested monday')

    # Should have validation to check if it even equals 1 letter
# if day_of_the_week == days_of_the_week[0]:
#     print('calculation has to happen 1')
# elif day_of_the_week == days_of_the_week[1]:
#     print('calculation has to happen 2')
# elif day_of_the_week == days_of_the_week[2]:
#     print('calculation has to happen 3')
# elif day_of_the_week == days_of_the_week[3]:
#     print('calculation has to  4')
# elif day_of_the_week == days_of_the_week[4:
#     print('calculation has to happen 5')
# elif day_of_the_week == days_of_the_week[5]:
#     print('calculation has to happen 6')
# elif day_of_the_week == days_of_the_week[6]:
#     print('calculation has to happen 7')







# make sure to use random() for the - available rooms

# Percentage increase should be:
  # br *= 1.2 (day of week rate) instead of doing br = br +  (br*0.2)
  # base rate could be a constant  like $80

# Display when you display the chosen day
# example MONDAY available Rooms .upper()
# Make sure to search for atleast the first letter in the input, like double0er had un error, you can make sure it still
# goes through by using some character capture thingy.

# The program must have several validations

# Original ideas:
# - Add validation module for credit card or paypal payment system
# - Based on your location - special rating br: (NE: $60, FL: $90, NY: $80), anywhere in  the U.S is $85
# - International location - Base rate of $95

# 3 Modules
# Validation
# Main
# Credit card authorization
# Semi - manual chatbot

