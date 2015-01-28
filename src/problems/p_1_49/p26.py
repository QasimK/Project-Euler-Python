'''
A unit fraction contains 1 in the numerator. The decimal representation
of the unit fractions with denominators 2 to 10 are given:

    1/2   = 0.5
    1/3   = 0.(3)
    1/4   = 0.25
    1/5   = 0.2
    1/6   = 0.1(6)
    1/7   = 0.(142857)
    1/8   = 0.125
    1/9   = 0.(1)
    1/10  = 0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest
recurring cycle in its decimal fraction part.
'''

"""
What could be done:
Clearly the length of the repeating section depends on d.
So start from 1000 going backwards and if the length of the largest repeating
section > current-d then you can stop.
"""
import math as maths

def p26():
    repeating_section_info = [] #denom, len(repeat_section), repeat_section
    for denom in range(2, 1000):
        numerator = [1]
        working_number_list = []
        answer = []
        
        #There are only unique working numbers
        current_num_i = -1
        while len(set(working_number_list)) == len(working_number_list):
            current_num_i += 1
            
            if numerator[current_num_i] in working_number_list:
                index = numerator.index(numerator[current_num_i])
                repeat_section = answer[index:]
                break
            
            cur_answer = maths.floor(numerator[current_num_i] / denom)
            carry = numerator[current_num_i] % denom
            try:
                numerator[current_num_i+1] = carry * 10 +\
                                            numerator[current_num_i+1]
            except IndexError:
                numerator.append(carry*10)
            
            answer.append(cur_answer)
            working_number_list.append(numerator[current_num_i])
            
            #print(list(set(working_number_list)), working_number_list)
        
        repeating_section_info.append((denom, len(repeat_section),
                                       repeat_section))
    
    #Analyse repeating_section_info
    max_length = (0, 0, 0)
    for denom, length, section in repeating_section_info:
        print(denom, length, section)
        if length > max_length[1]:
            max_length = (denom, length, section)
    
    return max_length[0]

if __name__ == '__main__':
    import utility.start as start
    start.time_functions(p26)
