#  File: TestLinkedList.py

#  Description: Singly Linked List Class and Tests

#  Student Name: Nicholas Kasper

#  Student UT EID: Nak874

#  Course Name: CS 313E

#  Unique Number: 52440

#  Date Created: 4/9/2021

#  Date Last Modified: 4/9/2021

class Link (object):
    # constructor
    def __init__ (self, data, next = None):
	    self.data = data
	    self.next = next
    def __str__(self):
        return str(self.data)

class LinkedList (object):
    # create a linked list
    # you may add other attributes
    def __init__ (self):
        self.first = None

    # get number of links 
    def get_num_links (self):
        link = self.first
        if link == None:
            return 0
        
        else:
            counter = 1
            while link.next != None:
                link = link.next
                counter +=1
        
        return counter
  
    # add an item at the beginning of the list
    def insert_first (self, data): 
        link = Link(data)
        link.next = self.first
        self.first = link


    # add an item at the end of a list
    def insert_last (self, data): 
        link = Link(data)
        this_link = self.first

        if this_link == None:
            self.first = link
            return
        
        while this_link.next != None:
            this_link = this_link.next
            
        this_link.next = link
                

    # add an item in an ordered list in ascending order
    # assume that the list is already sorted
    def insert_in_order (self, data):
        link = Link(data)

        this_link = self.first

        last_link = self.first

        if this_link == None or data <= this_link.data:
            link.next = self.first
            self.first = link
            return

        while this_link.next != None:
            if  this_link.data <= data:
                last_link = this_link
                this_link = this_link.next
            else:
                link.next = last_link.next
                last_link.next = link
                return

        if  this_link.data <= data: 
            this_link.next = link
        else:
            link.next = last_link.next
            last_link.next = link


    # search in an unordered list, return None if not found
    def find_unordered (self, data):
        this_link = self.first
        
        if this_link == None:
            return None
        
        while data != this_link.data:
            if this_link.next == None:
                return None
            else:
                this_link = this_link.next
            
        return this_link

    # Search in an ordered list, return None if not found
    def find_ordered (self, data):
        this_link = self.first

        if (this_link == None):
            return None 
        
        else:

            while this_link.data != data:
                if (this_link.next == None):
                    return None
                else:
                    if this_link.next.data > data:
                        return None
                    else:
                        this_link = this_link.next

            return this_link

    # Delete and return the first occurrence of a Link containing data
    # from an unordered list or None if not found
    def delete_link (self, data):
        this_link = self.first
        last_link = self.first
        
        if  this_link == None:
            return None

        while this_link.data != data:
            if  this_link.next == None:
                return None
            else:
                last_link = this_link
                this_link = this_link.next

        if this_link == self.first:
            self.first = self.first.next
        else:
            last_link.next = this_link.next

        return this_link


    # String representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):
        string = ''
        cur = self.first
        n_on_line = 0

        while (cur != None):
            string += str(cur.data) + "  "
            cur = cur.next
            # increment by 1, dont go to new line till 10
            n_on_line += 1
            
            if (n_on_line == 10):
                string += "\n"
                # restart counter
                n_on_line = 0
    

        return string[0:-2]


    # Copy the contents of a list and return new list
    # do not change the original list
    def copy_list (self):
        list_new = LinkedList()
        last_link = self.first
		
		# copy from end of the list
        while last_link != None:
            list_new.insert_last(last_link.data)
            last_link = last_link.next

        return list_new

    # Reverse the contents of a list and return new list
    # do not change the original list
    def reverse_list (self): 
        list_new = LinkedList()
        cur = self.first
        
        # go from front -> back so its in reverse
        while (cur != None):
            list_new.insert_first(cur.data)
            cur = cur.next

        return list_new

    # Sort the contents of a list in ascending order and return new list
    # do not change the original list
    def sort_list (self): 
        list_new = LinkedList()
        curr = self.first

        while (curr != None):
            # ascending
            list_new.insert_in_order(curr.data)
            if (curr.next != None):
                curr = curr.next
            else:
                break 

        return list_new


    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted (self):
        current = self.first
        if self.is_empty() or self.get_num_links == 1:
            return True
      
        for i in range(self.get_num_links() - 1):
            if current.data > current.next.data:
                return False
            current = current.next
            return True 
    # Return True if a list is empty or False otherwise
    def is_empty (self): 
        if self.first == None:
            return True
        else:
            return False

    # Merge two sorted lists and return new list in ascending order
    # do not change the original lists
    def merge_list (self, other): 
        # check if both list are empty

        current = other.first
        merged_list = self.copy_list().sort_list()

        if self.is_empty():
            if other.is_empty():
                return merged_list
            else:
                merged_list = other.copy_list()
                return merged_list
    
        elif other.is_empty():
            return merged_list

        for i in range(other.get_num_links()):
            merged_list.insert_in_order(current.data)
            current = current.next
      
        return merged_list
            
        

        first_self = self.first
        first_other = other.first
		
        # go through each list in entirety
        while ((first_self  != None) and (first_other != None)):
            if (first_self.data <= first_other.data):
                new_list.insert_last(first_self.data)
                first_self = first_self.next
            else: 
                new_list.insert_last(first_other.next)
                first_other = first_other.next

		
        # sort self list
        if first_self == None:
            while first_other != None:
                new_list.insert_last(first_other.data)
				
                if first_other.next == None:
                    break
                else:
                    first_other = first_other.next				

		# sort list other
        if first_other == None:
            while first_self != None:
                new_list.insert_last(first_self.data)
					
                if first_self.next == None:
                    break
                else:
                    first_self = first_self.next

        string= ""
        curr = new_list.first
        while new_list != None:
            string += str(curr.data) + "  "
            if curr.next == None:
                break
            else:
                curr = curr.next 
        return string[0:-2]



    # Test if two lists are equal, item by item and return True
    def is_equal (self, other):
        if self.get_num_links() != other.get_num_links():
            return False
      
        if self.is_empty() and other.is_empty():
            return True

        first_self = self.first
        first_other = other.first
    
        for i in range(self.get_num_links()):
            if first_self.data != first_other.data:
                return False
            first_self = first_self.next
            first_other = first_other.next
      
        return True

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    # do not change the original list
    def remove_duplicates (self):
        list_new = LinkedList()
        curr = self.first
        rolling_list = []
        
        while (curr != None):
            # check if theres even a value
            if (curr.data in rolling_list):
                pass
            else:
                rolling_list.append(curr.data)
                list_new.insert_last(curr.data)
		    
            curr = curr.next

        return list_new

