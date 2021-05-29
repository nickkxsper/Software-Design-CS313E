import sys

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  # insert data into the tree
  def insert (self, data):
    new_node = Node (data)

    if (self.root == None):
      self.root = new_node
      return
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (data < current.data):
          current = current.lchild
        else:
          current = current.rchild

      # found location now insert node
      if (data < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # ***There is no reason to change anything above this line***

  # Returns an integer representing the sum of the leaf nodes
  def get_leaf_sum(self):

    root = self.root
    global count
    count = 0
    
    


    def helper(node):
      global count
      
      #print(leaf_sum)
      if node is None:
        return 

      #check if leaf
      if node.lchild == None and node.rchild == None:
        count += node.data

      #recurse
      helper(node.lchild)
      helper(node.rchild)

    helper(root)

    return count

  
 

# ***There is no reason to change anything below this line***

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree_input = list (map (int, line))    # converts elements into ints

    tree = Tree()
    for i in tree_input:
      tree.insert(i)

    print(tree.get_leaf_sum())

if __name__ == "__main__":
  main()