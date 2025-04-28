class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):

        return self.width * self.height

    def perimeter(self):

        return 2 * (self.width + self.height)


rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)
rect3 = Rectangle(8, 2)

print(f"Прямоугольник 1: Площадь = {rect1.area()}, Периметр = {rect1.perimeter()}")
print(f"Прямоугольник 2: Площадь = {rect2.area()}, Периметр = {rect2.perimeter()}")
print(f"Прямоугольник 3: Площадь = {rect3.area()}, Периметр = {rect3.perimeter()}")