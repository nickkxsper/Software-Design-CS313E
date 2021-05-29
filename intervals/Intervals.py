#  File: Interval.py

#  Description: 

#  Student Name: Nicholas Kasper

#  Student UT EID: Nak874


#  Course Name: CS 313E

#  Unique Number: 52240

#  Date Created: 02/04/2021

#  Date Last Modified: 2/04/2021

import sys 


def merge_tuples(tuples_list):
    '''
    # Input: tuples_list is an unsorted list of tuples denoting intervals
    # Output: a list of merged tuples sorted by the lower number of the
    #         interval

    '''

    #first sort from low to high intervals

    sort_wout_merge = sorted(tuples_list[1:], key = lambda x: x[0])

    merged = []


    # for each tuple, find max in range and create/append new tuples expanding the range
    # otherwise, move onto next pair

    for pair in sort_wout_merge:
        if not merged:
            merged.append(pair)
        else:
            top = merged.pop()
            if pair[0] <= top[1]:
                updated_range = (top[0], max(top[1], pair[1]))
                merged.append(updated_range)
            else:
                merged.append(top)
                merged.append(pair)
        

    return merged


def sort_by_interval_size (tuples_list):
    '''
    # Input: tuples_list is a list of tuples of denoting intervals
    # Output: a list of tuples sorted by ascending order of the size of
    #         the interval
    #         if two intervals have the size then it will sort by the
    #         lower number in the interval
    '''

    # sort tuple list by absolute value of element 1 - element 0 (range)

    merged = sorted(tuples_list, key = lambda x: abs(x[1] - x[0]))
    return merged
    

def test_cases ():
  '''
  # Input: no input
  # Output: a string denoting all test cases have passed

  '''
  assert merge_tuples([(1,2)]) == [(1,2)]

  assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]

  return "all test cases passed"

def main():
  # open file intervals.in and read the data and create a list of tuples
  intervals_data = [tuple(map(int, x.strip().split(' '))) for x in sys.stdin.readlines()]


  tuples_list = intervals_data


  # merge the list of tuples

  merged = merge_tuples(tuples_list)


  # sort the list of tuples according to the size of the interval

  size_sort = sort_by_interval_size(merged)


  # run your test cases

  #print (test_cases())


  # write the output list of tuples from the two functions
  print(merged)

  print(size_sort)

if __name__ == "__main__":
  main()