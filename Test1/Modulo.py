#  File: Modulo.py

#  Description: Determines if a list of integers is closed under modulo (x % y is also a member # of the list for any nonzero x and y in the list)

#  Student Name: Nicholas Kasper

#  Student UT EID: Nak874

#  Course Name: CS 313E

#  Unique Number: 52240

import sys

# Input: lst is a list of positive integers that includes 0
# Output: return True if for any 2 nonzero elements x and y in the list, x % y is also in the list
# return False otherwise

def is_closed_modulo(lst):
    modulos = []
    hits = 0
    flag = True
    for i in lst:
        for j in lst:
            if i!= 0 and j!= 0:
                modulos.append(i%j)
    
    for i in modulos:
        if i in lst:
            continue
        else:
            flag = False

    return flag


def main(): 
    # read input file
    lst = [int(x) for x in sys.stdin.readline().strip().split(" ")]

    # get result from your call to is_closed_modulo()
    result = is_closed_modulo(lst)

    # print the result to standard output
    print(result)

if __name__ == "__main__":
    main()