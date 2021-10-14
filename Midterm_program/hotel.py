#!/usr/bin/env python3

"""
Programmer:
Date:
Description:
"""

import random
import validation

# authorship
__author__ = 'Ammishaddai Jacobus'
__version__ = '2.0'
__date__ = 'Oct 15, 2021'
__status__ = 'Development'

base_rate = 80 # GLOBAL VARIABLE - CONSTANT

def welcome_msg():

    print('=' * 100)
    print()
    print(f'{"Welcome to the Paradise Motel Booking System!":>30s}')  # NEEDS FIXING
    print()
    print('=' * 100)


def get_dow():
        #prompt the user for what dow they want to check in & validate (1-7)
        #NEED TO VALIDATE
        print("What day of the week would you like to check in? ")
        dow = input('MONDAY - SUNDAY: ').upper()

        return dow


def get_dow_rate(dow):
        # MUST VALIDATE
        # calculate the dow_rate based on dow
        print('this function runs...')
        # calculate dow
        if dow == 'SUNDAY':
            dow_rate = (base_rate * 0.2) + base_rate # br *= 1.2
            return dow_rate
        elif dow == 'MONDAY':
            dow_rate = (base_rate * 0.2) + base_rate
            return dow_rate
        elif dow == 'TUESDAY':
            dow_rate = (base_rate * 0.2) + base_rate
            return dow_rate
        elif dow == 'WEDNESDAY':
            dow_rate = (base_rate * 0.1) + base_rate
            return dow_rate
        elif dow == 'THURSDAY':
            dow_rate = (base_rate * 0.1) + base_rate
            return dow_rate
        elif dow == 'FRIDAY':
            dow_rate = base_rate
            return dow_rate
        elif dow == 'SATURDAY':
            dow_rate = base_rate
            return dow_rate

def get_avail_rooms(num_single, num_double, num_king):
#
#         rooms_single = random.randint(0, 9)
#         room_double = random.randint(0, 11)
#         room_king = random.randint(0, 3)
#
#         return num_single
#         return num_double
#         return num_king
#     #     generate
#     #     available
#     #     rooms
#     #     for single, double king using random numbers
#     #     return num_single, num_double, num_king
#
def get_room_rates():
     #     calculate rates based on type
    #     return single_rate, double_rate, king_rate
         dow = get_dow()
         dow_rate = get_dow_rate(dow)

        single_rate = dow_rate
        double_rate = (dow_rate * 0.5 ) + dow_rate
        king_rate = (dow_rate * 0.25 ) + dow_rate

        return single_rate
        return king_rate
#
def get_room_type_rate(dow_rate):
         # num_single, num_double, num_king = get_avail_rooms()
         # single_rate, double_rate, king_rate = get_room_rates(dow_rate)
            #
            #      # display available rooms & room rates
            #      print()
            #      print('DAY OF THE WEEK NAME HERE - ''available rooms')
            #      print('='*50)
            #      print('REPORT HERE')
            #      # MUST VALIDATE
            #      room_type = input('Which type of room (Single = S, Double = D, King = K')
            #
            #      # for which room type and validate room type (1-3) and availabilty
            #
            # return room_type, room_type_rate
            # return room_type
            # return room_type_rate

def get_num_guests(room_type):
        # #   prompt the user for the num_guests in the room and validate range based on room_type
        #     num_guests = input('How many guests are staying in the room: ')
        #         # or end
        #         #  the
        #         # program if an
        #          invalid
        #         # room_type is received
        #     return num_guests

def calc_surcharge(num_guests):
        # #     calculate
        # #     the
        # #     surcharge
        # #     return surcharge
        # #

def display_booking(dow, dow_rate, room_type, room_type_rate, num_guests, surcharge):
        # #     display
        # #     a
        # #     summary
        # #     of
        # #     the
        # #     all
        # #     booking
        # #     information
        # #     or end
        # #     the
        # #     program if invalid
        # #     dow, and room_type is received

def get_do_you_want_to_continue():

        while True:

         choice  = input('Would you like to book another room  [yes/no]: ').lower()
         if choice == 'yes' or 'y':
            return True
         else:
            return False

# the user if they want to book another room (lower case input and validate: y, n, yes, no) return true or false


def main():

    get_do_you_want_to_continue()


if __name__ == "__main__":
      main()