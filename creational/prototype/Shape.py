from abc import abstractmethod, ABCMeta


class Shape(metaclass=ABCMeta):

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def constructor(self, shape):
        self.x = shape.x
        self.y = shape.y
        self.color = shape.color

    @abstractmethod
    def clone(self) -> None:
        pass
