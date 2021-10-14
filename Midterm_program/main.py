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

    while loop:

        dow = hotel.get_dow()
        dow_rate = hotel.get_dow_rate(dow)
        room_type, room_type_rate = hotel.get_room_type_rate(dow_rate)
        print(room_type, room_type_rate) #test

    # display total_charge
    print(total_charge)

if __name__ == "__main__":
      main()