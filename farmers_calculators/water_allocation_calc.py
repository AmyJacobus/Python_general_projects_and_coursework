#!/usr/bin/env python3 # Done by Amy

""""
Programmers: Ammishaddai Jcobus and Ben Sadler #Amy
Date: Sept 26, 2021 # Amy
Description: Determine when the allocation of water will be used up in days. # Ben Sadler
This program makes use of 3 data input from the user, which are the rationed allocation depth, #done by Amy
the area being irrigated and the average rate of flow. It will runs this information through
a calculation algorithm and provide the user with the result of the amount of days that it will
take the water allocation to be used up.
"""

import validation as v # importing the module validation with the namespace v

# Authorship information # Done by Amy
__author__ = 'Ammishaddai Jacobus and Ben Sadler'
__version__ = '1.0'
__date__ = 'Sept 21, 2021'
__status__ = 'Development'


def water_allocation_calculator():
    """
    DOCSTRING
    :return: n/a
    """

    # Welcome message with information about the calculator and instructions
    print()
    print(f'{"="*104}')
    print()
    print(f"{'WELCOME':>50s}")
    print()
    print('This program will help determine when the allocation of water you have will be used up in days')
    print('To make use of this calculator, you will need the following data:')
    print('(1)rationed allocation depth (2) Area being irrigated (3)average rate of flow')
    print(f'{"="*104}')
    print()

    while True:  # While loop to ask the user if they want to calculate again

        # User Input with while loop for validation
        while True:
            # rationed_allocation_depth = int(input(f"{'Please input the depth (D) in inches: ':>100s}"))
            rationed_allocation_depth = v.get_range(prompt= 'Please input the depth (D) in inches',low=0,high=100,)
            if rationed_allocation_depth > 0:  # Amy
                break
            else:
                print(f"{'Please insert a value bigger than 0, please no letters or characters. Try again!':>100s}")

        while True:
            area_being_irrigated = (int(input(f"{'Please input the area being irrigated in acres (A): ':>100s}")))  # Ben
            if area_being_irrigated > 0:  # Amy
                break
            else:
                print(f"{'Please insert a value bigger than 0, please no letters or characters. Try again!':>100s}")

        while True:
            average_rate_of_flow = int(input(f"{'Please input the average rate of flow in U.S GPM: ':>100s}"))  # Ben Sadler
            if average_rate_of_flow > 0:
                break
            else:
                print(f"{'Please insert a value bigger than 0, please no letters or characters. Try again!':>100s}")  # Ben
        print()
        print(f'{"=" * 104}')

        #  Output results  done by Ben and updated and formatted by amy
        time_in_days = (18.857 * rationed_allocation_depth * area_being_irrigated) / average_rate_of_flow
        print(f'The allocation of water will be used up in [{round(time_in_days, 1)} days] when [{area_being_irrigated} '
              f'acres is irrigated] with \nan irrigation system that has an [average rate flow of {average_rate_of_flow} '
              f'US GPM] system capacity and the rationed\nallocation depth is [{rationed_allocation_depth} inches.]')
        print()

        # Ask again if user would like to make another calculation. Done by Amy
        re_use = input("Would you like to make another calculation? [Yes/No]: ").lower()
        if re_use == "yes":
            print()
            print(f'{"=" * 104}')
            print()
            continue
        else:
            break
    # Big main while loop ends here

    # Goodbye message for user
    print()
    print(f'{"=" * 104}')
    print()
    print("Thanks for using our water allocation calculator! End of program! :)")

    # CODE IN YOUR OWN WORDS
    if __name__ == "__main__":
        water_allocation_calculator()