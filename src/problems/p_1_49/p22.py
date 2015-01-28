'''
Created on 7 Apr 2010

@author: Qasim
'''

'''
Using names.txt  (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its
alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th
name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

import os
import string

import utility.start as start

def p22():
    with open(os.path.join(start.DATA_PATH, "p22-names.txt")) as file:
        for line in file:
            fixed_names = []
            unfixed_names = line.split(",")
            for name in unfixed_names:
                fixed_names.append(name.replace('"', ''))
    
    fixed_names.sort()
    
    scores = {}
    for score, letter in enumerate(string.ascii_uppercase):
        scores[letter] = score + 1 #Score starts from 0
    
    name_scores = 0
    for position, name in enumerate(fixed_names):

        name_score = 0
        for letter in name:
            name_score += scores[letter]
        name_scores  += name_score * (position+1) #Position starts from 0
    
    return name_scores

def main():
    import time
    start = time.time()
    print(p22())
    print("Time taken: ", (time.time()-start)*1000, "ms", sep="")

if __name__ == '__main__': main()