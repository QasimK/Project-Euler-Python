"""
An irrational decimal fraction is created by concatenating the +ve integers:

0.123456789101112131415161718192021...
             ^
It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part,
find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
"""

"""
Use the fact that 1-9 are 1 digit long, 10-99 are 2 digit long, etc.
So calculate the number dn is at by using this fact.
How may 1-digit numbers are used up to reach dn?
All of them? Then how many 2-digit numbers are used?
All of them? Then how many 3 digit numbers are used?
It is part way? Then work out the 3 digit number it is in and calc the digit.
"""

def p40():
    #This dict. specifies which dn we want
    dn_todo = [1, 10, 100, 1000, 10000, 100000, 1000000]
    #dn_todo = [1,10]
    dn_list = []
    
    n = 0
    num = 0
    while len(dn_todo):
        num += 1
        pre_n = n
        n += len(str(num)) #Can optimise this
        
        while len(dn_todo) and pre_n <= dn_todo[0] and dn_todo[0] <= n:
            n_wanted = dn_todo[0]
            del dn_todo[0]
            
            #We note:
            #Current num is the number leading to the n boundary
            #1234
            # * ^
            #   n=102
            dn_list.append(str(num)[-(n-n_wanted)-1])
    
    p = 1
    for x in [int(s) for s in dn_list]:
        p *= x
    return p
        

if __name__=="__main__":
    import utility.start as start
    start.time_functions(p40)
