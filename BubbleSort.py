#!/usr/bin/python3/env python
Valid = False
#Get user input and validate entry
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
#print the user-inputted list   
original_list = 'Original List: ' + ','.join(numbers)
print(original_list)

#set initial parameters for the sorting loop
loopcounter = 0
sorted = False
n = len(numbers)
while sorted == False:    
    for i in range(n-1):
        #check if each number in the input is greater than the next number
        if int(numbers[i]) > int(numbers[i+1]):
            #if this condition is met, start the next sorting loop
            loopcounter += 1
            for i in range (n-1):
                #if the current number is larger than the next number, swap the numbers
                if int(numbers[i]) > int(numbers[i+1]):
                    numbers[i], numbers[i+1] = numbers[i+1],numbers[i]
            #print the current loop
            print('Pass '+ str(loopcounter) + ': ' + ','.join(numbers))
            sorted = False
            break
        #if each number is smaller than the next number, set Sorted = True
        else:
            sorted = True

#print your ultimate outputs          
print(original_list)
print('Sorted List: ' + ','.join(numbers))
print('Number of Passes: ' + str(loopcounter))           
            
            