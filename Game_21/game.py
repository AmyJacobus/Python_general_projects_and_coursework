#!/usr/bin/env python3

"""
Programmers: Ammishaddai Jacobus
Date: Dec 7, 2021
Description:
"""


# Authorship information # Done by Amy
__author__ = 'Ammishaddai Jacobus'
__version__ = '1.0'
__date__ = 'Dec 10, 2021'
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

    for player, player_data in players.items():
        print(f'Dealing to {player}')
        cards = [cards_nr_generator1, cards_nr_generator2]
        print(f'Cards:', *cards, sep=" ")
        while True:
            choice = input('Do you want another card? (y=yes, n= no): ').lower()
            if choice in ['y', 'yes']:
                cards.append(cards_nr_generator1)
                print(f'cards:', *cards, sep=" ")
                player_data['cards'] = cards
            elif choice in ['n', 'no']:
                cards_total = sum(cards)
                player_data['cards_total'] = cards_total
                print(f'{player} holds at {cards_total} ')
                break

        initial_bet = 0.25
        bet = input('Do you want to double your 25 cent bet? (y=yes, n=no): ')
        if bet in ['y', 'yes']:
            initial_bet += 0.25
        player_data['bet'] = initial_bet
        print(player, player_data)



def dealer(players, cards_nr_generator1,cards_nr_generator2):
    # dealer compared to the highest the higher end
    # checks the highest hand

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

    # print(Dealing to{})
    #
    # # should use while or for loop here
    # input('Do you want another card? (y=yes, n=no): ')
    # print('Cards: RANDOM NR1, RANDOM NR2, RANDOM NR3')
    # # if user says yes, continue to add more cards, until they go over 21 (then they lose!)
    # # if they choose no, display player name, holds at  (Card total)
    #
    # print('Do you want to double your 25 cent beat? (y=yes, n=no): ')
    #
    # # GO TO NEXT PLAYER IN LINE (HOW TO DO THIS)
    # #     If player2 cards_total = 21
    # #         print('BLACKJACK FOR {player2')
    # #     elif player2_cards > 21
    # #         print(f'{player2}\'s card has exceeded 21.')
    # #     elif player2_Cards < 21
    # #         player2 = 'WINNER'
    #
    # # GO TO DEALER HAND, SHOULD HAVE ITS OWN DICTIONARY?
    #     # CARD NUMBERS
    #     # If dealer goes over 21
    #         # - House loses
    #
    # # if dealer_total_card > 21 and player 1 <=21
    # #     print(f'{player1} is a winner!')
    # # if dealer_total_card > 21 and print(f'{player2 <=21} '
    # #     print(f'{player2} is a winner!')


def main():

    players = {}  # We start with an empty dictionary
    cards_nr_generator1 = random.randint(1, 10)
    cards_nr_generator2 = random.randint(1, 10)

    display_msg()
    get_players(players)
    play(players, cards_nr_generator1,cards_nr_generator2)
    # dealer(players, cards_nr_generator1, cards_nr_generator2)


if __name__ == "__main__":  # Basically if the name of the module is equal to main
    main()  # Run this specific program.