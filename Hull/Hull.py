#  File: Hull.py

#  Description: Takes a set of points on a 2d plane, forms the convex hull using grahams algo, and calculates the area
# using determinants

#  Student Name: Nicholas Kasper

#  Student UT EID: Nak874

#  Course Name: CS 313E

#  Unique Number: 52240

#  Date Created: 03/01/2021

#  Date Last Modified: 03/01/2021

import sys
import math
class Point (object):
    # constructor with default values
    def __init__ (self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y
    # get the distance to another Point object
    def dist (self, other):
        return math.hypot (self.x - other.x, self.y - other.y)

    # string representation of a Point
    def __str__ (self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # equality tests of two Points
    def __eq__ (self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

    def __ne__ (self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

    def __lt__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
            else:
                return (self.y < other.y)
        return (self.x < other.x)

    def __le__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y <= other.y)
        return (self.x <= other.x)

    def __gt__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
        else:
            return (self.y > other.y)
        return (self.x > other.x)

    def __ge__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
        else:
            return (self.y >= other.y)
        return (self.x >= other.x)


def det(p,q,r):
    '''
    p,q,r = Point Objects
    Returns Determinant (3x2 matrix)
    '''
    return (p.x * q.y + q.x * r.y + r.x * p.y - p.y * q.x - q.y * r.x - r.y* p.x)



def convex_hull (sorted_points):
    '''
    Uses grahams algorithm to first form an upper hull, then extends upper hull with a lower hull
    creating the covnex hull

    sorted_points = Point Objects

    returns Set of Point Objects representing convex hull
    '''
    
    coordinates = sorted_points
    length = len(coordinates)
 
    
    upper_hull = []
    upper_hull.append(coordinates[0])
    upper_hull.append(coordinates[1])
    
    # iterate through points, append index value and delete the second to last point if determinant is less than 
    # or equal to 0
    
    for i in range(2, len(coordinates)):
        upper_hull.append(coordinates[i])
        while len(upper_hull) >= 3:
            if det(upper_hull[-1], upper_hull[-2], upper_hull[-3]) <= 0:
                del upper_hull[-2]
            else:
                break
 
        
    # lower hull
    lower_hull = []
    lower_hull.append(coordinates[length - 1])
    lower_hull.append(coordinates[length - 2])
    
    # iterate through points, append index value and delete the second to last point if determinant is less than 
    # or equal to 0
    for j in range(length - 3, -1, -1):
        lower_hull.append(coordinates[j])
        while(len(lower_hull) >= 3):
            if det(lower_hull[-1], lower_hull[-2], lower_hull[-3]) <= 0:
                del(lower_hull[-2])
            else:
                break
    del lower_hull[-1]
    del lower_hull[0]
 

 
    convex_hull = upper_hull + lower_hull
   
 
    return convex_hull

def area_poly(convex_poly):
    '''
    convex_poly = Convex hull from convex_hull (Objects)

    returns area using determinant through all the points adding/subtracting diagonally (thx for the illustration)
    '''
    det = 0
    
    for i in range(len(convex_poly) -1):
        det += (convex_poly[i + 1].y * convex_poly[i].x ) - (convex_poly[i +1].x * convex_poly[i].y)
    det_temp = (convex_poly[0].y * convex_poly[len(convex_poly)-1].x) - (convex_poly[0].x * convex_poly[len(convex_poly)-1].y)
    det += det_temp
    area = 1/2 * abs(det)
    return area
    



def read_input(data):
    '''
    data = Input data stripped and splitted on \t
    Makes point objects for each line in the data, returns list of point objects 

    '''
    points = []
    for line in data[1:]:
        points.append(Point(x = line[0], y = line[1]))

    return points


def main():
    #print('dd')
    points_list = []

    data = [line.strip().split('\t') for line in sys.stdin.readlines()]
    processed = []
    for line in data:
        x = [int(i) for i in line]
        processed.append(x)
    points = read_input(processed)
    coordinates = sorted(points)
    #coordinates = sorted([[point.x, point.y] for point in points],  key = lambda x: x[0])
    convexhull = convex_hull(coordinates)
    print('Convex Hull')
    for i in convexhull:
        print(tuple([i.x, i.y]))
    print('')
    print(f'Area of Convex Hull = {area_poly(convexhull)}')


if __name__ == '__main__':
    main()
