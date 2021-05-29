# File: Triangle.py

# Description: A basic 2D Triangle class

# Student Name: Nick Kasper

# Student UT EID: Nak874

# Course Name: CS 313E

# Unique Number: 52240

import sys
import math

TOL = 0.01

class Point (object):
  # constructor
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

  # get the distance to another Point object
    def dist (self, other):
        return math.hypot (self.x - other.x, self.y - other.y)

class Triangle (object):
    def __init__(self, PointA, PointB, PointC):
        self.PointA = PointA
        self.PointB = PointB
        self.PointC = PointC
  
    def __str__(self):
        return 'Point1: (' + str(self.PointA.x) + ', ' + str(self.PointA.y) +'), Point2: (' +str(self.PointB.x) +', ' + str(self.PointB.y) +'), Point3: (' + str(self.PointC.x) + ', '+ str(self.PointC.y) +'), Area: ' +str(self.area())

    def __eq__(self, other):
        # congruent if every side on the triangle is of equal length to a corresponding side
        flag = False
        self_lengths = [Point.dist(self.PointA, self.PointB), Point.dist(self.PointB, self.PointC), Point.dist(self.PointC, self.PointA)]
        other_lengths = [Point.dist(other.PointA, other.PointB), Point.dist(other.PointB, other.PointC), Point.dist(other.PointC, other.PointA)]
        #print(self_lengths)
        #print(other_lengths)
        if self_lengths[0] in other_lengths and self_lengths[1] in other_lengths and self_lengths[2] in other_lengths:
          flag = True
        else:
          flag = False

        return flag


    def is_triangle(self):
        # check if any two sides are greater than the other side == Invalid
        if self.area() >= TOL:
          return True
        else:
          return False

    def area(self):
        self.tri_area = float(abs((self.PointA.x * (self.PointB.y - self.PointC.y) + self.PointB.x*(self.PointC.y-self.PointA.y) + self.PointC.x*(self.PointA.y - self.PointB.y))/2))
        return self.tri_area


######################################################
# The code below is filled out for you, DO NOT EDIT. #
######################################################

# takes a string of coordinates and changes it to a list of Points
def get_points(coords_str):
    coords = [float(c) for c in coords_str.split(" ")]
    return [Point(c[0], c[1]) for c in zip(*[iter(coords)]*2)]

def main():
    # read the two triangles
    pointsA = get_points(sys.stdin.readline().strip())
    pointsB = get_points(sys.stdin.readline().strip())

    triangleA = Triangle(pointsA[0], pointsA[1], pointsA[2])
    triangleB = Triangle(pointsB[0], pointsB[1], pointsB[2])

    # Print final output
    print(triangleA)
    print(triangleB)
    #print(triangleA.area())
    #print(triangleB.area())
    print(triangleA.is_triangle())
    print(triangleB.is_triangle())
    print(triangleA == triangleB)

if __name__ == "__main__":
    main()
