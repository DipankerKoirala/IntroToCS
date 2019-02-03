#!/usr/bin/python3/env python
#Gets user input in Centigrade or Farenheit

#set the temperature variable to blank
Temperature = " "
#while 
while Temperature != "exit":
    Temperature = (input("Enter a temperature followed by 'Centigrade' or 'Fahrenheit'. Type exit to end: "))
    if Temperature.lower() == 'exit':
        break
    else:
        #tries to run the below code
        try:
            #splits the entry into temp and type
            Value, Type = Temperature.split(' ')
            Value = float(Value)
            #checks if Farenheit is not the Type
            if "farenheit" == Type.lower():
            #Applies the farehnheit to centigrade conversion formula
                Centigrade = ((float(Value) - 32)/1.80)
            #prints the answer          
                print(Temperature, " equals ", Centigrade, " Centigrade")
            elif "centigrade" == Type.lower():
            #Applies the centigrade to fahrenheit conversion formula
                Fahrenheit = ((float(Value)*1.80) + 32)
            #prints the answer
                print(Temperature, " equals ", Fahrenheit, " Fahrenheit")
            else:
                print("I don't understand, try again")
        #if any errors occur on above code, prompts user to try again
        except ValueError:
            print("I don't understand, try again")
      