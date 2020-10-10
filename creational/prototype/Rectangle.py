from Shape import Shape


class Rectangle(Shape):

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def clone(self):
        return Rectangle(self.x, self.y, self.color)


rectangle = Rectangle(2, 3, 'Red')

copy = rectangle.clone()

print(rectangle)
print(copy)
