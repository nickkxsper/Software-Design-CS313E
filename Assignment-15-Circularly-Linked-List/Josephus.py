#  File: Josephus.py

#  Description: Circularly Linked List Class and Tests

#  Student Name: Nicholas Kasper

#  Student UT EID: Nak874

#  Course Name: CS 313E

#  Unique Number: 52440

#  Date Created: 4/9/2021

#  Date Last Modified: 4/12/2021




import sys
class Link(object):
	# Constructor
	def __init__ (self, data, next = None):
		self.data = data
		self.next = next



class CircularList(object):
    # Constructor
    def __init__ (self): 
        self.first = None

    # Insert an element (value) in the list
    def insert (self, data):

        link = Link(data)
        curr = self.first

        if curr == None:
            self.first = link
            link.next = link
            self.first = link
            return

        first = curr
        while(curr.next != first):
            curr = curr.next
        curr.next = link
        link.next = first

    
	# Find the link with data
    def find (self, data):
        curr = self.first

     
        
        while (curr.data != data):
            if curr.next == self.first:
                return None
            curr = curr.next
            

        return curr
    

    # Delete a link with a given data
    def delete (self, data):
        curr = self.first
        prev = self.first

        if curr == None:
            return None
    
        
        if self.find(data) != None:
            while curr.data != data:
                prev = curr
                curr = curr.next
        else:
            return None

        if self.first == self.first.next:
            self.first = None
        
            
        prev.next = curr.next


    # Delete the nth Link starting from the Link start 
  	# Return the data of the deleted Link AND return the
  	# next Link after the deleted Link in that order
    def delete_after (self, start, n):
        curr = self.find(start)

        i = 1
        while i != n:
            curr = curr.next
            i +=1
        
        storage = curr.data
        print(storage)
        
        self.delete(curr.data)
        new_starting = curr


        return new_starting


	# Return a string representation of a Circular List
    def __str__ (self):

        line = "["
        current = self.first

        # traverse until we reach the starting link
        if self.first != None:
            while (current.next != self.first):
                line += str(current.data) + ", "
                current = current.next
            #line +=  (str(current.data) + ']')    
            return line + str(current.data) + ']'
        else:
            return '[]'
def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int(line)

    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int(line)

    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int(line)
    circle = CircularList()
    #insert the soldiers

    for i in range(1, num_soldiers + 1):
        circle.insert(i)

    for i in range(1, num_soldiers + 1):
        start_count = circle.delete_after(start_count, elim_num)
        start_count = start_count.data


if __name__ == '__main__': main()
