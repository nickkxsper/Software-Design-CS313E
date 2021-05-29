#  File: TopoSort.py

#  Description: Graph class with toposort, outputs if theres a cycle
# if theres a cycle, we can do toposort

#  Student Name: Nicholas Kasper

#  Student UT EID: Nak874

#  Course Name: CS 313E

#  Unique Number: 52440

#  Date Created: 5/1/2021

#  Date Last Modified: 5/1/2021

import sys
class Stack (object):
	def __init__ (self):
		self.stack = []

	# add an item to the top of the stack
	def push (self, item):
		self.stack.append (item)

	# remove an item from the top of the stack
	def pop (self):
		return self.stack.pop()

	# check the item on the top of the stack
	def peek (self):
		return self.stack[-1]

	# check if the stack if empty
	def is_empty (self):
		return (len (self.stack) == 0)

	# return the number of elements in the stack
	def size (self):
		return (len (self.stack))


class Queue (object):
	def __init__ (self):
		self.queue = []

	# add an item to the end of the queue
	def enqueue (self, item):
		self.queue.append (item)

	# remove an item from the beginning of the queue
	def dequeue (self):
		return (self.queue.pop(0))

	# check if the queue is empty
	def is_empty (self):
		return (len (self.queue) == 0)

	# return the size of the queue
	def size (self):
		return (len (self.queue))


class Vertex (object):
	def __init__ (self, label):
		self.label = label
		self.visited = False

	# determine if a vertex was visited
	def was_visited (self):
		return self.visited

	# determine the label of the vertex
	def get_label (self):
		return self.label

	# string representation of the vertex
	def __str__ (self):
		return str (self.label)


