'''
Created on 5 Sep 2011

@author: Qasim
'''

"""Problem:
It can be seen that the number, 125874, and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""

"""Thoughts:
Quick analysis shows for x/2x, there is no solution for 2-digit numbers.
Doing the analysis for x/2x/... for probably len(str(x))>6 is... impossible.

Brute force:
Check first if digits of x == digits of 2x then 3x and etc.

Didn't do:
Learning from that analysis I did earlier:
    2*x where x=AB, means A < 5 otherwise, x > 100!
    Therefore, if you do 6*x, x must start with the digit 1.
    
    Similarly, you can do a sort of upper limit
    (eg. 16*6 = 96, 166*6 = 996, 1666*6 = 9996, etc.)

LOL (Micket):
"I think i few people missed the fact that 1*x didn't have to contain the same
numbers (althought it did happen to have)"
"""

def p52():
    #ALL THESE IFs COULD HAVE BEEN REPLACED WITH A LOOP!!
    for x in range(142857, 10000000):
        x2 = 2*x
        if sorted(list(str(x))) == sorted(list(str(x2))):
            #return x
            x3 = 3*x
            if sorted(list(str(x))) == sorted(list(str(x3))):
                #return x
                x4 = 4*x
                if sorted(list(str(x))) == sorted(list(str(x4))):
                    #return x
                    x5 = 5*x
                    if sorted(list(str(x))) == sorted(list(str(x5))):
                        #return x
                        x6 = 6*x
                        if sorted(list(str(x))) == sorted(list(str(x6))):
                            return x

if __name__ == '__main__':
    import utility.start as start
    start.time_functions(p52)
