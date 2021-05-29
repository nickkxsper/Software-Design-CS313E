#  File: TestBinaryTree.py

#  Description: Tests multiple binary tree methods

#  Student Name: Nicholas Kasper

#  Student UT EID: Nak874  

#  Course Name: CS 313E

#  Unique Number: 52440

#  Date Created: 4/26/2021

#  Date Last Modified: 4/26/2021

import sys


def height(node): 
    if node == None: 
        return 0  
    # Compute the depth of each subtree 
    else:
        left = height(node.lchild) 
        right = height(node.rchild) 

        h = max (left, right)

        return h + 1

class Node (object):
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
  
    def has_child(self):
        return self.lchild != None or self.rchild != None

class Tree (object):
    def __init__(self):
        self.root = None


    def helper_pre(self, aNode, lst):
        # order is root, left, right
        if aNode != None:
            lst.append(aNode.data)
            self.helper_pre(aNode.lchild, lst)
            self.helper_pre(aNode.rchild, lst)
            
        return lst        
    
    def in_order(self, aNode, lst):
        if aNode != None:
            self.in_order(aNode.lchild, lst)
            lst.append(aNode.data)
            self.in_order(aNode.rchild, lst)

            return lst

    def helper_post(self, aNode, lst):
        # order is left, right, root
        if aNode != None:
            self.helper_post(aNode.lchild, lst)
            self.helper_post(aNode.rchild, lst)
            lst.append(aNode.data)
        return lst        
         
    def insert (self, ch):
        node = Node(ch)
        if self.root == None:
            self.root = node
            return

        else:
            curr = self.root
            parent = self.root
            while curr != None:
                parent = curr
                if  ch < curr.data:
                    curr = curr.lchild
                else:
                    curr = curr.rchild

            if (ch < parent.data):
                parent.lchild = node
        
            else:
                parent.rchild = node
    # Returns true if two binary trees are similar
    def is_similar (self, pNode):
        # pre order

        pre_self = self.helper_pre(self.root, [])
        pre_p = self.helper_pre(pNode.root, [])
      
        # post order

        post_self = self.helper_post(self.root, [])
        post_p = self.helper_post(pNode.root, [])

        # in order

        in_self = self.in_order(self.root, [])
        in_p = self.in_order(pNode.root, [])

        return pre_self == pre_p and post_self ==post_p and in_self == in_p


    # Returns a list of nodes at a given level from left to right
    def get_level (self, level): 

        if level < 0:
            return []
        
        lst = []
        def get_level_helper(level, node, lst):

            if node != None:
                if level == 0:
                    lst.append(node)
                
                else:
                    get_level_helper(level -1, node.lchild, lst)
                    get_level_helper(level -1, node.rchild, lst)
        get_level_helper(level, self.root, lst)
        return lst

    # Returns the height of the tree
    def get_height (self): 
        if(self.root == None):
            return 0
        def get_height_helper(node, height):
            if node != None:
                if not node.has_child():
                    return height
                else:
                    if node.lchild != None and node.rchild != None:
                        return max(get_height_helper(node.lchild, height + 1), get_height_helper(node.rchild, height + 1))
                    elif node.lchild != None:
                        return get_height_helper(node.lchild, height + 1)
                    else:
                        return get_height_helper(node.rchild, height + 1)
            return 0
        return get_height_helper(self.root, 0) + 1
    
    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes (self):

        def num_nodes_helper(node):
            if node == None:
                return 0
            
            return 1 + num_nodes_helper(node.lchild) + num_nodes_helper(node.rchild)

        return num_nodes_helper(self.root)
def main():
    
    # Create three trees - two are the same and the third is different
	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree1_input = list (map (int, line)) 	# converts elements into ints

	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree2_input = list (map (int, line)) 	# converts elements into ints

	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree3_input = list (map (int, line)) 	# converts elements into ints

    # Test your method is_similar()

    # Print the various levels of two of the trees that are different

    # Get the height of the two trees that are different

    # Get the total number of nodes a binary search tree


if __name__ == "__main__":
     main()