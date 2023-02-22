import pdb
class Rectangle:
    #pdb.set_trace()
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Create two Rectangle objects
rect1 = Rectangle(10,5)
rect2 = Rectangle(3, 7)

# Print the areas of the two rectangles
print("Area of rect1:", rect1.area())
print("Area of rect2:", rect2.area())
