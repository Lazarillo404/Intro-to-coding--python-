"""
Created on Sun Mar 16 12:31:17 2025

@author: Mateusz
"""
"""
Program 4 Loops, Decision Statements
For this assignment, write a program that will count specific types of values from two small groups of random numbers.
"""
import random

def main():
    #set random seed to 15 for consistent testing
    random.seed(15)
    print("Output with seed(15)")
    #Generate a random number between 2 and 20 for the first group
    group1 = random.randint(2,20)
    print("The program will generate " + str(group1) + " numbers using a for loop.")
    
    even1 = 0
    odd1 = 0
    zero1 = 0
    output1 = ""
    
    #use a for loop to generate numbers between 0 and 99
    for i in range(group1):
        random99 = random.randint(0,99)
        output1 = output1 + str(random99) + " "
        
        #the number of zero values in the group
        if random99 == 0:
            zero1 = zero1 + 1
        #the number of even values in the group
        elif random99 % 2 == 0:
            even1 = even1 + 1
        #the number of odd values in the group
        else:
            odd1 = odd1 + 1
    
    #print generated numbers and explain how many even, odd, and zeroes there are
    print(output1.strip())
    print("There were " + str(even1) + " even numbers, " + str(odd1) + " odd numbers, and " + str(zero1) + " zeroes in the group of numbers")

    #Generate a random number between 2 and 20 for the second group
    group2 = random.randint(2,20)
    print("The program will generate " + str(group2) + " numbers using a while loop.")
    
    even2 = 0
    odd2 = 0
    zero2 = 0
    output2 = ""
    
    #use a while loop to generate numbers between 0 and 99
    i = 0
    while i < group2:
        random99 = random.randint(0,99)
        output2 = output2 + str(random99) + " "
        
        #the number of zero values in the group
        if random99 == 0:
            zero2 = zero2 + 1
        #the number of even values in the group
        elif random99 % 2 == 0:
            even2 = even2 + 1
        #the number of odd values in the group
        else:
            odd2 = odd2 + 1
        i = i + 1
    
    #print generated numbers and explain how many even, odd, and zeroes there are
    print(output2.strip())
    print("There were " + str(even2) + " even numbers, " + str(odd2) + " odd numbers, and " + str(zero2) + " zeroes in the group of numbers")
    
main()