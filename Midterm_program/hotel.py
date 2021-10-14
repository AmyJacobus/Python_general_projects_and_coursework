#!/usr/bin/env python3

"""
Programmer: Ammishaddai Jacobus
Date: 10/14/2021
Description:
"""

import random
import validation

# authorship
__author__ = 'Ammishaddai Jacobus'
__version__ = '2.0'
__date__ = 'Oct 15, 2021'
__status__ = 'Development'

BASE_RATE = 80 # GLOBAL VARIABLE - CONSTANT

def welcome_msg():

    print('=' * 100)
    print()
    print(f'{"Welcome to the Paradise Motel Booking System!":>30s}')  # NEEDS FIXING
    print()
    print('=' * 100)


def get_dow():

        while True:

            print("What day of the week would you like to check in? ")
            dow = input('MONDAY - SUNDAY: ').upper()
            if dow in ['Monday','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY']:
                break
            else:
                print('Error! Please type in a day of the week.')

        return dow

def get_dow_rate(dow):
        # calculate dow
        if dow in ['SUNDAY', 'MONDAY', 'TUESDAY']:
            return BASE_RATE * 1.2
        elif dow == ['WEDNESDAY','THURSDAY']:
            return (BASE_RATE * 1.1)
        elif dow == ['FRIDAY','SATURDAY']:
            return BASE_RATE
        else:
            print('Program error')
            print('Exiting the program now')
            exit()

def get_avail_rooms():
        # WHAT EXACTLY IS HAPPENING HERE
        num_single = random.randint(0, 9)
        num_double = random.randint(0, 11)
        num_king= random.randint(0, 3)

        return num_single, num_double, num_king

# generate available rooms for single, double king using random numbers

#
def get_room_rates(dow_rate):

        single_rate = dow_rate
        double_rate = dow_rate * 15
        king_rate = dow_rate * 1.25

        return single_rate, double_rate, king_rate


def get_room_type_rate(prompt,dow, dow_rate):

     num_single, num_double, num_king = get_avail_rooms()
     single_rate, double_rate, king_rate = get_room_rates(dow_rate)

     print(f'{dow} available rooms')
     print('='*50)
     print(f'{num_single}(2 guest max) available at {single_rate}')
     print(f'{num_single}(4 guest max) available at {double_rate}')
     print(f'{num_single}(2 guest max) available at {king_rate}')

     print('What room would you like to book: ')

     while True:
         room_type = input('S= Single, D = Double, K = King').upper()
         if room_type in ['S', 'SINGLE']:
             return 'SINGLE', dow_rate
         elif room_type in ['D' or 'DOUBLE']:
             return 'DOUBLE', dow_rate * 1.5
         elif room_type in ['K' or 'KING']:
             return 'KING', dow_rate * 1.25
         else:
             print('Invalid input, try again.')


def get_num_guests(room_type):

        num_guests = input('How many guests will be staying in the room: ')
        if num_guests == 'int':
            return num_guests
        else:
            print('Invalid input')
            exit()

def calc_surcharge(num_guests):


        if num_guests == 1:
            surcharge = 0
        elif num_guests == 2:
            surcharge = 10
        elif num_guests == 3:
            surcharge = 18
        elif num_guests == 4:
            surcharge = 32

        return surcharge


def many_days(room_type, num_guests):

    print(f'How many days will you want to book a {room_type} room,')
    total_days = input(f'With {num_guests} at ')


def display_booking(dow, dow_rate, room_type, room_type_rate, num_guests, surcharge):
        # display
        # a
        # summary
        # of
        # the
        # all
        # booking
        # information
        # or end
        # the
        # program if invalid
        # dow, and room_type is received


def get_do_you_want_to_continue():
        # ISSUE
        while True:

         choice  = input('Would you like to book another room  [yes/no]: ').lower()
         if choice == 'yes' or 'y':
            return False
         else:
            return True

# the user if they want to book another room (lower case input and validate: y, n, yes, no) return true or false


def main():
    print('Here we test')


if __name__ == "__main__":
      main()