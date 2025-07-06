import math

# Базовый класс
class Shape:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Это фигура: {self.name}")

# Производный класс
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Круг")
        self.radius = radius

    def info(self):
        print(f"Это круг с радиусом {self.radius}")

    def area(self):
        return math.pi * self.radius ** 2

# Тестовая программа
if __name__ == "__main__":
    shape = Shape("Фигура")
    shape.info()

    circle = Circle(5)
    circle.info()
    print(f"Площадь круга: {circle.area():.2f}")
