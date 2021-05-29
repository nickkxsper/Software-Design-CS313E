
#  File: Cipher.py

#  Description: 

#  Student Name: Nicholas Kasper

#  Student UT EID: Nak874


#  Course Name: CS 313E

#  Unique Number: 52240

#  Date Created: 02/08/2021

#  Date Last Modified: 2/08/2021

import sys
import math


# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def encrypt(strng):
    L = len(strng)
    M = (math.ceil(math.sqrt(L)))**2
    

    for i in range(M-L):
        strng += '*'

    
    grid = []
    index = 0

    # loop through the square root of the size (N x N), add input to cell or
    # a star if its out of bounds

    for i in range(int(M**.5)):
        row = []
        for j in range(int(M**.5)):
            try:
                row.append(strng[index])
            except:
                row.append('*')
            index += 1
        
        grid.append(row)

    rotate = zip(*grid[::-1])
    message = []

    for i in rotate:
        for j in i:
            if j == '*':
                continue
            else:
                message.append(j)
    
    return ''.join(message)



# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt(strng):

    L = len(strng)
    M = (math.ceil(math.sqrt(L)))**2


    grid = []
    index = 0

    # loop through the square root of the size (N x N), add input to cell or
    # a star if its out of bounds


    for i in range(int(M**.5)):
        row = []
        for j in range(int(M**.5)):
            try:
                row.append(strng[index])
            except:
                row.append('*')
            index += 1
        grid.append(row)


    rotate = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0])-1,-1,-1)]

    #print(rotate) 
    # extract message

    message = ''

    for i in rotate:
        for j in i:
            message += j
    
    return message.replace('*', '')

    

def main():
  # read the two strings P and Q from standard imput
  data = [x.strip() for x in sys.stdin.readlines()]
  #print(sys.stdin.read().strip().split('\n')[1])
  p = data[0]
  #print(p)
  q = data[1]
  #print(q)
  # encrypt the string P

  encrypted = encrypt(p)
  
  # decrypt the string Q

  decrypted = decrypt(q)

  # print the encrypted string of P and the 
  # decrypted string of Q to standard out

  print(encrypted)
  print(decrypted)
if __name__ == "__main__":
  main()