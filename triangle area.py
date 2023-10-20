class shape:
    def __init__(self,base,height):
        shape.base = base
        shape.height = height


class triangle(shape):
    def area(self):
        self.area = shape.base * shape.height/2
        return self.area
class rectangle(shape):
    
    def area(self):
        self.area = shape.base * shape.height
        return self.area
        
base1 = int(input("Input base of shape"))
height1 = int(input("input height of shape"))

tri = triangle(base1,height1)
rect = rectangle(base1,height1)
print("If it is a triangle it will have the area of " +str(tri.area()))
print("if it is a rectangle it will have the area of "+str(rect.area()))
