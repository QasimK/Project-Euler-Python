'''
Created on 5 Apr 2010

@author: Qasim
'''

'''
Let d(n) be defined as the sum of proper divisors of n
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are
an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284
are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

'''
I will simply loop through all numbers from 1-9999 (x)
1) See if x is not in the list of numbers to ignore
2) Find factors of x
   (Exclude x from this list of factors)
3) Sum of factors = y
4) See y < 10,000
5) Find factors of y
6) See if (sum of factors of y) = x
   (and y != x)
7) If yes then x, y are an amicable pair
8) Add y to the list of numbers to ignore
   (y is necessarily larger than x)
'''

'''
Possible optimisation:
If x is odd then y must be odd because odd X odd = odd (only way to make odd)
therefore, factors of x are all odd.
Sum of pairs of odd make an even, but you exclude the original number
therefore sum of factors of x are odd (=y)
'''

import utility.factors as factors
import time

if __name__ == '__main__':
    begin = time.time()
    
    list_of_numbers_to_ignore = [] #Because they have already been checked
    amicable_pairs = []
    
    max = 10000
    for x in range(4, max): #Excludes 10,000 (we know 1, 2, 3 are not amicable)
        if x not in list_of_numbers_to_ignore:
            x_proper_factors = factors.geget_proper_divsor)
            x_factors_sum = sum(x_proper_factors)
            
            y = x_factors_sum
            
            #See optimisation outlined above (odd/even)
            if x % 2 == 1 and y % 2 == 0:
                #x is odd but y is not odd
                continue
            
            if y < max and y != x:
                y_proper_factors = factors.geget_proper_divsor)
                y_factors_sum = sum(y_proper_factors)
                
                if y_factors_sum == x:
                    #They are an amicable pair
                    amicable_pairs.append((x, y))
                    list_of_numbers_to_ignore.append(y)
        
    
    def sum_double_list(list):
        """Return the sum of all the numbers of all the lists inside a list"""
        total_sum = 0
        for list2 in list:
            total_sum += sum(list2)
        return total_sum
    
    #print(amicable_pairs)
    print(sum_double_list(amicable_pairs))
    
    print(time.time()-begin)