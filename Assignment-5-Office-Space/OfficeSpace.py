#  File: OfficeSpace.py

#  Description: Given a set of employees and their requested office dimensions along with office dimensions, we find the total, unallocated, contested, and per employee space


#  Student Name: Nicholas Kasper

#  Student UT EID: Nak874


#  Course Name: CS 313E

#  Unique Number: 52240

#  Date Created: 02/17/2021

#  Date Last Modified: 02/17/2021

import sys

# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle

def area (rect):
    '''
    Multiplys x difference by y difference, returning area
    '''
    area = 0 
    x_dim = rect[2] - rec[0]
    y_dim = rect[3] - rect[1]

    area = int(x_dim * y_dim)

    return area

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):
    # find if x axis or y axix is not overlapping
    top_left_1 = [rect1[0], rect1[3]]
    top_left_2 = [rect2[0], rect2[3]]
    
    bottom_right_1 = [rect1[2], rect1[1]]
    bottom_right_2 = [rect2[2], rect2[1]]

    flag = True

    # return true if rectangle is on side or above another

    if top_left_1[0] >= bottom_right_2[0] or top_left_2[0] >= bottom_right_1[0]:
        flag = False
    if top_left_1[1] <= bottom_right_2[1] or top_left_2[1] <= bottom_right_1[1]:
        flag = False

    # find x and y min and max
    if flag == True:
        x_1 = max(rect1[0], rect2[0])
        x_2 = min(rect1[2], rect2[2])
        y_1 = max(rect1[1], rect2[1])
        y_2 = min(rect1[3], rect2[3])
        return (x_1,y_1,x_2,y_2)

    else:
        return (0,0,0,0)





# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated 
#         space in the office
def unallocated_space (bldg):
    # iterate through each cell in the building
    # if its not 0, its being used

    used_space = 0
    for y in range(len(bldg)):
        for x in range(len(bldg[0])):
            if bldg[y][x] != 0:
                used_space +=1   
    
    #print(total_office_area(bldg))
    return total_office_area(bldg) - used_space
    
# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space (bldg):
    # iterate through each cell in the building
    # if its greater than 1, its contested

    contested_space = 0
    for row in bldg:
        for x in row:
            if x > 1:
                contested_space +=1   

    return contested_space

# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (bldg, rect):

    uncontested_space = 0


    x_min = min(rect[0], rect[2])
    x_max = max(rect[0], rect[2])
    y_max = max(rect[1], rect[3])
    y_min = min(rect[1], rect[3])
    #print(x_min, x_max, y_min, y_max)

    for y in range(len(bldg)):
            for x in range(len(bldg[0])):
                if x_min <= x < x_max and y_min <= y < y_max:
                    if bldg[y][x] == 1:
                        uncontested_space +=1
                    else:
                        pass

    return uncontested_space

    

# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):

    

    pass

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  assert area ((0, 0, 1, 1)) == 1
  # write your own test cases
  
  return "all test cases passed"


def cubicles_to_array_form(cubicles, office_dim):
    # converts cubicle coords to 2d array format
    #print(office_dim[0])1
    for x in cubicles:
        for index, coord in enumerate(x):
            if index % 2:
                x[index] = office_dim[1] - x[index]  
            else:
                pass       
    return cubicles


def fill_building(bldg, cubicles, n_employees):
    #print(len(bldg), len(bldg[0]))
    for i in range(n_employees):
        dims = cubicles[i]
        x_min = min(dims[0], dims[2])
        x_max = max(dims[0], dims[2])
        y_max = max(dims[1], dims[3])
        y_min = min(dims[1], dims[3])
        
        for y in range(len(bldg)):
            for x in range(len(bldg[0])):
                if x_min <= x < x_max and y_min <= y <  y_max:
                    #print(x, y)
                    if bldg[y][x] == 1:
                        if x_min <= x <= x_max and y_min <= y < y_max:
                            bldg[y][x] += 1 
                    else:
                        bldg[y][x] = 1
        

    for x in bldg:
        line = [int(i) for i in x]

    return bldg

def total_office_area(bldg):
    return len(bldg[0]) * len(bldg)



            
def main():
  # read the data
  data = [line.strip().split(' ') for line in sys.stdin.readlines()]
  office_dim = [int(x) for x in data[0]]
  n_employees = [int(x) for x in data[1]][0]
  office_space_dict = {}
  cubicle_coords = []
  for x in data[2::]:
      office_space_dict[str(x[0])] = (int(x[1]),int(x[2]),int(x[3]),int(x[4]))
      cubicle_coords.append([int(x[1]),int(x[2]),int(x[3]),int(x[4])])
  cubicles = [x for x in office_space_dict.values()]


  bldg = [[0 for x in range(office_dim[0])] for x in range(office_dim[1])]
  

  cubicles = cubicles_to_array_form(cubicle_coords, office_dim)
 

  # fill in the array according to the given parameters
  # 0 = unfilled, 1,2,3,...n = n contested 
  bldg = fill_building(bldg, cubicles, n_employees)

  #print(len(bldg), len(bldg[0]))

  # run your test cases
  '''
  print (test_cases())
  '''

  # print the following results after computation

  # compute the total office space
  total_office = total_office_area(bldg)
  print(f'Total {total_office}')

  # compute the total unallocated space

  unallocated = unallocated_space(bldg)
  print(f'Unallocated {unallocated}')

  
  # compute the total contested space
  
  contested = contested_space(bldg)

  print(f'Contested {contested}')

  # compute the uncontested space that each employee gets

  #print(office_space_dict)
  
  for rect in zip(office_space_dict.items(), cubicles):
    print(rect[0][0], uncontested_space(bldg, rect[1]))



if __name__ == "__main__":
    main()