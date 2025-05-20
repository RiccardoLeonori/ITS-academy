from circle import Circle
from rectangle import Rectangle


if __name__ == '__main__':
    c = Circle(20)
    print(f"Area e perimetro del cerchio con raggio = {c.raggio()}: ({c.area()}, {c.perimeter()})")

    r = Rectangle(10, 30)
    print(f"Area e perimetro del rettangolo con base = {r.base()} ed altezza = {r.altezza()}: ({r.area()}, {r.perimeter()})")