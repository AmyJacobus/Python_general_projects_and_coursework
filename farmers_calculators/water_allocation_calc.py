#!/usr/bin/env python3 # Done by Amy

""""
Programmers: Ammishaddai Jcobus
Date: Oct 6, 2021, 2021
Description: Determine when the allocation of water will be used up in days.
This program makes use of 3 data input from the user, which are the rationed allocation depth, #done by Amy
the area being irrigated and the average rate of flow. It will runs this information through
a calculation algorithm and provide the user with the result of the amount of days that it will
take the water allocation to be used up.
"""

import validation as v  # importing the module validation with the namespace v

# Authorship information # Done by Amy
__author__ = 'Ammishaddai Jacobus'
__version__ = '2.0'
__date__ = 'Oct 6, 2021'
__status__ = 'Development'


def water_allocation_calculator():
    """
    This function display a welcome message to the user. Then takes several input from the user, uses
    the function get range from the imported module validation, to validate if the user has input the
    right datatype and the right range. Also uses a while loop around each input prompt to check if they are
    bigger than 0. Then proceeds to calculate the water allocated and in how many days it will be used up.
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
            rationed_allocation_depth = v.get_range(prompt='Please input the depth (D) in inches ', low=0, high=100)
            if rationed_allocation_depth > 0:  # Amy
                break
            else:
                print(f"{'Please insert a value bigger than 0, please no letters or characters. Try again!':>100s}")

        while True:
            area_being_irrigated = v.get_range(prompt='Please input the area being irrigated in acres (A) ', low=1,
                                               high=2147483647)
            if area_being_irrigated > 0:  # Amy
                break
            else:
                print("Please insert a value bigger than 0, please no letters or characters. Try again!")

        while True:
            average_rate_of_flow = v.get_range(prompt='Please input the average rate of flow in U.S GPM: ', low=1,
                                               high=2147483647)
            if average_rate_of_flow > 0:
                break
            else:
                print("Please insert a value bigger than 0, please no letters or characters. Try again!")
        print()
        print(f'{"=" * 104}')

        #  Output results  done by Ben and updated and formatted by amy
        time_in_days = (18.857 * rationed_allocation_depth * area_being_irrigated) / average_rate_of_flow
        print(f'The allocation of water will be used up in [{round(time_in_days, 1)} days] when'
              f'[{area_being_irrigated} acres is irrigated] with an irrigation\n system that has an'
              f'[average rate flow of {average_rate_of_flow} [US GPM] system capacity and the rationed allocation '
              f'depth\n is [{rationed_allocation_depth} inches.]')
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


if __name__ == "__main__":  # Basically if the name of the module is equal to main
    water_allocation_calculator()  # Run this specific program.
