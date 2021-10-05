#!/usr/bin/env python3

"""
DOCSTRING
"""

__author__ = 'Ammishaddai Jacobus and Rushandy Andrea'
__version__ = '1.0'
__date__ = 'Oct 6, 2021'
__status__ = 'Development'


def get_range(prompt, low, high, data_type='int'):

    while True:
        user_input = input(f'{prompt} (Range = {low}-{high}): ')

        if data_type == 'int':
            number = int(user_input)
        else:
            number = float(user_input)

        if number > low and number <= high:
            return number

        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high)

# get_positive():
#     # ARGUMENTS HERE
#
# get_num():
#     # ARGUMENTS HERE


def main():
    choice = "y"
    while choice.lower() == "y":
        # get input
        valid_number = get_range(prompt="Enter float", low=0, high=1000, data_type='float')
        print("Valid number = ", valid_number)
        print()
        valid_number = get_range(prompt="Enter int", low=0, high=1000, data_type='int')
        print("Valid integer = ", valid_number)
        print()

        # see if the user wants to continue
        choice = input("Repeat? (y/n): ")
        print()

    print("Bye!")


if __name__ == "__main__":
    main()
