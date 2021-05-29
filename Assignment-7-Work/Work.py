#  File: Work.py

#  Description: Uses linear and binary search to find a minimum value in a f(x,y) s.t x is the min lines of code
# and y is the productivity factor 

#  Student Name: Nick Kasper

#  Student UT EID: Nak874

#  Course Name: CS 313E

#  Unique Number: 52240

#  Date Created: 3/3/2021

#  Date Last Modified: 3/3/2021
import sys
import time

# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
    count = 0
    temp = v//(k**count)
    summation = 0
    # add terms in summation while they're still above 0 (lower bound)
    while temp >0:
        summation += temp
        count += 1
        temp = v//(k**count)
    return summation

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):

    summation = 0
    count = 0
    # go through each possible value sequentially and stop when we reach the first allowable value
    while summation < n:
        count +=1
        summation = sum_series(count, k)
        
    return count


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
    # define problem domain and bounds
    possible_values = []
    for i in range(n+1):
        possible_values.append(i)

    low = 0
    high = len(possible_values) - 1

    # while the bounds are still distanced apart, find midpoint, move upper and lower bounds according to the
    # sum_series() function, return last midpoint in the domain
    while low <= high:
        midpoint = (low+high)//2
        if sum_series(possible_values[midpoint], k) < n:
            low = midpoint + 1
        elif sum_series(possible_values[midpoint], k) > n:
            if sum_series(possible_values[midpoint] - 1, k) < n:
                return possible_values[midpoint]
            else:
                high = midpoint - 1
        else:
            return possible_values[midpoint]
# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases

  return "all test cases passed"

def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int(line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    
    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()
    
if __name__ == "__main__": main()
