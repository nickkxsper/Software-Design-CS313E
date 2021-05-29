#  File: BalancingPairs.py

#  Description: 

#  Student Name: Nicholas Kasper

#  Student UT EID: Nak874

#  Course Name: CS 313E

#  Unique Number: 

import sys
def balancingPairs(strng):
	'''
	input type: String
	return type: Int
	'''

	stack = []

	for char in strng:
		if char == '(' or len(stack) == 0:
			stack.append(char)
		else:
			if stack[-1] == '(':
				stack.pop()
			else:
				stack.append(char)

	return len(stack)

def main():
	# read the input String
	f = sys.stdin
	unbalanced = f.readline().strip()
	print(balancingPairs(unbalanced))


if __name__ == "__main__":
 	 main()