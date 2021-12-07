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

    # players = {}  # We start with an empty dictionary

    # How do we add to the dictionary with while loops? SINCE DEBBIES EXAMPLE IS LIKE A 2D/3D dictionary
    print()
    print('=' * LINE_LENGTH)
    print('Now lets get this game setup.  Who is all playing?')
    print('Please enter a player\'s name or enter \'done\' when finished.')
    print()

    while True:
        player = input('Enter name: ').lower()  # NEEDS FORMATTING F-STRING
        if player != 'done':
            player = player.title()
            players[player] = {"cash": 1.0}
        elif player == 'done':
            return players


def play(players, cards_nr_generator1,cards_nr_generator2):
    print()
    print('=' * LINE_LENGTH)
    print('Starting game...')
    print('=' * LINE_LENGTH)
    print()

    # cards_nr_generator1 = random.randint(1, 10)
    # cards_nr_generator2 = random.randint(1, 10)

    for player in players.keys():
        print(f'Dealing to {player}')
        cards = [cards_nr_generator1, cards_nr_generator2]
        print(f'Cards:', *cards, sep=" ")
        while True:
            choice = input('Do you want another card? (y=yes, n= no): ').lower()
            if choice in ['y', 'yes']:
                cards.append(cards_nr_generator1)
                print(f'cards:', *cards, sep=" ")
                players[player] = {"cards": cards }
            elif choice in ['n', 'no']:
                cards_total = sum(cards)
                players[player] = {"cards_total": cards_total}
                print(f'{player} holds at {cards_total} ')
                break
        while True:
            initial_bet = 0.25
            bet = input('Do you want to double your 25 cent bet? (y=yes, n=no): ')
            if bet in ['y', 'yes']:
                initial_bet += 0.25
                players[player] = {"bet": initial_bet}
                return False
            else:
                return False


def dealer(players, cards_nr_generator1,cards_nr_generator2):

    print('Dealing to the dealer')
    cards = [cards_nr_generator1, cards_nr_generator2]
    print(f'Cards:', *cards, sep=" ")

    dealer_total = sum(cards)
    if dealer_total == 21:
        print('Dealer is a winner!')
        # all players lose!
    elif dealer_total > 21:
        for player in players.keys():
            bet = players[player]["bet"]
            cash = players[player]["cash"]
            new_cash = cash - bet
            print(f'{player} lost this round!')
            print(f'{player}\'s new balance is ${new_cash}')


def main():

    players = {}  # We start with an empty dictionary
    cards_nr_generator1 = random.randint(1, 10)
    cards_nr_generator2 = random.randint(1, 10)

    display_msg()
    get_players(players)
    dealer(players, cards_nr_generator1, cards_nr_generator2)


if __name__ == "__main__":  # Basically if the name of the module is equal to main
    main()   # Run this specific program.