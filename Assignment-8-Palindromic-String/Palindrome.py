#  File: Palindrome.py

#  Description: Finds and returns smallest palindrome by taking original string and adding to the front

#  Student Name: Nick Kasper

#  Student UT EID: Nak874

#  Course Name: CS 313E

#  Unique Number: 52240

#  Date Created: 3/8/2021

#  Date Last Modified: 3/8/2021

import sys

# Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a string that is the smallest palindrome that can be 
#         made by adding characters to the start of the input string
def smallest_palindrome(string):
    if len(string) == 1:
        return string 

    reversed_string = string[::-1]

    # go through length of reversed string n and add the first i elements of the reveresed string to the original string
    # if the original string started with that segment
    for i in range(len(string)):
        if string.startswith(reversed_string[i:]):
            return reversed_string[:i] + string
                
# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases

  return "all test cases passed"

def main():
    # run your test cases
    '''
    print (test_cases())
    '''
    lines = [x.strip() for x in sys.stdin.readlines()]
    
    for strings in lines:
        print(smallest_palindrome(strings))

    

    # print the smallest palindromic string that can be made for each input

if __name__ == "__main__":
  main()