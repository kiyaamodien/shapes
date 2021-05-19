import math


class Shapes:
    def __init__(self, name, side):
        self.name=name
        self.side=side
    def Area(self):
        print("I am a  :" + self.name + "\n" +
              "I have " + self.side + "sides")
object_shapes=Shapes("shape", "so many")
object_shapes.Area()

class Rectangle(Shapes):
    def __init__(self, lenl, wid1):
        self.length=lenl
        self.width=wid1
    def Area(self):
        result= self.length * self.width
        return result
obj_book=Rectangle(10, 7)
obj_screen=Rectangle(5,7)
print("The area of a book is" + str(obj_book.Area()))
print("The area of a screen is" + str(obj_screen.Area()))


class Circle(Shapes):
    def __init__(self, radius):
        self.radius=radius

    def Area(self):
        result=self.radius**2 * math.pi
        return result


obj_dvd=Circle(8)
print("The area of dvd is: " + str(obj_dvd.Area()))

class Triangle(Shapes):
    def __init__(self, base, height):
        self.base=base
        self.height=height

    def Area(self):
        result=self.base * self.height
        return result
obj_tri=Triangle(6, 8)
print("The area of a sandwitch is:" + str (obj_tri.Area()))

