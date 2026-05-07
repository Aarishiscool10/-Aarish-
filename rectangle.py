class Rectangle():
    def __init__(self, l, w):
        self.height = l
        self.width = w

    def rectangle_area(self):
            return self.width*self.height
    

newRectangle = Rectangle(12,10)
print ("Dimensions of Rectangle - Width %d :  Height %d : " % (newRectangle.height, newRectangle.width))
print("Area of Rectangle :", newRectangle.rectangle_area())