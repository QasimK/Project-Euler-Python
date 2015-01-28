'''
Created on 8 Jun 2010

@author: Qasim
'''

'''
Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

    1634 = 1^(4) + 6^(4) + 3^(4) + 4^(4)
    8208 = 8^(4) + 2^(4) + 0^(4) + 8^(4)
    9474 = 9^(4) + 4^(4) + 7^(4) + 4^(4)

As 1 = 1^(4) is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.
'''

'''
numbers = list
for number:
    digits = get_digits(number)
    digits_5 = list of digits to the power of 5
    sum = sum of digits_5
    if sum == number:
        add number to numbers
'''
if __name__ == '__main__':
    numbers = []
    #Max number is 999999
    for number in range(2, 10**6):
        digits = [int(char) for char in str(number)]
        digits5 = [n**5 for n in digits]
        sum_digits5 = sum(digits5)
        if sum_digits5 == number:
            numbers.append(sum_digits5)
    
    print(numbers, sum(numbers), sep="\n")
