#!/usr/bin/env python3

"""
Programmer: Ammishaddai Jacobus
Date: Oct 15, 2021
Description: This is a validation module to validate the input from users. It validates if the users input an integer,
if they input a number, a positive number, or a string, and if they not input the right data, it will notify them of
their error.
"""

# authorship


def get_dow(prompt):

    while True:
        dow = input(f'{prompt}').upper()
        if dow in ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY','SUNDAY']:
            return dow
        else:
            print('Error! Please type in a day of the week.')


def get_num(prompt, data_type='int'):

    while True:

        user_input = input(prompt)

        if data_type == 'int':
            user_input = int(user_input)
        elif data_type == 'float':
            user_input = float(user_input)
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
            print("ERROR")
            exit()


def get_choice(prompt):

    while True:

        choice = input(f'{prompt}').lower()
        if choice in ['yes', 'y']:
            break
        elif choice in ['no', 'n']:
            break
        else:
            print('You have not input a yes or no.Try again.')



def main():
    get_choice(prompt='yes or no: ')


if __name__ == "__main__":
      main()
