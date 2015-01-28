'''
Created on 18 Jul 2010

@author: Qasim
'''

'''
The decimal number, 585 = 1001001001_(2) (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
'''

'''

Conversion to base 2:
585 = 2^9 + 2^6 + 2^3 + 2^0 = 1001001001 (2^9, 2^8, ..., 2^0)

Find largest 2^n which is less than/equal to the number, and repeat.
(Subtract this 2^n from the number)

Did not do:
===========

Single-digit:
0 = 0 :)
1 = 1 :)
2 = 10
3 = 11 :)
4 = 100
5 = 101 :)
6 = 110
7 = 111 :)
8 = 1000
9 = 1001 :)
10 = 1010
11 = 1011
12 = 1100
13 = 1101
14 = 1110
15 = 1111 :)
16 = 10000
17 = 10001 :)
11011 = 27, which does not follow pattern

Therefore work from base 2 to base 10:
ie.

 1  2  3  4  5  6
[-][-][-][-][-][-]
999,999 = 11110100001000111111 (max)
20 slots

Use symmetry around central number
(when odd, this is (length+1)/2
(when even, there is no central position but it is in-between 2 numbers)

ie. create a pattern of length up to the central number

eg. For Even

 1  2  3  4 | 5  6  7  8
[1][-][-][-]|[-][-][-][-]
Then create combinations for 1, 2, 3, 4 where 1 is 1
eg.
1000 (000)
1001 (001)
..
010
011
100
101
110
111
And substitute the reverse of these into 5, 6, 7, 8

eg. For Odd

 1  2  3 |  4  | 5  6  7
[1][-][-]|[0/1]|[-][-][-]

Here 4 can be 0/1 only (do the following procedure for each).
Do the combinations for 1, 2, 3 and put the reverse into 5, 6, 7 as above.

These are all the binary numbers that are palindromic.
Convert to base 10 and check if they are palindromic.

ALSO as when 1st is True, last is True
Therefore the number must be odd (+2^0)
'''

def replace_char_in_string(string, pos, char):
    """Replace a character at a position in a string"""
    string_list = list(string)
    string_list[pos] = char
    
    stri = ""
    for char in string_list:
        stri += str(char)
    return stri

def base_10_to_2(num):
    """Convert a base 10 number to a base 2 string"""
    
    if num == 0:
        return "0"
    
    powers = []
    while num != 0:
        n = 0
        while 2**n <= num:
            n += 1
        else:
            #n needed is n-1
            n -= 1
            powers.append(n)
            num -= 2**n
    
    #Construct base 2 number
    num_2 = ""
    for i in range(0, max(powers)+1):
        if i in powers:
            num_2 += "1"
        else:
            num_2 += "0"
    return num_2

def base_2_to_10(string_number):
    """Convert a base 2 string to a base 10 number"""
    number = 0
    #reversed string [::-1]
    for power, char in enumerate(string_number[::-1]):
        if char == "1":
            number += 2**power
    return number

from math import floor

def num_is_palindromic_10(num):
    """Return if positive integer is palindromic"""
    num = str(num)
    size = len(num)
    if size == 1:
        return True
    elif size > 1:
        return num[0:floor(size/2)] == num[-1:-floor(size/2)-1:-1]
    else:
        #size=0
        assert(False)

def num_is_palindromic_2(num_str):
    """Return if the num_str in base 2 is palindromic"""
    size = len(num_str)
    if size == 1:
        return True
    elif size > 1:
        return num_str[0:floor(size/2)] == num_str[-1:-floor(size/2)-1:-1]
    else:
        #size = 0
        assert(False)

def p26():
    _sum = 0
    for num in range(1, 10**8-1, 2):
        if num_is_palindromic_10(num):
            if num_is_palindromic_2(base_10_to_2(num)):
                _sum += num
                print(num)
    return _sum

if __name__ == '__main__':
    import time
    start = time.time()
    print(p26())
    print("Time taken: ", (time.time()-start)*1000, "ms", sep="")
