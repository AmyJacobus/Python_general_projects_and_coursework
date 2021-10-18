#!/usr/bin/env python3

import hotel


def main():

    hotel.welcome_msg()
    dow = hotel.get_dow()
    dow_rate = hotel.get_dow_rate(dow)
    room_type, room_type_rate = hotel.get_room_type_rate(dow_rate)




if __name__ == "__main__":
      main()