#  File: ExpressionTree.py

#  Description: Evaluate infix expression using trees, converts to pre and postfix

#  Student Name: Nicholas Kasper

#  Student UT EID: Nak874

#  Course Name: CS 313E

#  Unique Number: 52440

#  Date Created: 4/19/2021

#  Date Last Modified: 4/19/2021

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


def op(operator, num_a, num_b):
    if operator == '+':
        return num_a + num_b
    elif operator == '%':
        return num_a % num_b
    elif operator == '**':
        return num_a ** num_b
    elif operator == '-':
        return num_a - num_b
    elif operator == '*':
        return num_a * num_b
    elif operator == '//':
        return num_a // num_b
    elif operator == '/':
        return num_a / num_b
    
   


class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = Node(None)
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        exp = expr.split()

        stack = Stack()

        curr = Node()
        self.root = curr

        for element in exp:
            if element == '(':
                #new node as the left child of the current node.
                node_O = Node()
                curr.lChild = node_O
                # Push current node on the stack and make current node equal to the left child.
                stack.push(curr)
                curr = curr.lChild

            elif element == ')':
            #current node equal to the parent node 

                if not stack.is_empty():
                    curr = stack.pop()

            elif element in operators:

                #set the current data to the operator
                curr.data = element
                # push to stack, add new node of right child
                stack.push(curr)

                node_O = Node()
                curr.rChild = node_O
                curr = curr.rChild



            else:
                #set the current node's data value to the operand and pop to make equal
                curr.data = element 
                curr = stack.pop()



    
    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):

        if aNode.data is None:
            return 0
        if aNode.lChild is None and aNode.rChild is None:
            return float(aNode.data)
        
        if aNode.data in operators:
            return float(op(aNode.data, self.evaluate(aNode.lChild), self.evaluate(aNode.rChild)))

    
    


    def helper_pre(self, aNode, lst):
        # order is root, left, right
        if aNode != None:
            lst.append(aNode.data)
            self.helper_pre(aNode.lChild, lst)
            self.helper_pre(aNode.rChild, lst)
            
        return lst        

    def helper_post(self, aNode, lst):
        # order is left, right, root
        if aNode != None:
            self.helper_post(aNode.lChild, lst)
            self.helper_post(aNode.rChild, lst)
            lst.append(aNode.data)
        return lst        

    
     # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        out = self.helper_pre(aNode, [])

        output = ''
        for i in out:
            output += (str(i) + ' ')
        return output
        

    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        
        out = self.helper_post(aNode, [])

        output = ''
        for i in out:
            output += (str(i) + ' ')
        return output


# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()