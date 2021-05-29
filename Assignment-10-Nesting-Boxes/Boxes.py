#  File: Boxes.py

#  Description: returns largest number of boxes that can fit inside eachother and the number of sets of boxes that do fit

#  Student Name: Nicholas Kasper

#  Student UT EID: Nak874

#  Unique Number: 52240

#  Date Created: 3/23/2021

#  Date Last Modified: 3/23/2021


import sys

# generates all subsets of boxes and stores them in all_box_subsets
# box_list is a list of boxes that have already been sorted
# sub_set is a list that is the current subset of boxes
# idx is an index in the list box_list
# all_box_subsets is a 3-D list that has all the subset of boxes
def sub_sets_boxes (box_list, sub_set, idx, all_box_subsets):
    '''
    Recurse through box_list: append a box_list element on the next index (on the new subset or if no add to throw away)
    '''
    upper_bound = len(box_list)

    # base case = last index

    if idx == upper_bound:
        #add everything else to all_box_subsets
        all_box_subsets.append(sub_set)
        return
    
    # recursive case: create 2 subsets. Using binary tree, rerun with subset and a copy

    else:
        copy = sub_set[:]
        sub_set.append(box_list[idx])

        sub_sets_boxes(box_list, sub_set, idx+1, all_box_subsets)
        sub_sets_boxes(box_list, copy, idx+1, all_box_subsets)


# goes through all the subset of boxes and only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size keeps track what the largest subset is
def largest_nesting_subsets (all_box_subsets):
    '''
    First sort subsets by volume, then finds largest length of subset for max and number of boxes that fit
    '''

    sorted_subsets = sorted(all_box_subsets, key = len, reverse = True)

    # for each subset, sort each box list in the subset by volume

    for i in range(len(sorted_subsets)):
      sorted_subsets[i].sort(key = lambda x: x[0]*x[1]*x[2])
    
    box_max = 0
    box_count = 0

    for i in range(len(sorted_subsets)):
    
        flag = True
        subset = sorted_subsets[i]

          
        for j in range(len(subset[:-1])):

          if does_fit(subset[j], subset[j + 1]) == False: 
            flag = False
            break
            #count if it fits
        if flag == True:
                
            if len(subset) > box_max:
              box_max = len(subset)

            #if subset is < the max, break and go to next iteration
            if len(subset) < box_max:
              break
            #if each condition is met, add box
            else:
              box_count += 1

    return box_max, box_count




# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
  # read the number of boxes 
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)


  # print to make sure that the input was read in correctly
  '''
  print (box_list)
  print()
  
  '''
  # sort the box list
  box_list.sort()
  '''
  
  # print the box_list to see if it has been sorted.
  print (box_list)
  print()
  
  '''

  # create an empty list to hold all subset of boxes
  all_box_subsets = []

  # create a list to hold a single subset of boxes
  sub_set = []

  # generate all subsets of boxes and store them in all_box_subsets
  sub_sets_boxes (box_list, sub_set, 0, all_box_subsets)

  # all_box_subsets should have a length of 2^n where n is the number
  # of boxes

  # print(len(all_box_subsets))
  #print(2**num_boxes)

  # go through all the subset of boxes and only store the
  # largest subsets that nest in all_nesting_boxes

  all_nesting_boxes = largest_nesting_subsets (all_box_subsets)

  '''
  for subset in all_nesting_boxes:
    for box in subset:
      print(box)
    print()
  ''' 

  # print the largest number of boxes that fit

  print(all_nesting_boxes[0])
  

  # print the number of sets of such boxes
  print(all_nesting_boxes[1])

if __name__ == "__main__":
  main()




