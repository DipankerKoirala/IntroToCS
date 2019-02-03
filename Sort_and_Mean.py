#!/usr/bin/python3/env python
"""
Created on Sat Nov 10 15:42:11 2018

@author: Dipanker
"""

Valid = False
#validate user entry
while Valid == False:
    UserInput = (input("Enter a series of integers seperated by commas: "))
    numbers = UserInput.split(',')
    for i in numbers:
        try:
            val = int(i)
            Valid = True
        except:
            print("not a comma separated set of integers, please try again")
            Valid = False
            break

#define a function that sorts and finds the mean:
def Sort_and_Mean(UserInput):
    #print the original list
    OriginalList = 'Original List: ' + UserInput    
    numbers = UserInput.split(',')
    n = len(numbers)
    i = 0
    #for each of the letters in the list, check is it's greater than the next number
    while i < n-1:
        if int(numbers[i]) > int(numbers[i+1]):
            #if it is greater, swap the numbers and change the loop counter back one step
            numbers[i], numbers[i+1] = numbers[i+1],numbers[i]
            if i < 1 :
                i = 0
            else:
                i -= 1
        #if it's not greater move the loop counter up one step
        else:
            i += 1
    #define the sorted list       
    SortedList = 'Sorted List: ' + ','.join(numbers)
    #sum the numbers
    sum = 0
    for i in range(n):
        sum+= int(numbers[i])
    #define the average
    average = sum/n
    MeanValue = 'Mean Value: ' + str(round(average,2))
    #print the answers
    print(OriginalList)
    print(SortedList)
    print(MeanValue)

#call the function
Sort_and_Mean(UserInput)