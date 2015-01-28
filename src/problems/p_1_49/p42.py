"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so
the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t(10).
If the word value is a triangle number then we shall call the word a
triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle words?
"""

import os.path

import utility.start as start
import utility.integers as integers

def p42():
    words = []
    with open(os.path.join(start.DATA_PATH, "p42-words.txt")) as file:
        for line in file:
            words.extend([word.replace('"', "") for word in line.split(",")])
    
    def letter_sum(word):
        letter_values = {
            "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8,
            "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15,
            "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22,
            "w": 23, "x": 24, "y": 25, "z": 26
        }
        
        value = sum(letter_values[char] for char in word.lower())
        return value
    
    word_sums = [letter_sum(word) for word in words]
    num_triangles = sum(1 for word_sum in word_sums
                        if integers.is_triangle_number(word_sum))
    return num_triangles

if __name__ == '__main__':
    start.time_functions(p42)
