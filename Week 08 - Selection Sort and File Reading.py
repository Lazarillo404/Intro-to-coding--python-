# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 14:07:56 2025

@author: Mateusz
"""
"""
This program will read a set of data representing a series of numeric measurements.
The program will display the data, first unsorted and then sorted, and then compute and display various statistics about the data set. 
"""

def build_list(filename, data_list):
    #open the file for reading
    infile = open(filename, "r")
    
    #Loop through file until there is no more lines
    while True:
        line = infile.readline()
        if not line:
            break
        
        # Remove new line
        line = line.replace("\n", "")
    
        if line != "":
            data_list.append(float(line)) #convert line to float and add to list

    # Close the file
    infile.close()

    # Return the populated list
    return data_list

def print_list(title, data_list):
    #print the title
    print(title)
    print() #empty line
    
    #loop through each number in the list
    for i in range(len(data_list)):
        # Print each value with 2 decimal places, without a newline
        print(f"{data_list[i]:>8.2f}", end="")
        
        #print new line after 8th number
        if (i + 1) % 8 == 0:
            print()
            
    if len(data_list) % 8 != 0:
        print() #empty line

def Sort_list(data_list):
    #sort list manually using selection sort
    print()
    for i in range(len(data_list)):
        min_index = i #assume first number is smallest at the start
        #loop through list to find smallest number
        for j in range(i + 1, len(data_list)):
                if data_list[j] < data_list[min_index]:
                   min_index = j #update smallest number
        if min_index != i: #swap if smallest number is not in current position
            temp = data_list[i]
            data_list[i] = data_list[min_index]
            data_list[min_index] = temp
            
def mean(data_list):
    #calculate average (mean) of list
    total = 0
    for number in data_list:
        total += number
    average = total / len(data_list)
    return average
    
def median(data_list):
    length = len(data_list)
    middle = int(length / 2) #find middle index
    return data_list[middle] #return middle number
    
def main():
    mylist = []
    #build list by reading numbers from file
    mylist = build_list("prog7_nums.txt", mylist)
    
    #print unsorted list
    print_list("Unsorted Set", mylist)
    
    #print sorted list
    Sort_list(mylist)
    print_list("Sorted Set", mylist)
    
    #calculate mean and median and print them
    avg = mean(mylist)
    med = median(mylist)
    print()
    print("Set Statistics")
    print()
    print("Mean:", f"                   {avg:.2f}", "  Median:", f"       {med:.2f}")

    
main()
