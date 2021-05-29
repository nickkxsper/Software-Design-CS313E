#  File: Reducible.py

#  Description: Finds and returns longest reducible words from input list

#  Student Name: Nicholas Kasper

#  Student UT EID: Nak874

#  Course Name: CS 313E

#  Unique Number: 52240

#  Date Created: 4/1/2021

#  Date Last Modified: 4/1/2021
 



import sys

def is_prime ( n ):
  if (n == 1):
    return False

  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True


# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
  hash_index = 0
  for j in range (len(s)):
    char = ord (s[j]) - 96
    hash_index = (hash_index * 26 + char) % size
  return hash_index

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
  return const - hash_word(s,const)
  

# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
  n = len(hash_table)
  key = hash_word(s,n)
  if (hash_table[key] == ''):
    hash_table[key] = s
  else:
    # double hashing
    
    stepsize = step_size(s,17)
    key = (key + stepsize) % len(hash_table)
    while (hash_table[key]  != ''):
      key = (key + stepsize) % n
    hash_table[key] = s

# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
  # probe until theres a match
  n = len(hash_table)
  key = hash_word(s,n)
  stepsize = step_size(s,17)
    #key = (key + step_size) % len(hash_table)
  while (hash_table[key]  != ''):
    if hash_table[key] == s:
      return True
    else:
      key = (key + stepsize) % len(hash_table)
  return False



# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
  # base case 
  # 1) length 1 -> is it a, i, or o? 
  if len(s) == 1:
    if s == 'a' or s == 'i' or s == 'o':
      return True
    else:
      return False
  # base case
  # 2) if the word's not even a word in the hash table, its obviously false
  if not find_word(s, hash_table):
    return False
  
  # base case
  # 3) if the word is already in the hash memo, return true
  if find_word (s, hash_memo):
    return True


  for i in range(len(s)):
    alt_str = s[:i] + s[i + 1:]
    # now that we have a new string, we can check if its reducible. Then is it in the hash_memo? Not -> Add it
    if is_reducible (alt_str, hash_table, hash_memo):
      if not find_word(alt_str, hash_memo):
        insert_word(alt_str,hash_memo)
        print(hash_memo)
      return True
  return False

#finds next prime number after n
def next_prime(n):
  # check if its a prime, otherwise incrament by one and check again
  while is_prime(n) == False:
    n +=1
  return n

def largest_reducible(words):
    max_length = max([len(i) for i in words])
    largest = []
    for word in words:
        if len(word) == max_length:
            largest.append(word)
    return largest

    
    

def main():
    # create an empty word_list
    word_list = []

    # read words from words.txt and append to word_list
    for line in sys.stdin:
        line = line.strip()
        word_list.append (line)

    # find length of word_list
    length = len(word_list)


    # determine prime number N that is greater than twice
    # the length of the word_list

    bigger_prime = next_prime(2*length)


    # create an empty hash_list
    hash_list = ['' for i in range(bigger_prime)]

    
    # hash each word in word_list into hash_list
    # for collisions use double hashing 
    for word in word_list:
        insert_word(word, hash_list)


    # create an empty hash_memo of size M
    # we do not know a priori how many words will be reducible
    # let us assume it is 10 percent (fairly safe) of the words
    # then M is a prime number that is slightly greater than 
    # 0.2 * size of word_list

    M = next_prime(int(.2*len(word_list)))

    # populate the hash_memo with M blank strings
    hash_memo = ['' for i in range(bigger_prime)]

    # create an empty list reducible_words
    reducible_words = []

    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words
    # as you recursively remove one letter at a time check
    # first if the sub-word exists in the hash_memo. if it does
    # then the word is reducible and you do not have to test
    # any further. add the word to the hash_memo.

    for word in word_list:
        if is_reducible(word, hash_list, hash_memo):
            reducible_words.append(word)
    
    # find the largest reducible words in reducible_words

    largest = largest_reducible(reducible_words)


    # print the reducible words in alphabetical order
    # one word per line
    largest.sort()
    for word in largest:
        print(word)

if __name__ == "__main__":
  main()
  
