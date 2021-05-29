#  File: Triangle.py

#  Description: Compared brute force, greedy search, recursive search, and dynamic programming to find the greatest path
# compares their times

#  Student Name: Nicholas Kasper

#  Student UT EID: Nak874

#  Course Name: CS 313E

#  Unique Number: 52240

import sys
from timeit import timeit

# returns the greatest path sum using exhaustive search
def brute_force (grid):
    # goes through each path to find the greatest sum
    sum_counter = [0]
    sums = []

    for i in range(len(grid)):
        sums.append(0)
    #recurse
    brute_helper(grid, 0, 0, sum_counter, sums, len(grid))
    return sum_counter[0]

#helper function for brute_force
def brute_helper(grid, row, col,  sum_counter, arr, length):

    if (row < length and col <= row) and grid[row][col]!= 0:
        arr[row] = grid[row][col]

        if row < length -1:
            brute_helper(grid, row +1, col, sum_counter, arr, length)
            brute_helper(grid, row +1, col + 1, sum_counter, arr, length)
        else:
            sum_temp = sum(arr)

            if sum_counter[0] < sum_temp:
                sum_counter[0] = sum_temp
                

# returns the greatest path sum using greedy approach
def greedy (grid):
    curr_sum = grid[0][0]
    greedy_col = 0
    for greedy_row in range(len(grid)-1):
        if grid[greedy_row + 1 ][greedy_col] > grid[greedy_row + 1][greedy_col + 1]:
            curr_sum += grid[greedy_row + 1 ][greedy_col]
        else: 
            curr_sum += grid[greedy_row + 1][greedy_col + 1]
            greedy_col +=1
    return curr_sum
 

# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):
    return divide_helper(grid,0,0)

def divide_helper(grid, row, col):
    if (len(grid) -1 <= row):
        return grid[row][col]
    else:
        #return max of top and bottom nodes + the current grid value
        return grid[row][col] + max(divide_helper(grid,row + 1, col), divide_helper(grid,row + 1, col+1))
    

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
    iters = len(grid)
    dynamic_grid = [[0 for i in range (iters)] for j in range (iters)]

    # go through each val, find greatest path if its not 0. If its the penultimate, make dynamic grid val the grid val
    for row in range(iters-1,-1,-1):
        for col in range(iters-1,-1,-1):

            # if its 0 it doesnt count
            if grid[row][col] == 0:
                continue 

            elif (row == iters-1):
                dynamic_grid[row][col] = grid[row][col]

            else: 
                #add maximum cell between top and bottom node
                dynamic_grid[row][col] = max(grid[row][col] + dynamic_grid[row + 1][col], grid[row][col] + dynamic_grid[row+1][col+1])

    return dynamic_grid[0][0]
  

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return grid 

def main ():
  # read triangular grid from file
  grid = read_file()
  
  
  # check that the grid was read in properly
  #print (grid)
  

  # output greatest path from exhaustive search
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search
  print("The greatest path sum through exhaustive search is")
  print(brute_force(grid))
  print("The time taken for exhaustive search in seconds is")
  print(times)

  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach
  print('')
  print("The greatest path sum through greedy search is")
  print(greedy(grid))
  print("The time taken for greedy approach in seconds is")
  print(times)

  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach
  print('')
  print("The greatest path sum through recursive search is")
  print(divide_conquer(grid))
  print("The time taken for recursive search in seconds is")
  print(times)

  # output greatest path from dynamic programming 
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  # print time taken using dynamic programming
  print()
  print("The greatest path sum through dynamic programming is")
  print(dynamic_prog(grid))
  print("The time taken for dynamic programming in seconds is")
  print(times)

if __name__ == "__main__":
  main()
