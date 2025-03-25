#! /usr/bin/env python3

# Imports
from tkinter import *
from tkinter import ttk

# Hardcoded alphabet reference (no longer used but included for now)
# charToInt = {
#     'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
#     'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
#     'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
#     'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
#     'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
# }

# intToChar = {
#     1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',
#     6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
#     11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O',
#     16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
#     21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
# }

# Logic

def int_to_char(val: int) -> str:
    """Given an uppercase character, A-Z, returns its equivalent value, 1-26"""
    return chr(val + 64)

def char_to_int(char: str) -> int:
    """Given a value, 1-26, returns its equivalent uppercase character, A-Z"""
    return (ord(char) - 64)

def shift(text: str, val: int) -> str:
    """Takes in a string of text and shifts that text by the given value"""
    result = ''
    text = text.upper()
    for char in text:
        # only shift non-whitespace characters
        if (char not in [' ', '\n', '\t']):
            curVal = char_to_int(char)
            newVal = curVal + val
            # this will probably be handled in the GUI (only certain values accepted) but it's still a good check for now
            if (newVal > 26):
                newVal -= 26
            result += int_to_char(newVal)
        else:
            result += char
    return result

# GUI

root = Tk()
root.title("Caesar Cipher")


# For testing
print("testing: ")
print("Plaintext: TEST WORDS GO HERE. Value: 3")
print("Ciphertext: " + shift("TEST WORDS GO HERE", 3))
        
