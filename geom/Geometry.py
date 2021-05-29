#  File: Geometry.py

#  Description: First creates shape objects, then finds various conditions, including if one shape
#  is inside or interesects another


#  Student Name: Nicholas Kasper

#  Student UT EID: Nak874


#  Course Name: CS 313E

#  Unique Number: 52240

#  Date Created: 02/11/2021

#  Date Last Modified: 2/11/2021

import math
import sys

class Point (object):
    # constructor with default values
    def __init__ (self, x = 0.0, y = 0.0, z = 0.0):
        self.x = x
        self.y = y
        self.z = z

    # create a string representation of a Point
    # returns a string of the form (x, y, z)
    def __str__ (self):
        return '(' + str(float(self.x)) + ', ' + str(float(self.y)) + ', ' + str(float(self.z)) + ')'


    # get distance to another Point object
    # other is a Point object
    # returns the distance as a floating point number
    def distance (self, other):
        return float(math.sqrt((self.x-other.x) **2 + (self.y - other.y)**2 + (self.z - other.z)**2))

    # test for equality between two points
    # other is a Point object
    # returns a Boolean
    def __eq__ (self, other):
        epsilon = 1.0e-6
        return ((abs(self.x - other.x) < epsilon) and (abs(self.y - other.y) < epsilon) and (abs(self.z - other.z) < epsilon))


class Sphere (object):
  # constructor with default values
    def __init__ (self, x = 0.0, y = 0.0, z = 0.0, radius = 1.0):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius

        self.center = Point(self.x, self.y, self.z)
            

        # define max and min of point coordinates 
        self.xmin = self.x - self.radius
        self.xmax = self.x + self.radius
        self.ymin = self.y - self.radius
        self.ymax = self.y + self.radius
        self.zmin = self.z - self.radius
        self.zmax = self.z + self.radius

    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__ (self):
        return 'Center:' +' (' + str(float(self.x)) +', ' +str(float(self.y)) +', ' + str(float(self.z)) +'), Radius: '+str(float(self.radius))

    # compute surface area of Sphere
    # returns a floating point number
    def area(self):
        self.surface_area = float(4 * math.pi * self.radius**2)
        return self.surface_area

    # compute volume of a Sphere
    # returns a floating point number
    def volume (self):
        self.volume = float(4/3 * math.pi * self.radius**3)
        return self.volume

    # determines if a Point is strictly inside the Sphere
    # p is Point object
    # returns a Boolean
    def is_inside_point (self, p):
        # check if radius is greater than distance
        return self.radius > self.center.distance(p)


    # determine if another Sphere is strictly inside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, other):
        return (other.radius + self.center.distance(other.center)) < self.radius

    def is_outside_sphere(self,other):
        return self.center.distance(other.center) > (self.radius + other.radius)

    # determine if a Cube is strictly inside this Sphere
    # determine if the eight corners of the Cube are strictly 
    # inside the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube (self, a_cube):
        '''
        Checks if the radius is larger than each vertex's distance from the center
        '''
        flag = True
        for vtx in a_cube.vertices:
            if self.radius > self.center.distance(vtx):
                flag = True
            else:
                flag = False
                break
        return flag

    def is_outside_cube(self, a_cube):
        '''
        Checks if x value is above or below the max values
        If one of these is true, we know a part of the other cube
        is outside

        '''
        flag = False
        # check is either x value is above or below max and min respectively
        if (self.xmax < a_cube.xmin) or (self.xmin > a_cube.xmax):
            flag = True
        elif (self.ymax < a_cube.ymin) or (self.ymin > a_cube.ymax):
            flag = True
        elif (self.zmax < a_cube.zmin) or (self.zmin > a_cube.zmax):
            flag = True
        return flag


    # determine if a Cylinder is strictly inside this Sphere
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cyl (self, a_cyl):
        '''
        First define the bounds for x,y,z dimensions
        If we are in the range, check if the distance from the bottom right and top left are less than the radius
        '''

        self.xranges = ((self.xmin < a_cyl.xmin < self.xmax) and (a_cyl.xmax < self.xmax))
        self.yranges = ((self.ymin < a_cyl.ymin < self.ymax) and (a_cyl.ymax < self.ymax))
        self.zranges = ((self.zmin < a_cyl.zmin < self.zmax) and (a_cyl.zmax < self.zmax))
        if self.xranges == True and self.yranges == True and self.zranges == True:
            flag = True
            if  (self.center.distance(a_cyl.bottom_down_center) < self.radius) and (self.center.distance(a_cyl.top_up_center) < self.radius):
                flag = True
            else:
                flag = False
        else:
            flag = False
        return flag
      

    # determine if another Sphere intersects this Sphere
    # other is a Sphere object
    # two spheres intersect if they are not strictly inside
    # or not strictly outside each other
    # returns a Boolean
    def does_intersect_sphere (self, other):
        '''
        Check if other sphere is both not inside or outside
        '''
        flag = False
        if self.is_inside_sphere(other) == False and self.is_outside_sphere(other) == False:
           flag = True
        return flag


    # determine if a Cube intersects this Sphere
    # the Cube and Sphere intersect if they are not
    # strictly inside or not strictly outside the other
    # a_cube is a Cube object
    # returns a Boolean
    def does_intersect_cube (self, a_cube):
        '''
        Check if a_cube is both not inside or outside
        '''
        return (self.is_inside_cube(a_cube) == False) and (self.is_outside_cube(a_cube) == False)

    # return the largest Cube object that is circumscribed
    # by this Sphere
    # all eight corners of the Cube are on the Sphere
    # returns a Cube object
    def circumscribe_cube (self):
        '''
        find where diagonal == radius and center is shared 
        '''
        self.side = self.radius*(2/math.sqrt(3))
        return Cube(self.x,self.y,self.z,self.side)

