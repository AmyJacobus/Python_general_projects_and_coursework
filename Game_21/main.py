#!/usr/bin/env python3

"""
Programmers:
Date:
Description:
"""

# Authorship information # Done by Amy
__author__ = 'Ammishaddai Jacobus'
__version__ = '1.0'
__date__ = 'NEED TO BE DONE'
__status__ = 'Development'

import random
import game as g


def play_game():
    """
    Play game is the main outer while loop to keep playing rounds
    return: n/a
    """


def main():

    players = {}  # We start with an empty dictionary
    cards_nr_generator1 = random.randint(1, 10)
    cards_nr_generator2 = random.randint(1, 10)

    g.display_msg() # Welcome players to the game
    g.get_players(players) # get the player data

    while True:

        g.play_rounds(players)
        choice = input('do you want to play again?  (y=yes, n=no): ').lower()
        if choice in ['y', 'yes']:
            g.setup_new_round(players)
            continue
        elif choice in ['n', 'no']:
            break

    print('Thank you for playing, hope you had fun!')

    g.display_round_summary(players) # Display the game report


if __name__ == "__main__":  # Basically if the name of the module is equal to main
    main()   #  Run this specific program.