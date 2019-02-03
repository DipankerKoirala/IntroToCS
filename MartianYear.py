#!/usr/bin/python3/env python

#the the year variable to be blank
year = ""
#start the while loop when the input is not "exit"
while year != "exit":
    #ask the user for input
    year = input("Enter a year or type exit: ")       
    #check if the year is numeric
    if year.isnumeric():
        #check is the year is even, and if it is, is it divisble by 10
        if int(year)%2 == 0:
            if int(year)%10 == 0:
                print("This is a Martian leap year")
            else:
                print("This is not a Martian Leap year")
        #else the year is odd - so it is a Martian leap year
        else:
            print("This is a Martian leap year")
    #check if user input is "exit"
    elif year.lower() == 'exit':
        print("Goodbye")
        break
    #else throws an error
    else:
        print("I do not understand")

        