class Cube (object):
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__ (self, x = 0.0, y = 0.0, z = 0.0, side = 1.0):
        self.x = x
        self.y = y
        self.z = z
        self.side = side
        self.center = Point(self.x,self.y,self.z)

        #define maxes and mins for (x,y,z)
        self.length = side/2
        
        self.xmin = self.x - self.length
        self.xmax = self.x + self.length
        self.ymin = self.y - self.length
        self.ymax = self.y + self.length
        self.zmin = self.z - self.length
        self.zmax = self.z + self.length
        

      
        # create each individual vertex
        self.bottomupperright = Point(self.xmax, self.ymin, self.zmax)
        self.bottomupperleft = Point(self.xmin, self.ymin, self.zmax)
        self.bottombottomright = Point(self.xmax, self.ymin, self.zmin)
        self.bottombottomleft = Point(self.xmin, self.ymin, self.zmin)
        self.topupperright = Point(self.xmax, self.ymax, self.zmax)
        self.topupperleft = Point(self.xmin, self.ymax, self.zmax)
        self.topbottomright = Point(self.xmax, self.ymax, self.zmin)
        self.topbottomleft = Point(self.xmin, self.ymax, self.zmin)
        
        #create list of vertices as point objects to loop through in later operations
        self.vertices = [self.topbottomleft, self.topupperright, self.topupperleft, self.topbottomright
        ,self.bottomupperright, self.bottomupperleft, self.bottombottomright, self.bottombottomleft]




    # string representation of a Cube of the form: 
    # Center: (x, y, z), Side: value
    def __str__ (self):
        return 'Center: ('+str(float(self.x)) +', ' +str(float(self.y)) +', ' +str(float(self.z)) +'), Side: ' + str(float(self.side))

    # compute the total surface area of Cube (all 6 sides)
    # returns a floating point number
    def area (self):
        self.surface_area = float(6*self.side**2)
        return self.surface_area

    # compute volume of a Cube
    # returns a floating point number
    def volume (self):
        self.volume = float(self.side**3)
        return self.volume

    # determines if a Point is strictly inside this Cube
    # p is a point object
    # returns a Boolean
    def is_inside_point (self, p):
        #check if all 3 coordinates max and min bound the points coordinates
        return (self.xmin <= p.x <= self.xmax) and (self.ymin <= p.x <= self.ymax) and (self.zmin <= p.z <= self.zmax)


    # determine if a Sphere is strictly inside this Cube 
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, a_sphere):
        return self.length > self.center.distance(a_sphere.center) + a_sphere.radius



    # determine if another Cube is strictly inside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_inside_cube (self, other):
        validate_x = self.xmin < other.xmin and self.xmax > other.xmax
        validate_y = self.ymin < other.ymin and self.ymax > other.ymax 
        validate_z = self.zmin < other.zmin and self.zmax > other.zmax 
        return validate_x and validate_y and validate_z

    def is_outside_cube(self, other):
        validate_x = self.xmax < other.xmin or self.xmin > other.xmax
        validate_y = self.ymax < other.ymin or self.ymin > other.ymax 
        validate_z = self.zmax < other.zmin or self.zmin > other.zmax 
        return validate_x or validate_y or validate_z

    # determine if a Cylinder is strictly inside this Cube
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cylinder (self, a_cyl):
        '''
        Not needed: ran out of time :o

        '''
        pass

    # determine if another Cube intersects this Cube
    # two Cube objects intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cube object
    # returns a Boolean
    def does_intersect_cube (self, other):
        
        return self.is_inside_cube(other) == False and self.is_outside_cube(other) == False

    # determine the volume of intersection if this Cube 
    # intersects with another Cube
    # other is a Cube object
    # returns a floating point number
    def intersection_volume (self, other):
        '''
        First initialize x,y,z maxes and mins, checks is self and other intersect
        If they do intersect, defines and replaces maxes and mins based on overlaps
        Finally find total x,y,z dimension differences and return the volume as a float
        If they don't intersect, it's trivially 0 
        '''

        # define default min and max values for cube sides

        self.side_x_min = 0
        self.side_x_max = 0
        self.side_y_min = 0
        self.side_y_max = 0
        self.side_z_min = 0
        self.side_z_max = 0

        if self.does_intersect_cube(other):

            # finds and changes min is original xmin is more than other min
            if self.xmin > other.xmin:
                self.side_x_min = self.xmin
            elif other.xmin > self.xmin:
                self.side_x_min = other.xmin
            # finds and changes max is original xmax is less than other max
            if self.xmax < other.xmax:
                self.side_x_max = self.xmax
            elif other.xmax < self.xmax:
                self.side_x_max = other.xmax

            # finds and changes min is original ymin is more than other min
            if self.ymin > other.ymin:
                self.side_y_min = self.ymin
            elif other.ymin > self.ymin:
                self.side_y_min = other.ymin
            # finds and changes max is original ymax is less than other max
            if self.ymax < other.ymax:
                self.side_y_max = self.ymax
            elif other.ymax < self.ymax:
                self.side_y_max = other.ymax

            # finds and changes min is original zmin is more than other min
            if self.zmin > other.zmin:
                self.side_z_min = self.zmin
            elif other.zmin > self.zmin:
                self.side_z_min = other.zmin
            # finds and changes max is original zmax is less than other max
            if self.zmax < other.zmax:
                self.side_z_max = self.zmax
            elif other.zmax < self.zmax:
                self.side_z_max = other.zmax

            #find side lengths of intersection volume and then find volume
            self.side_x = self.side_x_max - self.side_x_min
            self.side_y = self.side_y_max - self.side_y_min
            self.side_z = self.side_z_max - self.side_z_min

            self.volume = float(self.side_x * self.side_y * self.side_z)
        else:
            self.volume = 0

        return self.volume
      

    # return the largest Sphere object that is inscribed
    # by this Cube
    # Sphere object is inside the Cube and the faces of the
    # Cube are tangential planes of the Sphere
    # returns a Sphere object
    def inscribe_sphere (self):
        '''
        makes a sphere7
        '''
        sphere = Sphere(self.x, self.y, self.z, self.length)
        return sphere

