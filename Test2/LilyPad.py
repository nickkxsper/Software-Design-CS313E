#  File: LilyPad.py

#  Description: Determines the distinct amount of ways Foo can get to the other side
#               of a pond with n lily pads by hopping either 1 or 2 lily pads at a time

#  Student Name: Nicholas Kasper

#  Student UT EID: Nak874

#  Course Name: CS 313E

#  Unique Number: 

import sys

# Input: n is an int of how many lily pads there are
# Output: return an integer of how many distinct ways there are to cross the pond (order matters), # can hop either 1 or 2 lily pads at a time


def distinct_ways(n):
    step_sizes = [1,2]
    ways = [0 for i in range(n+1)]
    ways[0] = 1

    for i in range(n+1):
        ways[i] += sum(ways[i - x] for x in step_sizes if i - x > 0)
        ways[i] += 1 if i in step_sizes else 0
    return ways[-1]
    
    




def main(): 
    # read number of lily pads
    n = int(input())

    # get the result from your call to distinct_ways()
    x = [1,2]
    result = distinct_ways(n)

    # print the result to standard output
    print(result)

if __name__ == "__main__": main()