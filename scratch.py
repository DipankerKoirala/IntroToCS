
Valid = False
#Get user input and validate entry
while Valid == False:
    UserInput = (input("Enter a series of integers seperated by commas: "))
    numbers = UserInput.split(',')
    print(numbers)
    n = len(numbers)
    for i in numbers:
        try:
            int(i)
            Valid = True
        except Exception:
            print("not a comma separated set of integers, please try again")
            Valid = False
            break
            