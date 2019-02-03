#!/usr/bin/python3/env python
"""
Created on Wed Nov  7 20:15:19 2018

@author: Dipanker
"""
vowels = ['a','e','i','o','u']


UserInput = (input("Type a sentence: "))
words = UserInput.split()

for word in words:
    if word[0].lower() in vowels:       
        words[words.index(word)] = word + "yay"
    else:
        for i in word:
            if i.lower in vowels:
                x, y = word.split(i)
                words[words.index(word)] = i + y + x + "ay"
                break
    print(words)

