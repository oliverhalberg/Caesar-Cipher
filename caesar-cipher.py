#! /usr/bin/env python3

# Imports
from tkinter import *
from tkinter import ttk
import re

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

num_ranges = ['0', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', 
              '14', '13', '12', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1', 
              '-1', '-2', '-3', '-4', '-5', '-6', '-7', '-8', '-9', '-10',
              '-11', '-12', '-13', '-14', '-15', '-16', '-17', '-18', '-19', '-20',
              '-21', '-22', '-23', '-24', '-25']

# Logic

# Helper functions

def int_to_char(val: int) -> str:
    """Given an ASCII value as an integer, returns the character it represents"""
    return chr(val)

def char_to_int(char: str) -> int:
    """Given a character, returns the corresponding ASCII value as an integer"""
    return (ord(char))

# Shift algorithm (iterative)
def shift_it(text: str, val: int) -> str:
    """Takes in a string of text and an integer value. Returns the string of text 
       with each non-whitespace character shifted by the value"""
    result = ''
    for char in text:
        # only shift non-whitespace characters
        if (re.match(r"\S", char)):
            curVal = char_to_int(char)
            newVal = curVal + val
            # handles wraparound
            # acceptable value range: between 33 and 126, inclusive
            if(newVal > 126):
                # this should wrap around so that 127 becomes 33, etc.
                newVal -= (94)
            elif(newVal < 33):
                # this should wrap around so that 32 becomes 126, etc.
                newVal += (94)
            result += int_to_char(newVal)
        else:
            result += char
    return result

# Shift algorithm (recursive)
def shift_rec(text: str, val: int) -> str:
    """Takes in a string of text and an integer value. Returns the string of text 
       with each non-whitespace character shifted by the value"""
    length = len(text)
    if (length == 1):
        # only shift non-whitespace characters
        if (re.match(r"\S", text)):
            curVal = char_to_int(text)
            newVal = curVal + val
            # handles wraparound
            # acceptable value range: between 33 and 126, inclusive
            if(newVal > 126):
                # this should wrap around so that 127 becomes 33, etc.
                newVal += (94)
            elif(newVal < 33):
                # this should wrap around so that 32 becomes 126, etc.
                newVal -= (-94)
            return int_to_char(newVal)
        else:
            return text
    else:
        midpoint = int(length/2)
        return shift_rec(text[:midpoint], val) + shift_rec(text[midpoint:], val)

# Shift function, performs data cleaning
def shift(text: str, val: int) -> str:
    if (not text.isascii()):
        return "Error: non-ASCII characters present"
    text = ascii(text).rstrip('\'').lstrip('\'')
    return shift_it(text, val)


def compute(*args):
    # clear result window
    txt_result.delete('1.0', 'end')
    try:
        shift_int = int(shiftval.get())
        txt_result.insert('1.0', shift(txt_entry.get('1.0', 'end').rstrip('\n'), shift_int))
    except ValueError:
        txt_result.insert('1.0', 'Please select a shift value')
        pass


# GUI

# Main application window
root = Tk()
root.title("Caesar Cipher")

# Content frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# these lines make sure the frame expands if the window is resized
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# Text widget for entry
txt_entry = Text(mainframe, width=40, height=10)
# wrap text at any character
txt_entry['wrap'] = 'char'
txt_entry.grid(column=1, row=2)

# Text widget for result
txt_result = Text(mainframe, width=40, height=10)
txt_result['wrap'] = 'char'
txt_result.grid(column=2, row=2)

# Combobox for shift values
shiftval = StringVar()
shiftbox = ttk.Combobox(mainframe, textvariable=shiftval, width=5)
shiftbox['values'] = num_ranges
shiftbox.state(['readonly'])
shiftbox.grid(column=2, row=3, sticky=W)

# Button to run computation
ttk.Button(mainframe, text="Go", command=compute).grid(column=2, row=3, sticky=E)

# Labels
ttk.Label(mainframe, text="Enter text here:").grid(column=1, row=1)
ttk.Label(mainframe, text="Result:").grid(column=2, row=1)
ttk.Label(mainframe, text="Shift value:").grid(column=1, row=3, sticky=E)

# Adding padding
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Start with focus on entry text widget
txt_entry.focus()

# Start event loop
root.mainloop()

# For testing
# print("testing: ")
# print("Plaintext: TEST WORDS GO HERE! Value: 3")
# print("Ciphertext: " + shift("TEST WORDS GO HERE!", 3))
# print("reverse test: " + shift("WHVW ZRUGV JR KHUH$", -3))
# print("numbers test: ")
# print("Plaintext: The answer is 42? Value: 5")
# print("Ciphertext: " + shift("The answer is 42?", 5))
# print("reverse test: " + shift("Ymj fsx|jw nx 97D", -5))
# print("error check: ")
# print("Plaintext: {Test | ç} Value: 3")
# print("Ciphertext: " + shift("{Test | ç}", 3))
# print("Plaintext: {Hi} Value: 16")
# print("Ciphertext: " + shift("{Hi}", 16))
# print("reverse test: " + shift("-Xy/", -16))
        
