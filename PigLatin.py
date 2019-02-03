#!/usr/bin/python3/env python
"""
Created on Wed Nov  7 20:15:19 2018

@author: Dipanker
"""
#build a list of vowels
vowels = ['a','e','i','o','u']

PigLatinList = []

#get user input
UserInput = (input("Type a sentence: "))
words = UserInput.split()

#for each word in the sentence:
for word in words:
    #if the word starts with a vowel, add "yay"
    if word[0].lower() in vowels:
        word+="yay"
        PigLatinList.append(word)
    #otherwise, find the next vowel, split and reconfigure the word and add "ay"
    else:
        for i in word:
            if i.lower() in vowels:
                x, y = word.split(i,1)
                word = i + y + x + "ay"
                PigLatinList.append(word)
                break
#print the Pig Latin sentence           
print(' '.join(PigLatinList))
