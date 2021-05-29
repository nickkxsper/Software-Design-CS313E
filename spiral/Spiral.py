#  File: Spiral.py

#  Description: Creates an n dimensional circular integer spiral (2d list) and then
# finds the provided element and sums the adjacent cells in the 2d list (spiral)

#  Student Name: Nicholas Kasper

#  Student UT EID: Nak874


#  Course Name: CS 313E

#  Unique Number: 52240

#  Date Created: 1/30/2021

#  Date Last Modified: 2/01/2021

import sys


# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n

def create_spiral(n):
	#initialize spiral and dimension counters
	spiral = []
	dimension = n
	bottom_dim = (dimension // 2 + 1)
	dimension_count = dimension - 1

	#fills in number of rows to be made
	for i in range(dimension):
		matrix = []

        #fills in bottom left
		if bottom_dim <= i:
			for x in range(i + dimension_count):
				matrix.append(spiral[i-1][x] - 1)

        #fills in left side non squares
		if bottom_dim > i:
			for x in range (i):
				if i == 0:
					break
				else:
					matrix.append(spiral[i-1][x] - 1)

        
		#fill in the even squares
		if bottom_dim <= i:
			for x in range(1, dimension -1, -1):
				matrix.append(dimension_count **2 + x)

		#fills in bottom right 
		if bottom_dim <= i:
			for x in range(i + dimension_count, 0, -1):
				matrix.append(spiral[i-1][-x] + 1)

		#fills in odd square 
		for x in range (0, dimension):
			matrix.append((dimension **2) - (dimension_count))
			dimension_count -= 1

		#fills in top right portion of spiral
		if bottom_dim > i:
			for x in range (i, 0, -1):
				if i == 0:
					break
				if x == i:
					matrix.append(matrix[-1] +1)
				else:
					matrix.append(spiral[i-1][-x] + 1)

		#decrease the number for the next spiral row and counter 
		dimension -= 2
		dimension_count = dimension - 1

		#add list to the spiral
		spiral.append(matrix)

	return(spiral)	






# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0


def sum_adjacent_numbers (spiral, n):
    adj_sum = 0

    # bounds
    iMin = 0
    iMax = len(spiral) - 1
    jMin = 0
    jMax = len(spiral[0])-1

    if 1 <= n <= len(spiral)**2:

        for i in range(len(spiral)):
            for j in range(len(spiral)):
                if spiral[i][j] == n:

                    #up 
                    if iMin <= i - 1 <= iMax and jMin <= j <= jMax:
                        up = spiral[i-1][j]
                        adj_sum += up


                    # diagonal up right
                    if iMin <= i - 1 <= iMax and jMin <= j + 1 <= jMax:
                        dgnl_up_right = spiral[i-1][j+1]
                        adj_sum += dgnl_up_right
                    
                    # right
                    if iMin <= i <= iMax and jMin <= j + 1 <= jMax:
                        right = spiral[i][j+1]
                        adj_sum += right
                    
                    # diagonal down right
                    if iMin <= i+1 <= iMax and jMin <= j + 1 <= jMax:
                        dngl_down_right = spiral[i+1][j+1]
                        adj_sum += dngl_down_right
                
                    # down 
                    if iMin <= i + 1 <= iMax and jMin <= j <= jMax:
                        down = spiral[i+1][j]
                        adj_sum += down

                    
                    # diagonal down left
                    if iMin <= i +1 <= iMax and jMin <= j - 1 <= jMax:
                        dgnl_down_left = spiral[i+1][j-1]
                        adj_sum += dgnl_down_left
                    
                    # left
                    if iMin <= i <= iMax and jMin <= j - 1 <= jMax:
                        left = spiral[i][j-1]
                        adj_sum += left

                    
                    # diagonal up left
                    if iMin <= i-1 <= iMax and jMin <= j - 1 <= jMax:
                        dgnl_up_right = spiral[i-1][j-1]
                        adj_sum += dgnl_up_right
        return adj_sum

    else:
        return 0 
                    
    
            


def main():
  # read the input file

  #spiral_data = [int(x.replace('\n','')) for x in open('spiral.in','r')]

  spiral_data = [int(x) for x in sys.stdin.readlines()]

  spiral = create_spiral(spiral_data[0])

  # add the adjacent numbers

  for i in spiral_data[1::]:
        print(sum_adjacent_numbers(spiral, i))
  

if __name__ == "__main__":
    main()