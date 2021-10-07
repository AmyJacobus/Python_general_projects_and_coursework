#!/usr/bin/env python3

""""
Programmers: Ammishaddai Jcobus
Date: Sept 26, 2021 # Amy
Description: Determine when the allocation of water will be used up in days. This program will output the results based
on the data of  1), 2), 3) and will output the number of days. It will also during the input process, ask you if you
would like to reset all the data, in case that the user has inserted a wrong number or character. The user also gets
the option to re-use the calculator, to make another calculation if they want.

"""

# Authorship information # Amy
__author__ = 'Ammishaddai Jacobus and Ben Sadler'
__version__ = '1.0'
__date__ = 'Sept 12, 2021'
__status__ = 'Development'

# Start main program here
print('Welcome! This program will help determine when the allocation of water you have will be used up in days!')
# Ben Sadler
print(f':30s: You will need the following data: The rationed allocation depth in inches,\
the area being irrigated in acres , and the average rate of flow in U.S gpm.')

while True:  # While loop to ask the user if they want to calculate again

    while True:

        # User Input
        while True:  # while for validation, to check if the user has entered a number higher than 0
            rationed_allocation_depth = int(input('Please input the depth (D) in inches: '))  # Ben Sadler
            if rationed_allocation_depth > 0:  # Amy
                break
            else:
                print('Please insert a value bigger than 0, please no letters or characters. Try again!')

        while True:  # while for validation, to check if the user has entered a number higher than 0
            area_being_irrigated = (int(input('Please input the area being irrigated in acres (A): ')))  # Ben Sadler
            if rationed_allocation_depth > 0:  # Amy
                break
            else:
                print('Please insert a value bigger than 0, please no letters or characters. Try again!')

        while True:  # while for validation, to check if the user has entered a number higher than 0
            average_rate_of_flow = int(input('Please input the average rate of flow in U.S GPM: '))  # Ben Sadler
            if average_rate_of_flow > 0: # Ben
                break
            else:
                print('Please insert a value bigger that, please no letters or characters. Try again!')  # Ben Sadler

        # reset or calculate request:
        calculate_or_rest = input('Would you like to continue with the calculation or reset the data and try again?'
                                  ' [c/r]: ').lower()
        if calculate_or_rest == 'c':
            break
        elif calculate_or_rest == 'r':
            print('Resetting the calculator for you.')
            print()
            continue

    # Calculations done by Ben
    time_in_days = round((18.857 * rationed_allocation_depth * area_being_irrigated) / average_rate_of_flow, 1)

    # Output results done by Ben & Amy
    print(f'The allocation of water will be used up in [{time_in_days} days] when [{area_being_irrigated} acres] is '
          f'irrigated with an irrigation system that has an average of [{average_rate_of_flow} US gpm] system capacity '
          f'and the rationed allocation depth is [12 inches]. ')  # Ben Sadler

    # Ask again - Done by Amy
    re_use = input("Would you like to make another calculation? [yes/no]: ").lower()
    if re_use == "yes":
        continue
    else:
        break

# while loop ends here

# Good bye message
print('Thank you for making use of our calculator.')