class Graph (object):
	def __init__ (self):
		self.vertices = []
		self.adjmatrix = []

	# check if a vertex is already in the graph
	def has_vertex (self, label):
		n_vertex = len(self.vertices)
		for i in range (n_vertex):
			if label == (self.vertices[i]).get_label():
				return True
		return False

	# given the label get the index of a vertex
	def get_index (self, label):
		n_vertex = len (self.vertices)
		for i in range (n_vertex):
			if label == (self.vertices[i]).get_label():
				return i
		return -1

	# add a Vertex with a given label to the graph
	def add_vertex (self, label):
		if self.has_vertex (label):
			return

		# add vertex to the list of vertices
		self.vertices.append(Vertex(label))

		# add a new column in the adjacency matrix
		n_vertex = len (self.vertices)
		for i in range (n_vertex - 1):
			self.adjmatrix[i].append(0)

		# create next row
		next_row = []
		for i in range (n_vertex):
			next_row.append (0)
		self.adjmatrix.append (next_row)

	# add weighted directed edge to graph
	def add_directed_edge (self, start, finish, weight = 1):
		self.adjmatrix[start][finish] = weight

	# add weighted undirected edge to graph
	def add_undirected_edge (self, start, finish, weight = 1):
		self.adjmatrix[start][finish] = weight
		self.adjmatrix[finish][start] = weight

	# get edge weight between two vertices
	# return -1 if edge does not exist
	def get_edge_weight (self, fromVertexLabel, toVertexLabel):
		weight = self.adjmatrix[self.get_index(fromVertexLabel)][self.get_index(toVertexLabel)]
		if (weight != 0):
			return (weight)
		return -1
	
	# get a list of immediate neighbors that you can go to from a vertex
	# return a list of indices or an empty list if there are none
	def get_neighbors (self, vertexLabel):
		neighbors = []
		vtx_idx = self.get_index(vertexLabel)
		for i in range(len(self.vertices[vtx_idx])):
			if  self.vertices[vtx_idx][i] != 0:
				neighbors.append(self.vertices[vtx_idx][i])
		return neighbors
		
	# return an unvisited vertex adjacent to vertex v (index)
	def get_adj_unvisited_vertex (self, v):
		n_vertex = len (self.vertices)
		for i in range (n_vertex):
			if self.adjmatrix[v][i] > 0:
				if not self.vertices[i].was_visited():
					return i
		return -1

	# get a copy of the list of Vertex objects
	def get_vertices (self):
		for i in range(len(self.vertices)):
			print(self.vertices[i])

	# do a depth first search in a graph
	def dfs (self, v):
		# make stack
		stack = Stack()

		# mark as visited, push back to stack
		self.vertices[v].visited = True
		print (self.vertices[v])
		stack.push (v)

		# visit other vertices
		while (not stack.is_empty()):
			# get an adjacent unvisited vertex
			unvisited = self.get_adj_unvisited_vertex (stack.peek())
			if  unvisited == -1:
				unvisited = stack.pop()
			else:
				self.vertices[unvisited].visited = True
				print(self.vertices[unvisited])
				stack.push (unvisited)

		# if empty, reset 
		n_vertex = len (self.vertices)
		for i in range (n_vertex):
			self.vertices[i].visited = False
	
	# do a breadth first search in a graph starting at vertex v (index)
	def bfs (self, v):
		# make queue
		bfs_queue = Queue()

		# make starting vertex and mark visited by unqueue
		self.vertices[v].visited = True
		print (self.vertices[v])
		bfs_queue.enqueue(v)

		# 2. Visit unvisited vertex in order, mark visited
		# 3. If not unvisited, pop vertex from stack and make it current vertex 
		while not bfs_queue.is_empty():
			vtx_1 = bfs_queue.dequeue()
			vtx_2 = self.get_adj_unvisited_vertex(vtx_1)
			while (vtx_2 != -1):
				self.vertices[vtx_2].visited = True
				print (self.vertices[vtx_2])
				bfs_queue.enqueue (vtx_2)
				vtx_2 = self.get_adj_unvisited_vertex(vtx_1)

		# keep going until no queue (empty)
		num_vertices = len (self.vertices)
		for i in range (num_vertices):
			self.vertices[i].visited = False

	# delete an edge from the adjacency matrix
	# delete a single edge if the graph is directed
	# delete two edges if the graph is undirected
	def delete_edge (self, fromVertexLabel, toVertexLabel):
		start = self.get_index(fromVertexLabel)
		stop = self.get_index(toVertexLabel)
		self.adjmatrix[start][stop] = 0
		self.adjmatrix[stop][start] = 0

	# delete a vertex from the vertex list and all edges from and
	# to it in the adjacency matrix
	def delete_vertex (self, vertexLabel):
		vtx_idx = self.get_index(vertexLabel)
		del(self.vertices[vtx_idx])
		del(self.adjmatrix[vtx_idx])
		for i in range(len(self.vertices)):
			del(self.adjmatrix[i][vtx_idx])
    
	def has_successor(self, vertex):
			for i in range(len(self.vertices)):
					if (self.adjmatrix[i][self.get_index(vertex.get_label())]) != 0:
							return True

			return False



	def adj_unvisited(self, vtx):
		n_vert = len(self.vertices)

		for i in range(n_vert):
			if self.adjmatrix[vtx][i] > 0 and not self.vertices[i].was_visited():
				return i

		return -1
  # determine if a directed graph has a cycle
  # this function should return a boolean and not print the result
	def has_cycle(self):

		stack = Stack()

		# push back to stack after visiting
		for i in range(len(self.vertices)):
			self.vertices[i].visited = True
			stack.push(i)

			# vist other vertices 
			while (not stack.is_empty()):
				adj = self.adj_unvisited(stack.peek())
				if (adj == -1):
					adj = stack.pop()
				elif (self.adjmatrix[adj][i] == 1):
						return True
				else:
					self.vertices[adj].visited = True
					stack.push(adj)
			# the stack is empty let us reset the flags
			n_vert = len (self.vertices)
			for i in range (n_vert):
				self.vertices[i].visited = False

		return False

			



  # return a list of vertices after a topological sort
  # this function should not print the list
	def toposort (self):


			queue = Queue()

			# determine in degree for all vertices, remove those with 0. sort listt and enqueue erices

			while len(self.vertices) > 0:

					vertices = []

					for i in range(len(self.vertices)):

							if not(self.has_successor(self.vertices[i])):
									
									vertices.append(self.vertices[i].get_label())

					
					#prepare for next iteration
					vertices.sort()
					vertices.reverse()

					for i in range(len(vertices)-1, -1, -1):
							queue.enqueue(vertices[i])
							self.delete_vertex(vertices[i])

			
			vertex_q = []

			# dequeue and append
			while not queue.is_empty():
					vertex_q.append(queue.dequeue())

			
			return vertex_q




def main():
	# create a Graph object
	theGraph = Graph()


	n_vertices = int(sys.stdin.readline().strip())
	#print(n_vertices)



	for i in range(n_vertices):
			letter = sys.stdin.readline().strip()
			theGraph.add_vertex(letter)

	
	n_edges = int(sys.stdin.readline().strip())

	#print(n_edges)

	for i in range(n_edges):

			edge = sys.stdin.readline()
			edge = edge.strip()
			edge = edge.split()

			#print(edge)

			begin = theGraph.get_index(edge[0])
			end = theGraph.get_index(edge[1])

			theGraph.add_directed_edge(begin, end)


	# test if a directed graph has a cycle
	if (theGraph.has_cycle()):
			print ("The Graph has a cycle.")
	else:
			print ("The Graph does not have a cycle.")

	# test topological sort
	if (not theGraph.has_cycle()):
			vertex_list = theGraph.toposort()
			print ("\nList of vertices after toposort")
			print (vertex_list)

main()