from graphics import *


def main():
    win = GraphWin()
    r = 50
    shape1 = Circle(Point(50, 50), r)
    shape1.setFill("white")
    shape1.draw(win)
    shape2 = Circle(Point(50, 50), r / 2)
    shape2.setFill("black")
    shape2.draw(win)
    shape3 = Circle(Point(50, 50), r / 4)
    shape3.setFill("blue")
    shape3.draw(win)
    shape4 = Circle(Point(50, 50), r / 8)
    shape4.setFill("red")
    shape4.draw(win)
    shape5 = Circle(Point(50, 50), r / 16)
    shape5.setFill("yellow")
    shape5.draw(win)
    p = win.getMouse()
    if p:
        win.close()
main()

