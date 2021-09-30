#!/usr/bin/env python3

"""
# Programmers: Ammishaddai Jacobus and Rushandy Andrea
# Date: September 12, 2021
# Description: This calculator will take the user's input, their yield, price, and government payment, variable cost,
# and their overhead cost per acre and provide them with a report that gives them the following information. The total
# revenue, the total cost, the earnings, the break even price, per bushel profit, per acre. It also outputs in the
# report, the difference in case of 10% decrease in yield, 10% increase in yield, 10% decrease in costs, and 10%
# increase in cost.
"""

# Authorship
__author__ = 'Ammishaddai Jacobus and Rushandy Andrea'
__version__ = '1.0'
__date__ = 'Sept 12, 2021'
__status__ = 'Development'


def break_even_calculator():

    # GLOBAL VARIABLES??


    def welcome_message():
        print()
        print(f'='*112)
        print()
        print('                                    Break Even Calculator')
        print()
        print('To make use of this calculator, you will need the following data:')
        print('Yield per acre, price per acre, government payment per acre, variable cost per acre and overhead cost per acre.')
        print('The calculator is very asy to use. Type in your data and it will output the results in a report.')
        print(f'='*112)
        print()


    def user_input(yield_per_acre, price_per_acre, government_payment, variable_cost, overhead_cost):
        yield_per_acre = float(input("Please type in the yield per acre: "))
        price_per_acre = float(input("Please type in the price per acre: "))
        government_payment = float(input("Please type in the government payment per acre: "))
        variable_cost = float(input("Please type in the variable cost per acre: "))
        overhead_cost = float(input("Please type in the overhead cost per acre "))
        print()
        print(f'='*112)
        print()

    def calculate_column_1():
        total_revenue = (yield_per_acre * price_per_acre) + government_payment
        total_cost = (variable_cost + overhead_cost)
        total_earnings = (total_revenue - total_cost)
        break_even_price = round((total_cost - government_payment) / yield_per_acre, 2)
        total_bushel_profit = (price_per_acre - break_even_price)


    def calculate_column_data():# Calculations row 2,3,4 and 5
        yield_row_2 = round(yield_per_acre * 0.9, 2)  # (10% decrease in yield)
        yield_row_3 = round(yield_per_acre * 1.1, 2)  # (10% increase in yield)
        variable_cost_row_4 = round(variable_cost * 0.9, 2)  # (10% decrease in cost)
        variable_cost_row_5 = round(variable_cost * 1.1, 2)  # (10% increase in cost)
        overhead_cost_row_4 = round(overhead_cost * 0.9, 2)  # (10% decrease in cost)
        overhead_cost_row_5 = round(overhead_cost * 1.1, 2)  # (10% increase in cost)
        total_revenue_row_2 = round((yield_row_2 * price_per_acre) + government_payment, 2)  # (10% decrease in yield)
        total_revenue_row_3 = round((yield_row_3 * price_per_acre) + government_payment, 2)  # (10% increase in yield)
        total_cost_row_4 = round(variable_cost_row_4 + overhead_cost_row_4, 2)  # (10% decrease in yield)
        total_cost_row_5 = round(variable_cost_row_5 + overhead_cost_row_5, 2)  # (10% increase in yield)
        total_earnings_row_2 = round(total_revenue_row_2 - total_cost, 2)  # (10% decrease in yield)
        total_earnings_row_3 = round(total_revenue_row_3 - total_cost, 2)  # (10% increase in yield)
        total_earnings_row_4 = round(total_revenue - total_cost_row_4, 2)  # (10% decrease in yield)
        total_earnings_row_5 = round(total_revenue - total_cost_row_5, 2)  # (10% increase in yield)
        break_even_price_row_2 = round((total_cost - government_payment) / yield_row_2, 2)  # (10% decrease in yield)
        break_even_price_row_3 = round((total_cost - government_payment) / yield_row_3, 2)  # (10% increase in yield)
        break_even_price_row_4 = round((total_cost_row_4 - government_payment) / yield_per_acre, 2)  # (10% decrease in yield)
        break_even_price_row_5 = round((total_cost_row_5 - government_payment) / yield_per_acre, 2)  # (10% increase in yield)
        total_bushel_profit_row_2 = (price_per_acre - break_even_price_row_2)  # (10% decrease in yield)
        total_bushel_profit_row_3 = (price_per_acre - break_even_price_row_3)  # (10% increase in yield)
        total_bushel_profit_row_4 = (price_per_acre - break_even_price_row_4)  # (10% decrease in yield)
        total_bushel_profit_row_5 = (price_per_acre - break_even_price_row_5)  # (10% increase in yield)

    def user_data_entry_review(yield_per_acre, price_per_acre, government_payment,variable_cost,overhead_cost): # Display message to user
        print("Here is the data you have inserted: ")
        print(f"Yield per acre:                  {yield_per_acre}")
        print(f"Price per acre:                  {price_per_acre}")
        print(f"Government payment per acre:     {government_payment}")
        print(f"variable_cost per acre:          {variable_cost}")
        print(f"Overhead cost per acre:          {overhead_cost}")
        print(" ")
        print("Below you will find your full report.")
        print(" ")
        print(f'='*112)


    def output_report_menu(): # Output report [Menu]
        print(" ")
        print(
              f'{"":20s}'
              f'{"":15s}'
              f'{"10% Decrease":>15s}'
              f'{"10% Increase":>15s}'
              f'{"10% Decrease":>15s}'
              f'{"10% Increase":>15s}')
        print(f'{"BreakEven Calculator":20}'
              f'{"Per acre":>15s}'
              f'{"in Yield":>15s}'
              f'{"in Yield":>15s}'
              f'{"in cost":>15s}'
              f'{"in cost":>15s}')
        print(" ")
        print(f'='*112)

    def output_data_entry_rows_and_columns():  # Output report results [Menu]
        print(f'{"Yield":<20s}'
              f'{yield_per_acre:15,.2f}'
              f'{yield_row_2:15,.2f}'
              f'{yield_row_3:15,.2f}'
              f'{yield_per_acre:15,.2f}'
              f'{yield_per_acre:15,.2f}')
        print(f'{"Price":20s}'
              f'{price_per_acre:15,.2f}'
              f'{price_per_acre:15,.2f}'
              f'{price_per_acre:15,.2f}'
              f'{price_per_acre:15,.2f}'
              f'{price_per_acre:15,.2f}')
        print(f'{"Government Payment":20s}'
              f'{government_payment:15,.2f}'
              f'{government_payment:15,.2f}'
              f'{government_payment:15,.2f}'
              f'{government_payment:15,.2f}'
              f'{government_payment:15,.2f}')
        print(f'{"Total Revenue":20s}'
              f'{total_revenue:15,.2f}'
              f'{total_revenue_row_2:15,.2f}'
              f'{total_revenue_row_3:15,.2f}'
              f'{total_revenue:15,.2f}'
              f'{total_revenue:15,.2f}')
        print(f'{"Variable Cost":20s}'
              f'{variable_cost:15,.2f}'
              f'{variable_cost:15,.2f}'
              f'{variable_cost:15,.2f}'
              f'{variable_cost_row_4:15,.2f}'
              f'{variable_cost_row_5:15,.2f}')
        print(f'{"Overhead Cost":20s}'
              f'{overhead_cost:15,.2f}'
              f'{overhead_cost:15,.2f}'
              f'{overhead_cost:15,.2f}'
              f'{overhead_cost_row_4:15,.2f}'
              f'{overhead_cost_row_5:15,.2f}')
        print(f'{"Total Cost":20s}'
              f'{total_cost:15,.2f}'
              f'{total_cost:15,.2f}'
              f'{total_cost:15,.2f}'
              f'{total_cost_row_4:15,.2f}'
              f'{total_cost_row_5:15,.2f}')
        print(f'{"Earnings":20s}'
              f'{total_earnings:15,.2f}'
              f'{total_earnings_row_2:15,.2f}'
              f'{total_earnings_row_3:15,.2f}'
              f'{total_earnings_row_4:15,.2f}'
              f'{total_earnings_row_5:15,.2f}')
        print(f'{"BreakEven Price":20s}'
              f'{break_even_price:15,.2f}'
              f'{break_even_price_row_2:15,.2f}'
              f'{break_even_price_row_3:15,.2f}'
              f'{break_even_price_row_4:15,.2f}'
              f'{break_even_price_row_5:15,.2f}')
        print(f'{"Per Bushel Profit":20s}'
              f'{total_bushel_profit:15,.2f}'
              f'{total_bushel_profit_row_2:15,.2f}'
              f'{total_bushel_profit_row_3:15,.2f}'
              f'{total_bushel_profit_row_4:15,.2f}'
              f'{total_bushel_profit_row_5:15,.2f}')

        def goodbye_message():
            print(" ")
            print(f'='*112)
            print(" ")
            print("Thank you for making use of our break even calculator.")

        def main():

        if __name__ == "__main__":
            main()