def main():
    ### Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.

    special_list = [11, 12, 10, 3, 50, 22, 43, 36, 29, 91, 99, 100]
    print("Testing method insert_first and __str__")
    list_1 = LinkedList()
    
    for num in special_list:
        list_1.insert_first(num)
    print(list_1)
    print('')
    

    ### Test method insert_last()
    print("Testing method insert_last")
	# create new Linked List 
    list_2 = LinkedList()
    for num in special_list:
        list_2.insert_last(num)
    print(list_2)
    print('')
    


    ### Test method insert_in_order()

    print("Testing method insert_in_order")

	# create new LinkedList
    list_3 = LinkedList()
    for num in special_list:		
        list_3.insert_in_order(num)
    print(list_3)
    print('')
    

    ### Test method get_num_links()

    print("Testing method get_num_links")
    
    # create new LinkedList
    list_4 = LinkedList()

    for num in special_list:		
        list_4.insert_first(num)

    print(list_4.get_num_links())
    print('')
	

    # Test method find_unordered() 
    # Consider two cases - data is there, data is not there 
    
    print("Testing method find_unordered")

    list_5 = LinkedList()

	
    #item is not there
    print('Is 11 in the list?')
    print(list_5.find_unordered(11) != None)
    print('')
	# item is there
    print('Is 9 in the list?')
    print(list_5.find_unordered(9) == None)
    print('')

    
    list_6 = LinkedList()
    # Test method find_ordered() 
    # Consider two cases - data is there, data is not there 
    print("Testing method find_ordered")
    #item is there
    print('Is 11 in the list?')
    print(list_6.find_ordered(11) != None)
    print('')
    # item is not there
    print('Is 9 in the list?')
    print(list_6.find_ordered(9) == None)
    print('')

    
    # Test method delete_link()
    # Consider two cases - data is there, data is not there 
    list_7 = LinkedList()
    for num in special_list:		
        list_7.insert_last(num)
    print("Testing method delete_link")
    #item is there
    print('Item is there')
    print(list_7.delete_link(100))
    print('')
    #item is not there
    print('Item is not there')
    print(list_7.delete_link(9) == None)
    print('')

    '''
    # Test method copy_list()
    list_8 = LinkedList()
    for num in special_list:
        list_8.insert_in_order(num)

    print("Test method copy_list")
    print(list_8.copy_list())
    print('')

    
    # Test method reverse_list()
    list_9 = LinkedList()
    for num in special_list:		
        list_9.insert_in_order(num)
    
    print("Testing method reverse_list")
    print(list_9.reverse_list())
    print('')



    # Test method sort_list()

    list_10 = LinkedList()
    for num in special_list:		
        list_10.insert_in_order(num)
    
    print("Testing method sort_list")
    print(list_10.sort_list())
    print('')



    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    print("Testing method is_sorted")
    list_11 = LinkedList()
    for num in special_list:		
        list_11.insert_in_order(num)
	# Consider two cases - list is sorted, list is not sorted

    print('When Sorted')
    sorted_ = list_11.sort_list()
    print(sorted_.is_sorted() == True)


	#print(list11)
    print('When Not Sorted')
    print(list_11.is_sorted() != True)
    print('')


    # Test method is_empty()
    print("Test method is_empty")
    list_12 = LinkedList()
    for num in special_list:		
        list_12.insert_in_order(num)

    print(list_12.is_empty())
    print('')


    # Test method merge_list()
    special_list_2 = [1, 6, 3, 99, 29]
    list_13 = LinkedList()
    for num in special_list:		
        list_13.insert_in_order(num)
    
    merge = LinkedList()
    for num in special_list_2:		
        merge.insert_in_order(num)

    
    print("Testing method merge_list")
    print(list_13)
    print(merge)
    print(list_13.merge_list(merge))
    print()


    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal

    special_list_3 = [72, 79, 12, 90, 11]

    list_14 = LinkedList()
    for num in special_list_3:		
        list_14.insert_in_order(num)
    special_list_4 = [20, 21, 44, 32, 42, 11, 13, 88, 99, 1, 81, 91]

    list_15 = LinkedList()
    for num in special_list_4:		
        list_15.insert_in_order(num)

    print("Testing method is_equal")
    print(special_list_3)
    print(special_list_4)
	# Consider two cases - lists are equal, lists are not equal
    print(list_15.is_equal(list_14))
    print('')
	

    # Test remove_duplicates()
    list_16 = LinkedList()
    for num in special_list_3:		
        list_16.insert_in_order(num)
        
    print("Testing method remove_duplicates")
    print(list_16)

    list_16.insert_in_order(90)
    

    print(list_16)
    print(list_16.remove_duplicates())
    print('')
    '''
if __name__ == "__main__":
    main()
