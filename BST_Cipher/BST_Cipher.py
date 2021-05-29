
#  File: BST_Cipher.py

#  Description: Encrypt/Decrypt a message with BST

#  Student Name: Nicholas Kasper

#  Student UT EID: Nak874   

#  Course Name: CS 313E

#  Unique Number: 52440

#  Date Created: 4/23/2021

#  Date Last Modified: 4/23/2021


import sys

# extra method to pre process input string
def process_str(string):
    chars = []
    for char in string:
        #a-z
        if ord(char) >= 97 and ord(char) <= 122:
            chars.append(char)
        #space
        elif ord(char) == 32:
            chars.append(char)
        # upper case
        elif 90 >= ord(char) >= 65:
            chars.append(char.lower())
    return chars

class Node(object):
    # contstructor
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None




class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encrypt_str):
    self.first = Node(None)
    self.str = encrypt_str
    encrypt_str = process_str(encrypt_str)

    for char in encrypt_str:
        self.insert(char)



  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):
        node = Node(ch)
        if self.first.data == None:
            self.first = node
            return

        else:
            curr = self.first
            parent = self.first
            while curr != None:
                parent = curr
                if  ch < curr.data:
                    curr = curr.lChild
                elif ch == curr.data:
                    break
                else:
                    curr = curr.rChild

            if (ch < parent.data):
                parent.lChild = node
            elif ch == parent.data:
                pass
            else:
                parent.rChild = node


  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the first of the tree.
  def search (self, ch):
    #if char first of tree, return *
    curr = self.first
    if curr.data == ch:
        return "*"

    stringz = ''

    while curr.data != None:
        if  ch < curr.data:
            stringz += '<'
            curr = curr.lChild
            
        elif ch > curr.data:
            stringz += '>'
            curr = curr.rChild
        elif curr.data == ch:
            return stringz

    #if empty string, return none
    #at end, reset string output
    if curr.data != ch:
        stringz = ''
        return stringz



  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
    curr = self.first

    for char in st:

        if char == "*":
            return self.first.data

        elif char == "<":
            try:
                curr = curr.lChild
            except:
                return ''
                break

        elif char == ">":
            try:
                curr = curr.rChild
            except:
                return ''
                break

        else:
            return ""
        
    return curr.data 

  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
        clean_string = process_str(st)
        #search for number in tree, add to stringz
        stringz = ''
        for char in clean_string:
            found = self.search(char)
            stringz += found
            stringz += "!"

        return stringz[:-1]


  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
        starter = st.strip().split('!')
        stringz = ""
        #print(starter)
        #find char and append to output string
        for chars in starter:
            #find char
                found = self.traverse(chars)
                stringz += found
        
        return stringz


def main():
  # read encrypt string
  line = sys.stdin.readline()
  encrypt_str = line.strip()

  # create a Tree object
  the_tree = Tree (encrypt_str)

  # read string to be encrypted
  line = sys.stdin.readline()
  str_to_encode = line.strip()

  # print the encryption
  print (the_tree.encrypt(str_to_encode))

  # read the string to be decrypted
  line = sys.stdin.readline()
  str_to_decode = line.strip()
  
  # print the decryption
  print (the_tree.decrypt(str_to_decode))
 
if __name__ == "__main__":  main()