class Cylinder (object):
    # Cylinder is defined by its center (which is a Point object),
    # radius and height. The main axis of the Cylinder is along the
    # z-axis and height is measured along this axis
    def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
        self.x = x
        self.y = y
        self.z = z
        self.center = Point(self.x, self.y, self.z)
        self.radius = radius
        self.height = height
        self.xmin = self.x - self.radius
        self.xmax = self.x + self.radius
        self.ymin = self.y - self.radius
        self.ymax = self.y + self.radius

        self.length = height/2

        # define points on cylinder used later

        self.topcenter = Point(self.x, self.y, self.z + self.length)
        self.bottomcenter = Point(self.x, self.y, self.z - self.length)

        self.zmin = self.bottomcenter.z
        self.zmax = self.topcenter.z

        self.top_up_center = Point(self.x, self.y + self.length, self.topcenter.z)
        self.bottom_down_center = Point(self.x, self.y - self.length, self.bottomcenter.z)
        self.top_down_center = Point(self.x, self.y + self.length, self.topcenter.z)
        self.bottom_up_center = Point(self.x, self.y + self.length, self.bottomcenter.z)
    

        
       

    # returns a string representation of a Cylinder of the form: 
    # Center: (x, y, z), Radius: value, Height: value
    def __str__ (self):
        return 'Center: (' + str(float(self.x))+ ', ' + str(float(self.y)) + ', ' + str(float(self.z)) + '), Radius: ' + str(float(self.radius)) + ', Height: ' + str(float(self.height))
    
    # compute surface area of Cylinder
    # returns a floating point number
    def area (self):
        self.surface_area = (self.height + self.radius) * (2* (math.pi) * (self.radius))
        return float(self.surface_area)

    # compute volume of a Cylinder
    # returns a floating point number
    def volume (self):
        self.volume = math.pi * (self.radius**2) *self.height
        return float(self.volume)

    # determine if a Point is strictly inside this Cylinder
    # p is a Point object
    # returns a Boolean
    def is_inside_point (self, p):
        # verify all 3 conditions are met
        verify_x = self.xmin < p.x < self.xmax
        verify_y = self.ymin < p.y < self.ymax
        verify_z = self.zmin < p.z < self.zmax

        # if verified, grab point and return true if the distance from the center to p is less than the radianc
        if verify_x and verify_y and verify_z:
            self.alt_center = Point(self.x, self.y, p.z)
            return self.alt_center.distance(p) < self.radius
        else:
            return False

    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere (self, a_sphere):
        self.xrange = ((a_sphere.xmax < self.xmax) and (self.xmin < a_sphere.xmin < self.xmax))
        self.yrange = ((a_sphere.ymax < self.ymax) and (self.xmin < a_sphere.ymin < self.ymax))
        self.zrange = ((a_sphere.zmax < self.zmax) and (self.xmin < a_sphere.zmin < self.zmax))
        if self.xrange and self.yrange and self.zrange:
            self.alt_center = Point(self.x, self.y, a_sphere.z)
            if self.alt_center.distance(a_sphere.center) + a_sphere.radius < self.radius:
                return True
            else:
                return False
        else:
            return False

    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are inside
    # the Cylinder
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube (self, a_cube):
        self.xranges = ((self.xmin < a_cube.xmin < self.xmax) and (a_cube.xmax < self.xmax))
        self.yranges = ((self.ymin < a_cube.ymin < self.ymax) and (a_cube.ymax < self.ymax))
        self.zranges = ((self.zmin < a_cube.zmin < self.zmax) and (a_cube.zmax < self.zmax))
        if  self.xranges == True and self.yranges == True and self.zranges == True:
            flag = True
            for vertex in a_cube.vertices:
                self.centered = Point(self.x, self.y, vertex.z)
                if self.centered.distance(vertex) < self.radius:
                    flag = True
                else:
                    flag = False
                    break
        else:
            flag = False
        return flag   

    # determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object
    # returns a Boolean
    def is_inside_cylinder (self, other):
        self.xranges = ((self.xmin < other.xmin < self.xmax) and (other.xmax < self.xmax))
        self.yranges = ((self.ymin < other.ymin < self.ymax) and (other.ymax < self.ymax))
        self.zranges = ((self.zmin < other.zmin < self.zmax) and (other.zmax < self.zmax))
        if  self.xranges == True and self.yranges == True and self.zranges == True:
            flag = True
            self.centered = Point(self.x, self.y, other.z)
            if self.centered.distance(other.center) + other.radius < self.radius:
                return True
            else: 
                return False
        else:
            return False


    # determine if another Cylinder intersects this Cylinder
    # two Cylinder object intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cylinder object
    # returns a Boolean
    def is_outside_cylinder(self,other):
        '''

        '''
        flag = True
        self.xrange = (other.xmax < self.xmin) or (other.xmin > self.xmax)
        self.yrange = (other.ymax < self.ymin) or (other.ymin > self.ymax)
        self.zrange = (other.zmax < self.zmin) or (other.zmin > self.zmax)
        if  self.xrange or self.yrange or self.zrange:
            flag = True
        else:
            if self.zmin< other.bottomcenter.z < self.zmax:
                centered = Point(self.x, self.y, other.bottomcenter.z)
                if centered.distance(other.bottomcenter) > self.radius + other.radius:
                    flag = True
                else:
                    flag = False
            elif self.zmin < other.topcenter.z < self.zmax:
                centered = Point(self.x, self.y, other.topcenter.z)
                if centered.distance(other.topcenter) > self.radius + other.radius:
                    flag = True
                else:
                    flag = False
        return flag

    def does_intersect_cylinder (self, other):
        '''
        Returns true if the two cylinders are neither inside or outside of eachother (intersection)
        '''
        if self.is_outside_cylinder(other) == False and self.is_inside_cylinder(other) == False:
            return True
        else:
            return False


