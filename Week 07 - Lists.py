# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 14:08:29 2025

@author: Mateusz
"""
"""
This program asks the user to input an unknown number of positive numbers.
It will print out all the values and calculate the average.
"""

#Ask user for positive numbers until they type -1.
def get_values(number_list):
    number = input("Please enter a positive number: (-1 to quit): ")
    while number != "-1":
        if int(number) < 0:
            print("Value must be positive")
        else:
            number_list.append(number)
        number = input("Please enter a positive number: (-1 to quit): ")
    return number_list

#Print values of index spots 3, 5, and 8 if they exist.
def print_positions(number_list):
    if len(number_list) > 3:
        print("The value at index 3 is: " + number_list[3])
    else:
        print("The value at index 3 does not exist")
        
    if len(number_list) > 5:
        print("The value at index 5 is: " + number_list[5])
    else:
        print("The value at index 5 does not exist")
        
    if len(number_list) > 8:
        print("The value at index 8 is: " + number_list[8])
    else:
        print("The value at index 8 does not exist")

#Get the sum of all the entered numbers and divide by the total amount of numbers entered to get the average.      
def calculate_average(number_list):
    sum = 0
    for number in number_list:
        sum += int(number)
    average = sum / len(number_list)
    return average

#Print out all of the entered numbers and the average.
def print_list(number_list, average):
    values = ""
    for i in range(len(number_list)):
        values = values + number_list[i] + " "
    print("The values are: " + values.strip())
    print("The average is: " + str(average))
        
def main():
    number_list = []
    get_values(number_list)
    print_positions(number_list)
    average = calculate_average(number_list)
    print_list(number_list, average)
    
main()
