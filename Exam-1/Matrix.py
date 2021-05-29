#  File: Matrix.py

#  Description: Determines if a square 2d list of 1s and 0s has some "symmetry" where the matrix is 
#               the same after one of the following operations: rotate clockwise 90 degrees, rotate 
#               counterclockwise 90 degrees, flip horizontally, or flip vertically

#  Student Name: Nick Kasper

#  Student UT EID: Nak874

#  Course Name: CS 313E

#  Unique Number: 52240

import sys

# Prints your 2d list
# Can be used for debugging purposes
def print_arr(temp):
    mx = max((len(str(ele)) for sub in temp for ele in sub))
    for row in temp:
        print(" ".join(["{:<{mx}}".format(ele,mx=mx) for ele in row]))
    print()

def rotate_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            cell = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = cell
 
    # swap columns
    for i in range(len(matrix)):
        for j in range(len(matrix)// 2):
            cell = matrix[i][j]
            matrix[i][j] = matrix[i][len(matrix) - j - 1]
            matrix[i][len(matrix) - j - 1] = cell
    return matrix

def flip_matrix(matrix, hor_or_vert):

    if hor_or_vert =='vert':
        return matrix.reverse()
    else:
        for i in range(len(matrix)):
            matrix[i].reverse()
        return matrix 
# Input: matrix is a 2d square list of 1s and 0s
# Output: return True if a rotation by 90 degrees in either direction (clockwise/counterclockwise)
# or a horizontal/vertical flip results in the matrix being equal to itself.
# return False otherwise
def matrix_has_symmetry(matrix):

    rotated_90 = rotate_matrix(matrix)
    rotated_270 = rotate_matrix(rotate_matrix(rotated_90))
    hor_mat = flip_matrix(matrix, 'hor')
    vert_mat = flip_matrix(matrix, 'vert')

    if matrix == rotated_90 or matrix == rotated_270 or matrix == hor_mat or matrix == vert_mat:
        return True
    else:
        return False


def main(): 
    # read dimension of square matrix
    n = int(input())

    matrix = []
    # read data from standard input
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    #print(matrix)

    # get the result from your call to matrix_has_symmetry()
    result = matrix_has_symmetry(matrix)

    # print the result to standard output
    print(result)

if __name__ == "__main__":
    main()