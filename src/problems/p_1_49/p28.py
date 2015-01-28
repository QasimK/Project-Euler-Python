'''
Created on 8 Jun 2010

@author: Qasim
'''

'''
Starting with the number 1 and moving to the right in a clockwise direction
a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
formed in the same way?
'''

'''
1 + (3 + 5 + 7 + 9) + (13 + 17 + 21 + 25) + ...
  +2   +2  +2  +2   +4    +4   +4   +4    +6

where 6+1 = 7 is the size of the spiral.

Therefore:
sum = 1
adder = 2
addnumber = 1
while adder+1 < 1003:
    do 4 times:
        addnumber += adder
        sum += addnumber
    adder += 2
    

Later:
(better solution)
Notice in an nxn grid:
- top-right: n^2
- top-left: n^2 - n + 1
- ...
- sum = 4n^2 + ...
Then loop from start=1, end=1001, step=2:
    sum += 4n^2 + ...
'''

if __name__ == '__main__':
    _sum = 1
    adder = 2
    addnumber = 1
    while adder + 1 < 1003:
        for i in range(0,4):
            addnumber += adder
            _sum += addnumber
        adder += 2
    print(_sum)
