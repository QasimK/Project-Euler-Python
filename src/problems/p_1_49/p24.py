'''
A permutation is an ordered arrangement of objects. For example,
3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of 0, 1
and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

'''
1: a
2: [b]a, [a]b
3: [c]2s, [b]2s, [a]2s
(2s is [b]a and [a]b)
ie. use recursion and lists
'''

def permute(number_list):
    if len(number_list) == 1:
        return number_list
    
    all_permutations = []
    
    for i, number in enumerate(number_list):
        #[a]
        first = [number] #= [ number_list[i] ]
        
        #2s
        remaining = number_list[0:i]
        remaining += number_list[i+1:]
    
        appendices = permute(remaining)
        
        for appendix in appendices:
            permutation = first+[appendix]
            all_permutations.append(permutation)
        
    return all_permutations
    

def p24():
    all_permutations = permute([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print("size:", len(all_permutations))
    
    selected = all_permutations[10**6-1]
    print(selected)

if __name__ == '__main__':
    import time
    start = time.time()
    print(p24())
    print("Time taken: ", (time.time()-start)*1000, "ms", sep="")