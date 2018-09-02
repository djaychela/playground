class Rectangle:

    def __init__(self,x1 ,y1 ,x2 ,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def width(self):
        return self.x2 - self.x1

    def height(self):
        return self.y2 - self.y1

    def area(self):
        return self.width() * self.height()

    def circumference(self):
        return 2 * self.width() + 2 * self.height()


class Square(Rectangle):

    def __init__(self, x1, y1, size):
        super().__init__(x1, y1, x1+size, y1+size)



rect = Rectangle(1,1,51,101)
print(rect.width())
print(rect.height())
print(rect.area())
print(rect.circumference())

square = Square(1,1,50)
print(square.width())
print(square.height())
print(square.area())
print(square.circumference())