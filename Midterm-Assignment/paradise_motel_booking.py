#!/usr/bin/env python3

import random
import day_of_week as dow
import Rooms as rm

# authorship
__author__ = 'Ammishaddai Jacobus'
__version__ = '2.0'
__date__ = 'Oct 6, 2021'
__status__ = 'Development'


base_rate = 80
# Welcome message
print('=' * 100)
print()
print(f'{"Welcome to the Paradise Motel Booking System!":>30s}') # NEEDS FIXING
print()
print('=' * 100)

# Take user input
print()
print('Which day of the week will you be checking in?')
day_chosen = dow.get_dow(prompt='Monday – Sunday: ').upper()



# CALCULATE BASE RATE
if day_chosen == 'SUNDAY':
    BSRT = (base_rate * 0.2) + base_rate
    print(BSRT)
elif day_chosen == 'MONDAY':
    BSRT = (base_rate * 0.2) + base_rate
    print(BSRT)
elif day_chosen == 'TUESDAY':
    BSRT = (base_rate * 0.2) + base_rate
    print(BSRT)
elif day_chosen == 'WEDNESDAY':
    BSRT = (base_rate * 0.1) + base_rate
    print(BSRT)
elif day_chosen == 'THURSDAY':
    BSRT = (base_rate * 0.1) + base_rate
    print(BSRT)
elif day_chosen == 'FRIDAY':
    BSRT = base_rate
    print(BSRT)
elif day_chosen == 'SATURDAY':
    BSRT = base_rate
    print(BSRT)

# RANDOMIZE NUMBERS
print()
print(f'{day_chosen} Available rooms')
print('=' * 100)
print()

rooms_single = random.randint(0,9)
room_double = random.randint(0,11)
room_king = random.randint(0,3)

bsrt_single = BSRT
bsrt_double = (BSRT * 0.5) + BSRT
bsrt_king = (BSRT * 0.25) + BSRT

# base rate room calculation
print(f'{rooms_single} single rooms (2 guests max) available at ${bsrt_single}')
print(f'{room_double} single rooms (2 guests max) available at ${bsrt_double}')
print(f'{room_king} single rooms (2 guests max) available at ${bsrt_king}')

# DECLARE ROOMS

# ROOM CALCULATION

# if day_chosen == 'SUN':
#     # DISPLAY FUNCTION FOR THIS
# elif day_chosen == 'MON':
#     # DISPLAY FUNCTION FOR THIS
#
# elif day_chosen == 'TUE':
#         # DISPLAY FUNCTION FOR THIS
#
# elif day_chosen == 'WED':
#     # DISPLAY FUNCTION FOR THIS
#
# elif day_chosen == 'THU':
#     # DISPLAY FUNCTION FOR THIS
#
# elif day_chosen == 'FRI':
#     # DISPLAY FUNCTION FOR THIS
#
# elif day_chosen == 'SAT':
#     # DISPLAY FUNCTION FOR THIS




# RANDOMIZE ROOMS


# DISPLAY ROOM REPORT

# ASK WHAT TYPE OF BOOK DO THEY WANT TO BOOK

# ASK HOW MANY GUESTS WILL BE STAYING

# HOW MANY DAYS THEY WANT TO BOOK {ROOM{

# DISPLAY REPORT OF THE INFO













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



