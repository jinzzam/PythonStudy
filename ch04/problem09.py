from graphics import *


def main():
    win = GraphWin()
    p1 = win.getMouse()
    p2 = win.getMouse()
    shape = Rectangle(Point(p1.getX(), p1.getY()), Point(p2.getX(), p2.getY()))
    shape.draw(win)
    x = abs(p1.getX() - p2.getX())
    y = abs(p1.getX() - p2.getY())
    print("area : ", x * y)
    print("length : ", 2 * (x + y))

    win.getMouse()
    win.close()


main()
