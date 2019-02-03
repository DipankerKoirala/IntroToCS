#!/usr/bin/python3/env python
"""
Created on Tue Nov 13 18:11:56 2018

@author: Dipanker
"""
prompt_line1 = "|A1|A2|A3|"
prompt_line2 = "|B1|B2|B3|"
prompt_line3 = "|C1|C2|C3|"

#show the user the entry keys
print("Welcome to tic tac toe. You can make an entry in the square of your choice by using the below keys:")
print(prompt_line1)
print(prompt_line2)
print(prompt_line3)

#build a library with the values set to blank
gd = {'A1':' ','A2':' ','A3':' ','B1':' ','B2':' ','B3':' ','C1':' ','C2':' ','C3':' '}

#define a function to take a user key entry and update the value in the grid
def make_entry(UserInput, entry):
    #if the userinput exists as a key:
    if UserInput.upper() in gd:
            #and the square is blank
            if gd[UserInput.upper()] == ' ':
                #update and print the game board
               gd[UserInput.upper()] = entry
               print("|"+gd['A1']+"|"+gd['A2']+"|"+gd['A3']+"|")
               print("|"+gd['B1']+"|"+gd['B2']+"|"+gd['B3']+"|")
               print("|"+gd['C1']+"|"+gd['C2']+"|"+gd['C3']+"|")
               #have the function return 1
               return 1
            #if the square is 0, have the function ask for another entry and return 0
            else:
                print("square is already taken, please try again: ")
                return 0
    #if user input does not exist as a key, ask for another entry
    else:
            print("Invalid Entry, try again: ")
            return 0
#define a function that checks all the winning conditions
def win_condition():
    if gd['A1'] == gd['A2'] == gd['A3'] !=' ':
        return True
    elif gd['B1'] == gd['B2'] == gd['B3'] !=' ':
        return True
    elif gd['C1'] == gd['C2'] == gd['C3'] !=' ':
        return True
    elif gd['A1'] == gd['B2'] == gd['C3'] !=' ':
        return True
    elif gd['A3'] == gd['B2'] == gd['C1'] !=' ':
        return True  
    elif gd['A1'] == gd['B1'] == gd['C1'] !=' ':
        return True
    elif gd['A2'] == gd['B2'] == gd['C2'] !=' ':
        return True
    elif gd['A3'] == gd['B3'] == gd['C3'] !=' ':
        return True   

#define a function that checks if all the squares are taken
def draw_condition():
    for key in gd:
        if gd[key] == ' ':
            return False
    return True
       
#set the starting parameters for the main game loop    
player_counter = 0
game_end = False

while game_end == False:
    #if player counter is even - ask player 1 for an entry
    if player_counter % 2 == 0:
        UserInput = (input("Player 1 make an entry: "))
        entry = 'x'
        #call the function to validate entry and update the grid
        player_counter += make_entry(UserInput, entry)
        #check if the win condition function returns True
        if win_condition() == True:
            game_end = True
            print("Player 1 has won the game!")
            Play_again = (input("Would you like to play again? [Y/N]? "))
            if Play_again.upper() == str('Y'):
               gd = {'A1':' ','A2':' ','A3':' ','B1':' ','B2':' ','B3':' ','C1':' ','C2':' ','C3':' '}
               player_counter = 0
               game_end = False
            else:
                game_end = True
                break
    #if player counter is odd - ask player 2 for an entry    
    else:
        UserInput = (input("Player 2 make an entry: "))
        entry = 'o'
        #call the function to validate entry and update the grid
        player_counter += make_entry(UserInput, entry)
        #check if the win condition function returns True
        if win_condition() == True:
            game_end = True
            print("Player 2 has won the game!")
            Play_again = (input("Would you like to play again? [Y/N]? ")) 
            if Play_again.upper() == str('Y'):
                gd = {'A1':' ','A2':' ','A3':' ','B1':' ','B2':' ','B3':' ','C1':' ','C2':' ','C3':' '}
                player_counter = 0
                game_end = False
            else:
                game_end = True
                break
    #call the draw condition function to see if the game is a draw
    if draw_condition() == True:
        print("The game ended in a draw")
        Play_again = (input("Would you like to play again? [Y/N]? ")) 
        if Play_again.upper() == str('Y'):
                gd = {'A1':' ','A2':' ','A3':' ','B1':' ','B2':' ','B3':' ','C1':' ','C2':' ','C3':' '}
                player_counter = 0
                game_end = False
        else:
                game_end = True
                break
