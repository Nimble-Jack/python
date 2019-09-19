#%%
import math

class Line:

    def __init__(self,coor1,coor2):
        self.coor1 = (coor1)
        self.coor2 = (coor2)

    def distance(self):
        x_diff = self.coor2[0]-self.coor1[0]
        y_diff = self.coor2[1]-self.coor1[1]
        distance = math.sqrt(x_diff**2+y_diff**2)
        return distance

    def slope(self):
        x_diff = self.coor2[0]-self.coor1[0]
        y_diff = self.coor2[1]-self.coor1[1]
        m = y_diff/x_diff
        return m
#%%
l = Line((3,2),(8,10))
l.distance()

#%%
l.slope()

#%%
class Cylinder:

    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        volume = Cylinder.pi*self.height*self.radius**2
        return volume

    def surface_area(self):
        area = 2*Cylinder.pi*self.radius*self.height + 2*Cylinder.pi*self.radius**2
        return area

#%%
c = Cylinder(2,3)
c.volume()

#%%
c.surface_area()
