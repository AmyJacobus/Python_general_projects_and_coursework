#!/usr/bin/env python3


"""
Programmers: Ammishaddai Jacobus
Date: Dec 16, 2021
Description: This is the game module. Different functions to run Game 21. Displaying the message function, get the
players function to get all the players, play function to actually play the round, dealer function to play deal to the
dealer if there are still players in the game that is, a function to display all the winners, a function to display
the each round summary, a function to play each round and a function for setup new round. All these functions make
the game 21 run properly.
"""


# Authorship information # Done by Amy
__author__ = 'Ammishaddai Jacobus'
__version__ = '1.0'
__date__ = 'Dec 10, 2021'
__status__ = 'Development'


import random
import validation as v


LINE_LENGTH = 100


def display_msg():
    """
    This function display the welcome message and game rules to the user.
    :return: n/a
    """
    print('$' * LINE_LENGTH)
    print()
    print('                                    WELCOME TO GAME 21')
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
            players[player] = {
                'cash': 1.0,
                'cards': [],
                'cards_total': 0,
                'bet': 0.25
            }
        elif player == 'done':
            return players


def play(players, cards_nr_generator1, cards_nr_generator2):
    """
    This function basically runs the main play part of the game. If checks if players have cash to play a round at all.
    If so, it deals cards to the players, until they exceed 21 or decide to hold. Once they hold, it checks if they want
    to double their bet, if not, the process of this function ends there.
    :param players: Makes use of the paramater dictionary data from other functions
    :param cards_nr_generator1: Makes use of the this data to generate random card numbers
    :param cards_nr_generator2:  Makes use of the this data to generate random card numbers
    :return: n/a
    """
    print()
    print('=' * LINE_LENGTH)
    print('Starting round...')
    print('=' * LINE_LENGTH)
    print()

    for player, player_data in players.items():
        cash, cards, cards_total, bet = player_data.values()

        if cash < 0.25:
            print(f'{player} is out ')
            continue

        print(f'Dealing to {player}')

        cards_nr_generator1 = random.randint(1, 10)
        cards_nr_generator2 = random.randint(1, 10)

        cards = [cards_nr_generator1, cards_nr_generator2]
        player_data['cards'] = cards
        print(f'Cards:', *cards, sep=" ")

        initial_bet1 = 0.25
        while True:
            cards_total = sum(cards)
            player_data['cards_total'] = cards_total
            if cards_total > 21:  # CHECKS IF PLAYER HAS EXCEEDED THE GAME LIMIT AND GET THEM OUT OF THE GAME IF SO
                print(f'{player} has exceeded 21! You lose!')
                loss = cash - 0.25
                player_data['cash'] = loss
                print()
                break

            choice = v.get_yes_no(prompt='Do you want another card? (y=yes, n= no): ').lower()
            if choice in ['y', 'yes']:
                cards_nr_generator = random.randint(1, 10)
                cards.append(cards_nr_generator)
                print(f'cards:', *cards, sep=" ")
                player_data['cards'] = cards
            elif choice in ['n', 'no']:
                print(f'{player} holds at {cards_total} ')
                break

        if cards_total > 21:
            continue

        initial_bet = 0.25
        print()
        bet = input('Do you want to double your 25 cent bet? (y=yes, n=no): ')
        if bet in ['y', 'yes']:
            print(f'Bet doubled for {player}')
            initial_bet += 0.25
        player_data['bet'] = initial_bet
        print()


