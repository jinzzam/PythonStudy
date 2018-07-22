from graphics import *


def main():
    win = GraphWin("Home Sweet Home", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    shape = Rectangle(Point(p1.getX(), p1.getY()), Point(p2.getX(), p2.getY()))
    shape.draw(win)

    p3 = win.getMouse()
    dx = abs(p1.getX() - p2.getX())
    door = dx / 5
    doortemp = door / 2
    doorupline = Line(Point(p3.getX() - doortemp, p3.getY()), Point(p3.getX() + doortemp, p3.getY()))
    doorleftline = Line(Point(p3.getX() - doortemp, p3.getY()), Point(p3.getX() - doortemp, p1.getY()))
    doorrightline = Line(Point(p3.getX() + doortemp, p3.getY()), Point(p3.getX() + doortemp, p1.getY()))
    doorupline.draw(win)
    doorleftline.draw(win)
    doorrightline.draw(win)

    p4 = win.getMouse()
    window = door / 2
    windowtemp = window / 2
    windowshape = Rectangle(Point(p4.getX() - windowtemp, p4.getY() - windowtemp),
                            Point(p4.getX() + windowtemp, p4.getY() + windowtemp))
    windowshape.draw(win)

    p5 = win.getMouse()
    roofshape = Polygon(Point(p5.getX(), p5.getY()), Point(p1.getX(), p2.getY()), Point(p2.getX(), p2.getY()))
    roofshape.draw(win)

    win.getMouse()
    win.close()


main()
