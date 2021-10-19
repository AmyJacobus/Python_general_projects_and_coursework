#!/usr/bin/env python3

"""
Programmer: Ammishaddai Jacobus
Date: Oct 15, 2021
Description: This program basically helps the user book a room at the paradise motel. It asks the user for the day of
the week that they would like to book, based of that day they would calculate a day of the week rate, then asks the user
for the room they would like to book, number of gets, number of nights, and based of that information, it calculates the
surcharge, the total charge. And asks the user if they want to confirm their booking by presenting them with the report
of their booking. They get the option of canceling their booking and book another one, or they can book more than one
room at the time or they can not book anything at all, and cancel out the whole program. And if they book multiple rooms,
it will calculate the grand total charge and displays that information for the user once they are done booking.
"""

import random # import the random module to be use to generate random numbers
import sys # import sys to be able to exit out of the program
import validation as v # Imports the validation module as v to be user in this program to validate user input


# authorship
__author__ = 'Ammishaddai Jacobus'
__version__ = '1.0'
__date__ = 'Oct 15, 2021'
__status__ = 'Development'


BASE_RATE = 80  # GLOBAL VARIABLE - CONSTANT


def welcome_msg():
    """
    This function displays the welcome message to the user
    :return: n/a
    """
    print()
    print('=' * 100)
    print()
    print("Welcome to the Paradise Motel Booking System!")
    print()
    print('=' * 100)


def get_dow():
    """
    This functions prompts the user for the day of the week that they would like to book for, it also
    validates the input that the user has typed, by making use of the validation.py module that is imported
    into this module.
    :return: dow
    """

    print("What day of the week would you like to check in? ")
    dow = v.get_dow(prompt='MONDAY - SUNDAY: ')

    return dow


def get_dow_rate(dow):
    """
    This program basically just checks for whatever it takes as dow, that it equals any of the 7 days of the week, then
    it  calculates the base_rate, and if for whatever reason the dow is not a day of the week, which is an error that
    should have never happened, it will output message to the user, and exit the program.
    :param dow: Takes the parameter dow to use it as a variable to check
    :return: n/a
    """
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
    """
    This function generations random numbers for each room, and it returns them to the module so other functions can
    later use this information. Each random number is inserted into a variable.
    :return: num single, num_double, num_king
    """

    num_single = random.randint(0, 8)
    num_double = random.randint(0, 10)
    num_king = random.randint(0, 2)

    return num_single, num_double, num_king


def get_room_rates(dow_rate):
    """
    This functions calculates the rate for the variables single, double and king rate, which the function returns to
    the program so other functions can use it later.
    :param dow_rate: Basically this function takes the parameter dow_rate to use it for the calculation
    :return: single_rate,double_rate, and king_rate
    """

    single_rate = dow_rate
    double_rate = dow_rate * 15
    king_rate = dow_rate * 1.25

    return int(single_rate), int(double_rate), int(king_rate)


def get_room_type_rate(dow, dow_rate):
    """
    This function adds data to the variable num single, num double and num king for the function get_avail_rooms, it
    also adds data from the get_room_rates to the variable single_rate, double_rate, king_rate while making use of the
    parameter dow_rate in order to do so. This function displays the available rooms report for the user, then prompts
    the user for what room they would like to book, and in a loop verifies if the user has inserted the right info,
    and return the room type, and the room rate, otherwise it will tell the user invalid input and that they should
    try again.
    :param dow: this parameter is passed to be used in the print out information for the user
    :param dow_rate: this parameter is used to successfully gather the right data from the ger room rates function
    :return: room_type, room_rate(depending on what the user typed)
    """
    num_single, num_double, num_king = get_avail_rooms()
    single_rate, double_rate, king_rate = get_room_rates(dow_rate)

    print()
    print(f'{dow} Available Rooms')
    print('=' * 100)
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
    """
    Asks the user for the num of guests that will stay in a specific room. And returns num_guests.It also has validation
    for the user input to check if they have typed in only the allowed guests for each room. If for whatever reason
    the room_type does not equal any of the rooms, it will tell the user that there has been an error and it will
    exit the program.
    :param room_type: this parameter is passed to be used in the if-else
    :return: num_guests
    """
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
    """
    This function basically checks if the num_guests equals a certain amount of guests, and return the surcharge based
    on those number of guests.
    :param num_guests: It passes the num_guests parameter in order to run the if else
    :return: surcharge data
    """
    if num_guests == 1:
        return 0
    elif num_guests == 2:
        return 10
    elif num_guests == 3:
        return 18
    elif num_guests == 4:
        return 32


def get_number_of_nights(room_type, num_guests, room_type_rate):
    """
    Basically this function takes the user input for the number of nights that they would like to input, and returns
    this data to the program, so other functions can later make use of it.
    :param room_type: It is being passed as a parameter so it can display the room_type from other functions in the main
    :param num_guests: It is being passed as a parameter so it can display the num_guests from other functions in the main
    :param room_type_rate:  It is being passed as a parameter so it can display the room_type_rate from other functions in the main
    :return:  num_nights
    """

    num_nights = v.get_num(prompt=f'How many nights will you want to book a {room_type} room, with {num_guests} guests '
                                  f'at the rate of ${room_type_rate}: ', data_type='int')

    return num_nights


def confirm_booking(num_nights, total_charge):
    """
    This function prompts the user for confirm booking for certain number of nights and tells them the total charge,
    so they can yes or no. Then it returns this data of yes and no to the main program so other functions can make use
    of it.
    :param num_nights: it is being passed as a parameter so it can display the num_nights from other functions in the main
    :param total_charge: it is being passed as a parameter so it can display the total_charge from other functions in the main
    :return: choice
    """
    print()
    print(f'Would you like to confirm your booking for {num_nights} nights at the total charge of ${total_charge}')
    choice = v.get_choice(prompt='Y=Yes or N=no: ')

    return choice

def get_do_you_want_to_continue():
    """
    This function prompts if they want to book another room or not. If it is a yes, returns true so other functions can
    use this data, if its not a yes, it returns False, so other functions know that uses do not want to continue, and
    should not loop the whole module again.
    :return: True or False
    """
    choice = v.get_choice(prompt='Would you like to book another room [yes/no]: ')
    if choice in ['yes','y']:
        return True
    else:
        return False

def main():
    print('WE USE THIS TO TEST')

if __name__ == "__main__":
      main()
