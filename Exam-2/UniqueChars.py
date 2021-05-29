
#  File: UniqueChars.py

#  Description:

#  Student Name: Nick Kasper

#  Student UT EID: Nak874

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

import sys

# Input:  alphabet is a list of characters that you will
#         build your strings from.
#         n is an integer and is the length of the unique-character strings
#         that you will need to construct.
# Output: return a list of strings that are length n, are comprised only of
#         characters from alphabet, and have unique characters.




def unique(n, alphabet):
  '''Ex. unique(2, ['a', 'b', 'c']) -> ['ab', 'ac', 'ba', 'bc', 'ca', 'cb]'''
  len_set = len(alphabet)
  lst = []

  def rec(n, alphabet, len_set, string, lst):
    if n == 0:
      lst.append(string)
      exit

    for i in range(len_set):
      if alphabet[i] not in string:
        temp_str = string + alphabet[i] 
        rec(n-1, alphabet, len_set, temp_str, lst)

  rec(n, alphabet, len_set, '', lst)
  
  return lst
  
  

# ***There is no reason to change anything below this line***

def main():
  alphabet = sys.stdin.readline().split()
  n = int(sys.stdin.readline())

  result = unique(n, alphabet)
  result.sort()
  for r in result:
    print(r)

if __name__ == "__main__":
  main()
