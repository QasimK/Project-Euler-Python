'''
Created on 3 Apr 2010

@author: Qasim
'''

'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
'''

'''
I shall attempt this by a tree-traversal method.
In each position I will see what is the largest possible sum
and which route to take to get that sum.
I will work downwards from the top.
Eventually I will find the largest sum at the bottom row and see
which route was taken to find it (OPTIONAL - will not do)
'''

class node:
    """Once you have constructed the node graph
    you must not call get_sum otherwise any changes
    you make to the graph may not take effect"""
    
    def __init__(self, number, parents=[]):
        self.number = number
        self.parents = parents
        self.sum = None
    def get_sum(self):
        if self.sum != None:
            return self.sum
        elif self.parents == []:
            return self.number
        else:
            largest_sum = 0
            for parent in self.parents:
                parent_sum = parent.get_sum()
                if parent_sum > largest_sum:
                    largest_sum = parent_sum
            self.sum = largest_sum + self.number
            return self.sum

the_graph = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

def p18(graph):
    global node
    
    #Construct node
    numbers = []
    #Split graph into lines (rows)
    for line in graph.split("\n"):
        #Split lines into numbers
        line_numbers = line.split(" ")
        #Convert into ints
        line_numbers = [int(number) for number in line_numbers]
        numbers.append(line_numbers)
    
    base_node = node(numbers[0][0])
    actual_graph = [ [base_node] ]
    for row_num, row in enumerate(numbers):
        if row_num == 0:
            continue
        new_row = []
        for column_num, number in enumerate(row):
            
            if column_num == 0: #at beginning edge
                parents = [actual_graph[row_num-1][column_num]]
            elif column_num == row_num: #at end edge
                parents = [actual_graph[row_num-1][column_num-1]]
            else:
                parents = [actual_graph[row_num-1][column_num], 
                           actual_graph[row_num-1][column_num-1]]
            node_num = node(number, parents)
            new_row.append(node_num)
        actual_graph.append(new_row)
    
    #Traverse the last row and find the sums
    sums = []
    for node in actual_graph[-1]:
        this_sum = node.get_sum()
        sums.append(this_sum)
    biggest_sum = max(sums)
    return biggest_sum

if __name__ == '__main__':
    solution = p18(the_graph)
    print(solution)
