class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def division(self):
        if self.height == 0:
            print("Error: Width or height cannot be zero.")
        else :
            return self.width / self.height

