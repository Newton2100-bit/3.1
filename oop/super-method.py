class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f'I am shape of the color {self.color}')

class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f'My area is {self.radius * self.radius * 3.14}')


class Triangle(Shape):
    def __init__(self,color,is_filled,width,height):
        super().__init__(color,is_filled)
        self.width = width
        self.height = height


    def describe(self):
        super().describe()
        print(f'Mya area is {0.5 * self.width * self.height}')


class Square(Shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width = width


    def describe(self):
        super().describe()
        print(f'My area is {self.width * self.width}')



triangle = Triangle('red',True,12,24)
triangle.describe()
print()

circle = Circle('purple',True,21)
circle.describe()
print()

square = Square('red',True,12)
square.describe()


