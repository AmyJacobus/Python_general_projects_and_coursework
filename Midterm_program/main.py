#!/usr/bin/env python3

import hotel


def main():

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

        if hotel.confirm_booking(num_nights, total_charge):
                grand_total_charge += total_charge

        loop = hotel.get_do_you_want_to_continue()

    print()
    print('='*50)
    print(f'Your grand total for this booking is: ${grand_total_charge}')
    print(f'Thank you for making use of our booking system. See you soon!')
    print()
    print('='*50)


if __name__ == "__main__":
      main()