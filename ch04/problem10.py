from graphics import *
import math


def main():
    win = GraphWin()
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()
    shape = Polygon(Point(p1.getX(), p1.getY()), Point(p2.getX(), p2.getY()), Point(p3.getX(), p3.getY()))
    shape.draw(win)
    adx = abs(p1.getX() - p2.getX())
    ady = abs(p1.getY() - p2.getY())
    bdx = abs(p2.getX() - p3.getX())
    bdy = abs(p2.getY() - p3.getY())
    cdx = abs(p3.getX() - p1.getX())
    cdy = abs(p3.getY() - p1.getY())
    a = math.sqrt((adx * adx) + (ady * ady))
    b = math.sqrt((bdx * bdx) + (bdy * bdy))
    c = math.sqrt((cdx * cdx) + (cdy * cdy))

    s = (a + b + c) / 2
    area = math.sqrt(s*(s - a)*(s - b)*(s - c))
    print("area : ", area)

    win.getMouse()
    win.close()


main()
