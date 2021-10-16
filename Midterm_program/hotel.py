#!/usr/bin/env python3

"""
Programmer: Ammishaddai Jacobus
Date: 10/14/2021
Description:
"""

import random
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

    while True:

        print("What day of the week would you like to check in? ")
        dow = v.get_dow(prompt='MONDAY - SUNDAY')

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


def get_room_rates(dow_rate):

    single_rate = dow_rate
    double_rate = dow_rate * 15
    king_rate = dow_rate * 1.25

    return single_rate, double_rate, king_rate


def get_room_type_rate(dow_rate):

     num_single, num_double, num_king = get_avail_rooms()
     single_rate, double_rate, king_rate = get_room_rates(dow_rate)

     # print(f'{dow} available rooms')
     print('='*50)
     print(f'{num_single} single rooms (2 guest max) available at {single_rate}')
     print(f'{num_double} double rooms(4 guest max) available at {double_rate}')
     print(f'{num_king} king rooms (2 guest max) available at {king_rate}')

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

         return room_type

def get_num_guests(room_type):

        num_guests = v.get_range(prompt='How many guests will be staying in the room: ', low=0, high=5)

        return num_guests

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


def get_number_of_nights(room_type, num_guests, room_type_rate):

    print(f'How many days will you want to book a {room_type} room,')
    num_nights = input(f'With {num_guests} at ')

    return num_nights


def display_booking(dow, dow_rate, room_type, room_type_rate, num_guests, surcharge):
    print()
    print(f'You chose {dow}')
    print(f'Room type: {room_type}')
    print(f'With {num_guests}')
    if num_guests > 0:
        print(f'With a surcharge of ${surcharge}')
        total_charge = room_type_rate + surcharge
        print(f'So your total charge for this booking is: ${total_charge}')
    else:
        total_charge = room_type_rate
        print(f'Your total charge for this booking is: ${total_charge}')


def confirm_booking(num_nights, total_charge):
        #  prompt the user to confirm their booking num_nights & total_charge
        print(f'Would you like to confirm your booking for {num_nights} nights at the total charge of ${total_charge}')

        while True:
            confirm = v.get_choice(prompt='Y=Yes or N=no').lower()
            if confirm in ['yes','y']:
                print(f'Your total bill is ${total_charge}')
                print('We are looking forward to seeing you soon!')
                break
            elif confirm in ['no','n']:
                print('Thank you for making use of our service')
                print('Hope to see you again soon')
                exit()


def get_do_you_want_to_continue():
        # ISSUE
        while True:
          choice  = v.get_choice(prompt= 'Would you like to book another room  [yes/no]: ').lower()
          if choice in ['yes','y']:
              main()
          elif choice in ['no','n']:
              print('Thank you for making use of our booking service')
              exit()


def main():
    print('Here we test')


if __name__ == "__main__":
      main()