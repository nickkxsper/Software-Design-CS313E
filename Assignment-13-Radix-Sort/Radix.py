
#  File: Radix.py

#  Description: Uses Radix sort to sort number letter phrases

#  Student Name: Nicholas Kasper

#  Student UT EID: Nak874

#  Course Name: CS 313E

#  Unique Number: 52440

#  Date Created: 4/5/2021

#  Date Last Modified: 4/5/2021

import sys

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))

# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
    queues = []
    for i in range(37): #37 long because 26 letter, 10 digits, and a space
        queues.append(Queue())
  
    max_passes = max([len(i) for i in a])
  

    radix_storage = a
    
    # going from left to right on loop, enqueued all words for each iteration 

    for i in range(max_passes-1, -1, -1):
        for phrase in radix_storage:
        #get code for phrase
            if len(phrase) > i:  
                char = phrase[i]
                #convert numbers and letters, add to queue.
                if char.isdigit():
                    queue_id = int(char)
                elif char.isalpha():
                    queue_id = int(ord(char) - 87)
            else: 
                queue_id = 0
            queues[queue_id].enqueue(phrase)
    
        radix_storage = []

        #deque in order 
        for queue in queues:
            while not queue.is_empty():
              radix_storage.append(queue.dequeue())

    return radix_storage

def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  

  # use radix sort to sort the word_list
  sorted_list = radix_sort(word_list)

  # print the sorted_list
  print (sorted_list)

if __name__ == "__main__":
  main()

    