def strip_data():
    '''
    Used for data input.
    Reads each line then strips the numbers, turns them into numbers, then appends tuples to final list
    Returns the final list
    '''
    values = []
    for line in sys.stdin.readlines():
        coords_tuple = ()
        line = line.strip()
        numbers = line.split('             ')[0].split(' ')
        
        try:
            numbers = [float(x) for x in numbers]
        except:
            pass
        
        for num in numbers:
            coords_tuple = coords_tuple + (num,)
        values.append(coords_tuple)

    return values


    

def main():
    # read data from standard input
    
    data = strip_data()
    
    # read the coordinates of the first Point p
    P_coordinates = data[0]
    # create a Point object 
    Point1 = Point(P_coordinates[0], P_coordinates[1], P_coordinates[2])

    # create point object for origin
    origin = Point()
    # read the coordinates of the second Point q
    Q_coordinates = data[1]
    # create a Point object 
    Point2 = Point(Q_coordinates[0], Q_coordinates[1], Q_coordinates[2])

    # read the coordinates of the center and radius of sphereA
    sphereA_coordinates = data[2]
    # create a Sphere object 
    sphereA = Sphere(sphereA_coordinates[0], sphereA_coordinates[1], sphereA_coordinates[2], sphereA_coordinates[3])
   
    # read the coordinates of the center and radius of sphereB
    sphereB_coordinates = data[3]
    # create a Sphere object
    sphereB = Sphere(sphereB_coordinates[0], sphereB_coordinates[1], sphereB_coordinates[2], sphereB_coordinates[3])
      
    # read the coordinates of the center and side of cubeA
    cubeA_coordinates = data[4]
    cubeA = Cube(cubeA_coordinates[0], cubeA_coordinates[1], cubeA_coordinates[2], cubeA_coordinates[3])
    # create a Cube object 

    # read the coordinates of the center and side of cubeB
    cubeB_coordinates = data[5]
    # create a Cube object 
    cubeB = Cube(cubeB_coordinates[0], cubeB_coordinates[1], cubeB_coordinates[2], cubeB_coordinates[3])
 
    # read the coordinates of the center, radius and height of cylA
    cylinderA_coordinates = data[6]
    # create a Cylinder object 
    cylA = Cylinder(cylinderA_coordinates[0], cylinderA_coordinates[1], cylinderA_coordinates[2], cylinderA_coordinates[3], cylinderA_coordinates[4])

    # read the coordinates of the center, radius and height of cylB
    cylinderB_coordinates = data[7]
    cylB = Cylinder(cylinderB_coordinates[0], cylinderB_coordinates[1], cylinderB_coordinates[2], cylinderB_coordinates[3], cylinderB_coordinates[4])

    #reading data and creating objects done. now if/else for print statements

    # print if the distance of p from the origin is greater 
    # than the distance of q from the origin
    if Point1.distance(origin) > Point2.distance(origin):
        print("Distance of Point p from the origin is greater than ", end = '')
        print("the distance of Point q from the origin")
    else:
        print("Distance of Point p from the origin is not greater than ", end = '')
        print("the distance of Point q from the origin")


  # print if Point p is inside sphereA
    if sphereA.is_inside_point(Point1) == True:
        print('Point p is inside sphereA')
    else:
        print('Point p is not inside sphereA')

  # print if sphereB is inside sphereA
    if sphereA.is_inside_sphere(sphereB) == True:
        print('sphereB is inside sphereA')
    else:
        print('sphereB is not inside sphereA')
  # print if cubeA is inside sphereA
    if sphereA.is_inside_cube(cubeA) == True:
        print('cubeA is inside sphereA')
    else:
        print('cubeA is not inside sphereA')
  # print if cylA is inside sphereA
    if sphereA.is_inside_cyl(cylA) == True:
        print('cylA is inside sphereA')
    else:
        print('cylA is not inside sphereA')

  # print if sphereA intersects with sphereB
    if sphereB.does_intersect_sphere(sphereA) == True:
        print('sphereA does intersect sphereB')
    else:
        print('sphereA does not intersect sphereB')
  # print if cubeB intersects with sphereB
    if sphereB.does_intersect_cube(cubeB) == True:
        print('cubeB does intersect sphereB')
    else:
        print('cubeB does not intersect sphereB')    
  # print if the volume of the largest Cube that is circumscribed 
  # by sphereA is greater than the volume of cylA
    if sphereA.circumscribe_cube().volume() > cylA.volume():
        print("Volume of the largest Cube that is circumscribed by sphereA is ", end = '')
        print("greater than the volume of cylA")
    else:
        print("Volume of the largest Cube that is circumscribed by sphereA is ", end = '')
        print("not greater than the volume of cylA")


  # print if Point p is inside cubeA
    if cubeA.is_inside_point(Point1) == True:
        print('Point p is inside cubeA')
    else:
        print('Point p is not inside cubeA')
  # print if sphereA is inside cubeA
    if cubeA.is_inside_sphere(sphereA) == True:
        print('sphereA is inside cubeA')
    else:
        print('sphereA is not inside cubeA')
  # print if cubeB is inside cubeA
    if cubeA.is_inside_cube(cubeB) == True:
        print('cubeB is inside cubeA')
    else:
        print('cubeB is not inside cubeA')
  # print if cylA is inside cubeA
    if cubeA.is_inside_cylinder(cylA) == True:
        print('cylA is inside cubeA')
    else:
        print('cylA is not inside cubeA')
  # print if cubeA intersects with cubeB
    if cubeA.does_intersect_cube(cubeB) == True:
        print('cubeA does intersect cubeB')
    else:
        print('cubeA does not intersect cubeB')
  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA
    if cubeA.intersection_volume(cubeB) > sphereA.volume():
        print("Intersection volume of cubeA and cubeB is ", end = '')
        print("greater than the volume of sphereA")
    else:
        print("Intersection volume of cubeA and cubeB is ", end = '')
        print("not greater than the volume of sphereA")

  # print if the surface area of the largest Sphere object inscribed 
  # by cubeA is greater than the surface area of cylA
    if cubeA.inscribe_sphere().area() > cylA.area():
        print("Surface area of the largest Sphere object inscribed by cubeA ", end = '')
        print("is greater than the surface area of cylA")
    else:
        print("Surface area of the largest Sphere object inscribed by cubeA ", end = '')
        print("is not greater than the surface area of cylA")
        
  # print if Point p is inside cylA
    if cylA.is_inside_point(Point1) == True: 
        print('Point p is inside cylA')
    else:
        print('Point p is not inside cylA')
  # print if sphereA is inside cylA
    if cylA.is_inside_sphere(sphereA) == True:
        print('sphereA is inside cylA')
    else:
        print('sphereA is not inside cylA')
  # print if cubeA is inside cylA
    if cylA.is_inside_cube(cubeA) == True:
        print('cubeA is inside cylA')
    else:
        print('cubeA is not inside cylA')
  # print if cylB is inside cylA
    if cylA.is_inside_cylinder(cylB) == True:
        print('cylB is inside cylA')
    else:
        print('cylB is not inside cylA')
  # print if cylB intersects with cylA
    if cylA.does_intersect_cylinder(cylB) == True: 
        print('cylB does intersect cylA')
    else:
        print('cylB does not intersect cylA')


if __name__ == "__main__": main()