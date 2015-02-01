''' https://projecteuler.net/problem=43

Simple constraints to restrict permutations
We must have d_4 = 0, 2, 4, 6, or 8
We must have d_3 + d_4 + d_5 be a multiple of 3.
We must have d_6 = 0, or 5
'''

import itertools
from utility import start

def p43():
    def check_three(number, start, div_by):
        return ((100*number[start] + 10*number[start+1] + number[start+2])
                % div_by == 0)
    
    found = []
    base = '0123456789'
    for pd in itertools.permutations(base):
        #Filler just so d_1 corresponds to 1st digit
        pd = ['filler'] + [int(digit) for digit in pd]
        if pd[4] in (0, 2, 4, 6, 8): #Could optimise ordering of ifs:
            if sum(pd[3:6]) % 3 == 0:
                if pd[6] in (0, 5):
                    if check_three(pd, 5, 7):
                        if check_three(pd, 6, 11):
                            if check_three(pd, 7, 13):
                                if check_three(pd, 8, 17):
                                    found.append(pd[1:])
    
    return sum(int(''.join(str(digit) for digit in snum)) for snum in found)

if __name__ == '__main__':
    start.time_functions(p43)
