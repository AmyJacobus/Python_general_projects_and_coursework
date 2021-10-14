#!/usr/bin/env python3

"""
Programmer: Ammishaddai Jacobus
Date: Oct 15, 2021
Description: This is a validation module to validate the input from users. It validates if the users input an integer,
if they input a number, a positive number, or a string, and if they not input the right data, it will notify them of
their error.
"""

# authorship

def get_num(prompt, data_type='int'):

    while True:

        user_input = input(prompt)

        if data_type == 'int':
            number = int(user_input)
        elif data_type == 'float':
            number = float(user_input)
        else:
            print("Entry must be a number")


def get_pos(prompt, limit, data_type='int'):

    while True:

        user_input = input(f'{prompt} input must be greater than or equal to {limit}: ')

        if data_type == 'int':
            number = int(user_input)
        else:
            number = float(user_input)

        if number > limit:
            return number
        else:
            print(f'The number cannot be below {limit}')


def main():
    get_pos(prompt='How many rooms would you like to book ', limit=1)
    get_num(prompt='input a number: ', data_type='float')

if __name__ == "__main__":
      main()
