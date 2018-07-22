from graphics import *
import math


def main():
    win = GraphWin()
    p1 = win.getMouse()
    p2 = win.getMouse()
    line = Line(Point(p1.getX(), p1.getY()), Point(p2.getX(), p2.getY()))
    line.draw(win)
    m = Point((p1.getX() + p2.getX()) / 2, (p1.getY() + p2.getY()) / 2)
    m.setFill("magenta")
    m.draw(win)
    dx = abs(p1.getX() - p2.getX())
    dy = abs(p1.getY() - p2.getY())
    gradient = dy / dx
    print("gradient : ", gradient)
    length = math.sqrt((dx * dx) + (dy * dy))
    print("length : ", length)
    win.getMouse()
    win.close()


main()
