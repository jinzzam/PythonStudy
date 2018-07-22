from graphics import *
import math


def main():
    r = float(input("r : "))
    y = float(input("y : "))

    win = GraphWin()
    win.setCoords(-10, -10, 10, 10)

    circle = Circle(Point(0, 0), r)
    circle.draw(win)
    line = Line(Point(-10, y), Point(10, y))
    line.draw(win)

    x = math.sqrt((r * r) - (y * y))
    print("x : ", -x, x)

    circle2 = Circle(Point(x, y), 0.25)
    circle2.setOutline("red")
    circle2.setFill("red")
    circle2.draw(win)

    circle3 = circle2.clone()
    circle3.move(-2 * x, 0)
    circle3.draw(win)

    win.getMouse()
    win.close()


main()
