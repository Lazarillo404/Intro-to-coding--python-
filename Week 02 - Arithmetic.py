# -*- coding: utf-8 -*-
"""
CIS 106         Program 1     

Programmer: Mateusz

Date Due: Next Sunday after it was assigned by 11:59 PM

Purpose: The purpose of this program is to calculate compound 
         interest over a 4 year period. The user is prompted 
         for the initial investment amount and the annual interest
         rate for the investment. 
"""

def main():
    #prompt the user for the initial investment amount for the account
    initial_investment = float(input("How much is your initial investment amount for the account? "))
    
    #prompt the user for the annual interest rate
    interest_rate = float(input("How much is the annual interest rate? "))
    
    #use the initial investment and interest rate to calculate the future value of the account
    value_for_year_1 = initial_investment + (initial_investment*interest_rate/100)
    value_for_year_2 = value_for_year_1 + (value_for_year_1*interest_rate/100)
    value_for_year_3 = value_for_year_2 + (value_for_year_2*interest_rate/100)
    value_for_year_4 = value_for_year_3 + (value_for_year_3*interest_rate/100)
    future_value_of_the_account = round(value_for_year_4, 2)
    
    print("**************************************")
    print("           Investment Result")
    print("**************************************")
    print("")
    print("Initial Amount: " + str(initial_investment))
    print("Interest Rate: " + str(interest_rate))
    print("Final Value: " + str(future_value_of_the_account))

main()