def dealer(players):
    """
    This function does the process of dealing to the dealer. It first checks if the players have not exceeded 21,if they
    have, the dealer wins. If the number of players still in the game is 0, means the dealer wins too. Otherwise cards
    are dealt to the dealer until he reaches 21 or goes over 21, which in that case he loses.
    :param players: This functions makes use of the paramater players data
    :return: n/a
    """

    num_players_out = 0
    highest_hand = 0

    # CHECK IF ANY OF THE PLAYERS HAVEN'T EXCEEDED 21
    # IF SO HE WINS
    for player, player_data in players.items():
        cards_total = player_data['cards_total']
        if cards_total > 21:
            num_players_out += 1
        elif cards_total > highest_hand:
            highest_hand = cards_total

    if num_players_out == len(players):
        print('All players exceeded 21, so dealer automatically WINS!')
        print()
        return 21  # Return 21 because the dealer wins, we need the data for later

    print()
    print('Dealing to dealer')
    print()

    dealer_cards = []
    dealer_cards_total = 0

    while dealer_cards_total < 21 or highest_hand > dealer_cards_total:
        card = random.randint(1, 10)
        dealer_cards.append(card)
        dealer_cards_total += card
        print(dealer_cards_total)
    print(f'Dealer\'s cards:', *dealer_cards, sep=" ")

    if dealer_cards_total > 21:
        print('Dealer\'s hand exceed 21!')
    else:
        print(f'cards:', *dealer_cards, sep=" ")

    return dealer_cards_total


def display_winners(players, dealers_cards_total):
    """
    This function display the winners of each round. It starts by checking is the players have enough funds to play
    a round, if they player cards are over 21, dealer wins. If the players cards are below 21 or equal t0 21, it increase
    the winner and add the winning funds to the players total and declare the player as the winner.
    :param players: Uses the players dictionary
    :param dealers_cards_total: Takes the dealers cards total to use in this function
    :return: n/a
    """

    total_winners = 0

    for player, player_data in players.items():

        cash, cards, cards_total, bet = player_data.values()

        if cash < 0.25:
            continue

        if dealers_cards_total > 21:
            if cards_total <= 21:
                total_winners += 1
                player_data['cash'] += bet
                print(player, 'is a winner!')
            else:
                player_data['cash'] -= bet
        else:
            print('Dealer wins!')


def display_round_summary(players):
    """
    This function will display the round summary and how much money each player has currently.
    :param players: 2D dictionary of all player's data
    :return: number of players who still have cash
    """

    print()
    print('End of Round Summary')
    print('=' * LINE_LENGTH)

    for player, player_data in players.items():

        cash, cards, cards_total, bet = player_data.values()

        print(f'{player:<5s} balance is ${cash}')

    print()

    return cash

def play_rounds(players):
    """
    This module basically is one round, this module runs all the rounds every time the user wants to play a new round.
    It plays the cards for each players, it checks if there are still players that havent reached 21 or lost, and if so,
    it will deal cards to the dealer and at the end display the winner of the round.
    :param players: This is the dictionary paramater that this function needs to run
    :return: n/a
    """

    cards_nr_generator1 = random.randint(1, 10)
    cards_nr_generator2 = random.randint(1, 10)

    # setup_new_round(players)
    play(players, cards_nr_generator1, cards_nr_generator2)
    dealers_card_total = dealer(players)  # storing data in variable
    display_winners(players, dealers_card_total)


def setup_new_round(players):
    """
    Basically this function is suppose to works as some sort of clear, back to default command. Basically it defaults
    all the player's data. Like it's cash goes back to 1.0 and cards_total to 0.
    """
    for player in players:
        players[player] = {
            'cash': 1.0,
            'cards': [],
            'cards_total': 0,
            'bet': 0.25
        }


def main():
    """
    This is the main function in this module that we use for testing that all the functions in the module works properly.
    :return: n/a
    """

    players = {}  # We start with an empty dictionary
    cards_nr_generator1 = random.randint(1, 10)
    cards_nr_generator2 = random.randint(1, 10)

    play_rounds(players)
    # display_msg()
    # get_players(players)
    # # START WHILE PLAY AGAIN HERE.
    # play(players, cards_nr_generator1, cards_nr_generator2)
    # dealers_card_total = dealer(players)  # storing data in variable
    # display_winners(players, dealers_card_total)


if __name__ == "__main__":  # Basically if the name of the module is equal to main
    main()