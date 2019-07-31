import math


class Shape:
    def __init__(self,
                 shape_type="circle",
                 color="red",
                 square_formula=lambda x: (x[0] ** 2) * math.pi,
                 sizes: tuple = (1,)):
        self.shape_type = shape_type
        self.color = color
        self.square_formula = square_formula
        self.sizes = sizes

    def square(self):
        return self.square_formula(self.sizes)

    def __str__(self) -> str:
        return "Shape {}, color {}, sizes {}".format(self.shape_type, self.color, self.sizes)


def rectangle_square(sizes: tuple):
    return sizes[0] * sizes[1]


blue_circle = Shape("circle", "blue")
print(blue_circle)
print(blue_circle.square())

red_square = Shape("square", "red", lambda x: x[0] ** 2, (2,))
print(red_square)
print(red_square.square())

white_rectangle = Shape("rectangle", "white", rectangle_square, (3, 4))
pink_rectangle = Shape("rectangle", "pink", rectangle_square, (20, 7))
print(white_rectangle)
print(white_rectangle.square())
print(pink_rectangle)
print(pink_rectangle.square())
