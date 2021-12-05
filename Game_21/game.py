#!/usr/bin/env python3

"""
Programmers:
Date:
Description:
"""

# Authorship information # Done by Amy
__author__ = 'Ammishaddai Jacobus and Ben Sadler'
__version__ = '1.0'
__date__ = 'NEED TO BE DONE'
__status__ = 'Development'


LINE_LENGTH = 100




def display_msg():
    print('$' * LINE_LENGTH)
    print()
    print('                                       WELCOME TO GAME 21')  # HOW TO STRING FORMAT
    print()
    print('$' * LINE_LENGTH)
    print()
    print('The rules are simple!')
    print('1. Each player is trying to get as close to 21 without going over.')
    print('2. Each player is ONLY trying to beat the dealer\'s hand.')
    print('3. The dealer will keep dealing himself cards until he beats all players hands or goes over 21.')
    print('4. Tie goes to the player, not the dealer.')
    print('5. Each player gets dealt two card between 1 - 10.')
    print('6. The player then can choose to receive additional cards.')
    print('7. Each player starts with $1.00.')
    print('8. Default bet is 25 cents, but the player can double it after holding.')
    print('9. Winner is the last person with cash, not including the dealer.')


def get_players(players):
    # Create a dictionary or pass an empty dictionary
    # while loop
    # Add funds etc to the dictionary

    # How do we add to the dictionary with while loops? SINCE DEBBIES EXAMPLE IS LIKE A 2D/3D dictionary
    print()
    print('=' * LINE_LENGTH)
    print('Now lets get this game setup.  Who is all playing?')
    print('Please enter a player\'s name or enter \'done\' when finished.')
    print()
    while True:
        name = input('Enter name: ') # NEEDS FORMATTING F-STRING
        if name != 'Done':
            continue
        else:
            break

def play(players):
    print()
    print('=' * LINE_LENGTH)
    print('Starting game...')
    print('=' * LINE_LENGTH)
    print()

    # NEED TO DETECT PLAYER FROM THE DICTIONARY (KEY AND ACCESS THEIR INFORMATION)
      # - RANDOM NUMBER FOR CARDS TO GENERATE 2 CARDS FOR PLAYER

    # should use while or for loop here
    input('Do you want another card? (y=yes, n=no): ')
    print('Cards: RANDOM NR1, RANDOM NR2, RANDOM NR3')
    # if user says yes, continue to add more cards, until they go over 21 (then they lose!)
    # if they choose no, display player name, holds at  (Card total)

    print('Do you want to double your 25 cent beat? (y=yes, n=no): ')


def main():

    players = {}  # We start with an empty dictionary

    display_msg(players)
    get_players(players)


if __name__ == "__main__":  # Basically if the name of the module is equal to main
    main()  # Run this specific program.