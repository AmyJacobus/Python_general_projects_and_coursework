#!/usr/bin/env python3

"""
Programmers: Ammishaddai Jacobus
Date: Dec 16, 2021
Description:
"""

# Authorship information # Done by Amy
__author__ = 'Ammishaddai Jacobus'
__version__ = '1.0'
__date__ = 'NEED TO BE DONE'
__status__ = 'Development'


import random  # Imports random so we it can be used to generate random numbers
import game as g  # Imports the game module as g to be used in this main module


def main():
    """
    This function starts with the an empty player dictionary, that later gets populated with all the players and
    their data. The main runs the functions to display the game intro message, the function to get all the players,
    then it uses a while true, which runs the game round, displays the game round summary at the end of each round
    checks if the user wants to play again, if they do want to play again, it clears everything and add starts the
    round again with the original players data. Once the player says no to play any more round, it will break out
    of the while loop and thank the player for playing and that hopefully they had fun. And displays the summary
    of that last round.
    :return: n/a
    """

    players = {}  # We start with an empty dictionary
    cards_nr_generator1 = random.randint(1, 10)
    cards_nr_generator2 = random.randint(1, 10)

    g.display_msg() # Welcome players to the game
    g.get_players(players) # get the player data

    while True:

        g.play_rounds(players)
        g.display_round_summary(players)
        choice = input('do you want to play again?  (y=yes, n=no): ').lower()
        if choice in ['y', 'yes']:
            g.setup_new_round(players)
            continue
        elif choice in ['n', 'no']:
            break

    print('Thank you for playing, hope you had fun!')

    g.display_round_summary(players)  # Display the game report


if __name__ == "__main__":  # Basically if the name of the module is equal to main
    main()   #  Run this specific program.