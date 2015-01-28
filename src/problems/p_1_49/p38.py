''' https://projecteuler.net/problem=38

X = k .x (1, 2, ..., n)

In order to make X 9-digits:
    If k is 1 digit:
        k=1, n=9 & k=3, n=6 & k>=5, n=5 - Exclude k=3 since not pandigital!
    If k is 2 digits, then 25 <= k <= 33 (and n=4 only)
    If k is 3 digits, then 100 <= k <= 333 (and n=3 only)
    If k is 4 digits, then 5000 <= k <= 9999 (and n=2 only)

So do the concatenated product, and only if it is large enough check if
it is a pandigital.
'''

from utility import start

def concatenated_product(k, n):
    single_products = [k * i for i in range(1, n+1)]
    return int(''.join([str(product) for product in single_products]))

def is_pandigital(number):
    return sorted(str(number)) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def p38():
    # k = 1 cases:
    largest_pandigital = concatenated_product(1, 9)
    checks = [(5, 9, 5), (25, 33, 4), (100, 333, 3), (5000, 9999, 2)]
    
    for check in checks:
        k_start = check[0]
        k_end = check[1]
        n = check[2]
        for k in range(k_start, k_end + 1):
            possible = concatenated_product(k, n)
            if possible > largest_pandigital and is_pandigital(possible):
                largest_pandigital = possible
    
    return largest_pandigital

if __name__ == '__main__':
    start.time_functions(p38)
