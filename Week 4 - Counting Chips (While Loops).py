"""
Created on Sun Mar  9 17:11:50 2025

@author: Mateusz
"""
"""
This program is a two-person chip game. The game starts with a pile of chips. Each player takes turns picking up at least 1 chip and at most half of the current pile. This continues until one player takes the last chip. The player who takes the last chip wins the game.
The purpose of this program is to demonstrate the use of loops and decision structures while providing additional practice in reading user input and writing output.
"""

def main():
    #Print brief instructions for the game.
    print("Rules: The game starts with a pile of chips. Each player may only take at most half of the chips. The player that gets the last chip wins. Good luck!")
    print("")
    #Prompt the two players for their first names.
    player1 = input("Player 1 please enter your first name: ")
    player2 = input("Player 2 please enter your first name: ")
    print("")
    
    #Determin which player goes first
    current_player = player1
    
    #Prompt for the number of chips to start the game.
    total_chips = int(input("How many chips would you like to start with? "))
        
    #Loop while chips are in pile    
    while total_chips > 0:
        #most chips that can be taken
        limit = (total_chips + 1) //2
        print ("")
        #ask how many chips to take
        chips_taken = int(input(str(current_player) + " how many of the remaining " + str(total_chips) + " chip(s) would you like " + "(" + str(int(limit)) + " max)? "))
        #validate the amount of chips taken
        while chips_taken < 1 or chips_taken > limit:
            chips_taken = int(input("Invalid ERROR: invalid number of chips. Try again: "))
        #take away from total chips
        total_chips = total_chips - chips_taken
        # Check if the game is over
        if total_chips == 0:
            print("")
            print("")
            print("Congratulations " + current_player + "! You won!")
            
        #Switch players
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1
        
main()