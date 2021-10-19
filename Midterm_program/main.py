#!/usr/bin/env python3

"""
Programmer:
Date:
Description:
"""

import hotel

# authorship
__author__ = 'Ammishaddai Jacobus'
__version__ = '1.0'
__date__ = 'Oct 15, 2021'
__status__ = 'Development'

def main():
    """
    This is main, it calls different functions from the hotel module. It assigns some of their return into variables
    and assigns some of those variables to other functions in order to run them. Basically main is running the program.
    It also puts the program in a while loop, so the user can book more than one room at the time, and once they no
    longer want to book a room, it will get out of the loop and provide the user with the grand total charge of their
    booking.
    :return: n/a
    """

    loop = True
    grand_total_charge = 0

    while loop:

        hotel.welcome_msg()
        dow = hotel.get_dow()
        dow_rate = hotel.get_dow_rate(dow)

        room_type, room_type_rate = hotel.get_room_type_rate(dow,dow_rate)
        num_guests = hotel.get_num_guests(room_type)

        surcharge = hotel.calc_surcharge(num_guests)
        total_room_rate = room_type_rate + surcharge

        num_nights = hotel.get_number_of_nights(room_type, num_guests, total_room_rate)
        total_charge = total_room_rate * num_nights

        book_another = hotel.confirm_booking(num_nights, total_charge)
        if book_another in ['yes','y']:
            grand_total_charge += total_charge

        loop = hotel.get_do_you_want_to_continue()

    print()
    print('='*50)
    print(f'Your grand total for this booking is: ${grand_total_charge}')
    print(f'Thank you for making use of our booking system. See you soon!')
    print()
    print('='*50)


if __name__ == "__main__": # Basically if the name of the module is equal to main
     main() # It calls mains