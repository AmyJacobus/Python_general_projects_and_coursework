#!/usr/bin/env python3

"""
Programmer: Ammishaddai Jacobus
Date: 10/14/2021
Description:
"""

import random
import sys
import validation as v

# authorship
__author__ = 'Ammishaddai Jacobus'
__version__ = '2.0'
__date__ = 'Oct 15, 2021'
__status__ = 'Development'


BASE_RATE = 80  # GLOBAL VARIABLE - CONSTANT


def welcome_msg():

    print('=' * 100)
    print()
    print(f'{"Welcome to the Paradise Motel Booking System!":>30s}')  # NEEDS FIXING
    print()
    print('=' * 100)


def get_dow():

    print("What day of the week would you like to check in? ")
    dow = v.get_dow(prompt='MONDAY - SUNDAY: ')

    return dow


def get_dow_rate(dow):
    # calculate dow
    if dow in ['SUNDAY', 'MONDAY', 'TUESDAY']:
        return BASE_RATE * 1.2
    elif dow == ['WEDNESDAY', 'THURSDAY']:
        return BASE_RATE * 1.1
    elif dow == ['FRIDAY', 'SATURDAY']:
        return BASE_RATE
    else:
        print('Program error')
        print('Exiting the program now..')
        exit()


def get_avail_rooms():

    num_single = random.randint(0, 8)
    num_double = random.randint(0, 10)
    num_king = random.randint(0, 2)

    return num_single, num_double, num_king


def get_room_rates(dow_rate):

    single_rate = dow_rate
    double_rate = dow_rate * 15
    king_rate = dow_rate * 1.25

    return single_rate, double_rate, king_rate


def get_room_type_rate(dow, dow_rate):

    num_single, num_double, num_king = get_avail_rooms()
    single_rate, double_rate, king_rate = get_room_rates(dow_rate)

    print()
    print(f'{dow} Available Rooms')
    print('='*50)
    print(f'{num_single} single rooms (2 guest max) available at ${single_rate}')
    print(f'{num_double} double rooms (4 guest max) available at ${double_rate}')
    print(f'{num_king} king rooms   (2 guest max) available at ${king_rate}')
    print()

    print('What room would you like to book: ')

    while True:
     room_type = input('S = Single, D = Double, K = King: ').upper()
     if room_type in ['S', 'SINGLE']:
        return room_type, single_rate
     elif room_type in ['D', 'DOUBLE']:
        return room_type, double_rate
     elif room_type in ['K', 'KING']:
        return room_type, king_rate
     else:
        print('Invalid input, try again.')


def get_num_guests(room_type):

    if room_type in ['D' or 'DOUBLE']:
        print()
        num_guests = v.get_range(prompt=f'How many guests will be staying in the {room_type} room: ', low=1, high=4)
        return num_guests
    elif room_type in ['S', 'SINGLE', 'K', 'KING']:
        print()
        num_guests = v.get_range(prompt=f'How many guests will be staying in the {room_type} room: ', low=1, high=2)
        return num_guests
    else:
        print('There has been an error.')
        sys.exit()


def calc_surcharge(num_guests):

    if num_guests == 1:
        return 0
    elif num_guests == 2:
        return 10
    elif num_guests == 3:
        return 18
    elif num_guests == 4:
        return 32


def get_number_of_nights(room_type, num_guests, room_type_rate):

    num_nights = v.get_num(prompt=f'How many nights will you want to book a {room_type} room, with {num_guests} guests '
                                  f'at the rate of ${room_type_rate}: ', data_type='int')

    return num_nights


def confirm_booking(num_nights, total_charge):

    print(f'Would you like to confirm your booking for {num_nights} nights at the total charge of ${total_charge}')
    choice = v.get_choice(prompt='Y=Yes or N=no: ')

    return choice

def get_do_you_want_to_continue():

    choice = v.get_choice(prompt='Would you like to book another room [yes/no]: ')
    if choice in ['yes','y']:
        return True
    else:
        return False
