#! /usr/bin/env python3


# Hardcoded alphabet reference
# There's probably better ways to do this, but I'm leaving it for now
# I thought about using a list and .index(), but the math could get weird with off-by-one errors
# so this keeps the calculation code simpler
charToInt = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
    'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
    'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}

intToChar = {
    1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',
    6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
    11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O',
    16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
    21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
}

def shift(text: str, val: int) -> str:
    """Takes in a string of text and shifts that text by the given value"""
    result = ''
    text = text.upper()
    for char in text:
        curVal = charToInt[char]
        newVal = curVal + val
        if (newVal > 26):
            newVal -= 26
        result += intToChar[newVal]
    return result

print("testing: ")
print("Plaintext: TEST. Value: 3")
print("Ciphertext: " + shift("TEST", 3))
        
