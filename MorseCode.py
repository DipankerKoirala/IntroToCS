#!/usr/bin/python3/env python

#This program is set to have 1 unit of time for morse code = 0.5 seconds
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup (11, GPIO.OUT)

#Morse Code dictionary source: http://code.activestate.com/recipes/578407-simple-morse-code-translator-in-python/
CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
     	'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }
#asks user for input
UserInput = (input("Make any alphanumeric entry: "))

#loops through each character in the input
for char in UserInput:
    #if the character is a space - LED sleeps for 3.5 seconds
    if char == " ":
        print(char)
        GPIO.output(11, False)
        time.sleep(3.5)
    #if character is a letter or numbers, pulls the appropriate code from the dictionary
    else:
        try:
            MorseCode = CODE[char.upper()]
            print(char)
            print (MorseCode)
            #loops through each character of the morsecode
            for c in MorseCode:
                #if character is a dash - Led blicks for 1.5 Seconds, then sleeps for 0.5 seconds
                if c == "-":
                    GPIO.output(11, True)
                    time.sleep(1.5)
                    GPIO.output(11, False)
                    time.sleep(0.5)
                #if character is a dot - Led blicks for 0.5 Seconds, then sleeps for 0.5 seconds
                else:
                    GPIO.output(11, True)
                    time.sleep(0.5)
                    GPIO.output(11, False)
                    time.sleep(0.5)
            time.sleep(1.5)
        #if the entered character is not a key in the dictionary, an error is thrown
        except KeyError:
            print("Only use alphanumeric entries")