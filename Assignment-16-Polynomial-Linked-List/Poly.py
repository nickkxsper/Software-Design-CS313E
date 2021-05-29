#  File: Poly.py

#  Description: Add, multiply polynomials using linked lists

#  Student Name: Nick Kasper

#  Student UT EID: Nak874

#  Course Name: CS 313E

#  Unique Number: 52240

#  Date Created: 4/15/2021

#  Date Last Modified: 4/15/2021

import sys

class Link (object):
  def __init__ (self, coeff = 1, exp = 1, next = None):
      self.coeff = coeff
      self.exp = exp
      self.next = next

  def __str__ (self):
    return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
  def __init__ (self):
    self.first = None

  # keep Links in descending order of exponents
  def insert_in_order (self, coeff, exp):
    link = Link(coeff, exp)
    if self.first == None:
        link.next = self.first
        self.first = link
    elif self.first.exp <= link.exp:
        link.next = self.first
        self.first = link
    else:   
        curr = self.first
        while curr.next != None and curr.next.exp > link.exp:
            curr = curr.next
        link.next = curr.next
        curr.next = link

  def get_num_links(self):
    num_links = 0
    if self.first == None:
        return 0
    else:
        curr = self.first
        while curr != None:
            num_links+=1
            curr = curr.next
    return num_links

  # add polynomial p to this polynomial and return the sum
  def add (self, p):
    summation = LinkedList()
    curr = self.first
    curr_p = p.first
    if curr == None:
        return p
    elif curr_p == None:
        return self
    
    #Use smallest list
    if self.get_num_links() <= p.get_num_links():
        while curr != None and curr_p != None:
            if curr.exp == curr_p.exp:
                if curr.coeff+curr_p.coeff != 0:
                    summation.insert_in_order((curr.coeff+curr_p.coeff), curr.exp)
                curr = curr.next
                curr_p = curr_p.next
            elif curr.exp > curr_p.exp:
                if curr.coeff != 0:
                    summation.insert_in_order(curr.coeff, curr.exp)
                curr = curr.next
            elif curr.exp < curr_p.exp:
                if curr_p.coeff != 0:
                    summation.insert_in_order(curr_p.coeff, curr_p.exp)
                curr_p = curr_p.next
    elif self.get_num_links() > p.get_num_links():
        while curr_p != None and curr != None:
            if curr.exp == curr_p.exp:
                if curr.coeff+curr_p.coeff != 0:
                    summation.insert_in_order((curr.coeff+curr_p.coeff), curr.exp)
                curr = curr.next
                curr_p = curr_p.next
            elif curr.exp > curr_p.exp:
                if curr.coeff != 0:
                    summation.insert_in_order(curr.coeff, curr.exp)
                curr = curr.next
            elif curr.exp < curr_p.exp:
                if curr_p.coeff != 0:
                    summation.insert_in_order(curr_p.coeff, curr_p.exp)
                curr_p = curr_p.next

    while curr != None:
        if curr.coeff != 0:
            summation.insert_in_order(curr.coeff, curr.exp)
        curr = curr.next
    while curr_p != None:
        if curr_p.coeff != 0:
            summation.insert_in_order(curr_p.coeff, curr_p.exp)
        curr_p = curr_p.next
    return summation

       
    
  # multiply polynomial p to this polynomial and return the product
  def mult (self, p):
    multiplicaton = LinkedList()
    curr = self.first
      
    while curr != None:
        p_link = p.first
        linked = LinkedList()

        # compare nodes

        while p_link != None:
            linked.insert_in_order(curr.coeff * p_link.coeff, curr.exp + p_link.exp)
            p_link = p_link.next
        curr = curr.next
        multiplicaton = multiplicaton.add(linked)
    return multiplicaton
      
  def simplify(self):
      if(self.first != None):
        curr = self.first
        while(curr != None):
            n_ptr = curr.next
            while(n_ptr != None and n_ptr.exp == curr.exp):
                curr.coeff += n_ptr.coeff
                curr.next = n_ptr.next
                n_ptr = n_ptr.next
            curr = curr.next
      
  # create a string representation of the polynomial
  def __str__ (self):
    string = ''
    curr = self.first
    if curr != None:
        string += f'({curr.coeff}, {curr.exp})'
        curr = curr.next
    while curr != None:
        string += f' + ({curr.coeff}, {curr.exp})'
        curr = curr.next
    return string
    
def main():
    # read data from file poly.in from stdin

    
    lines = [line for line in sys.stdin.readlines()]
    for i in range(len(lines)):
        lines[i] = lines[i].strip().split()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            lines[i][j] = int(lines[i][j])

    # create polynomial p
    p = LinkedList()

    # create polynomial q
    q = LinkedList()

    p_flag = True

    for line in lines:
        if line == []:
            p_flag = False
        if len(line) == 2:
            if p_flag:
                p.insert_in_order(line[0], line[1])
            else:
                q.insert_in_order(line[0], line[1])

    # get sum of p and q and print sum\
    added = q.add(p)
    added.simplify()
    print(f'{str(added)}')
    
    multiplied = q.mult(p)
    multiplied.simplify()

    # get product of p and q and print product
    print(f"{str(multiplied)}")

if __name__ == "__main__":
  main()