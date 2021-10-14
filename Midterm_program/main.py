#!/usr/bin/env python3

"""
Programmer:
Date:
Description:
"""

import hotel

def main():
    """
    DOCSTRING
    :return: n/a
    """

    loop = True

    total_charge = 0

    while loop

        dow = hotel.get_dow_rate()
        dow_rate = hotel.get_dow_rate(dow)
        room_type, room_type_rate = hotel.get_room_type_rate(dow_rate)
        num_guests = hotel.get_num_guests(room_type)
        surcharge = hotel.get_surcharge(num_guests)
        total_charge += room_type_rate + surcharge
        hotel.display_booking(dow, dow_rate, room_type, room_type_rate, num_guests, surcharge)
        loop = hotel.get_do_you_want_to_continue()

    # display total_charge
    print(total_charge)

if __name__ == "__main__":
      main()