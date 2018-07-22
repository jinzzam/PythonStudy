from graphics import *


def main():
    win = GraphWin()
    face = Oval(Point(50, 50), Point(180, 180))
    face.draw(win)
    lefteye = Circle(Point(90, 90), 15)
    lefteye.draw(win)
    leye = Circle(Point(90, 90), 7)
    leye.setFill("black")
    leye.draw(win)
    righteye = Circle(Point(140, 90), 15)
    righteye.draw(win)
    reye = Circle(Point(140, 90), 7)
    reye.setFill("black")
    reye.draw(win)
    nose = Polygon(Point(115, 110), Point(105, 140), Point(125, 140))
    nose.draw(win)
    mouth = Polygon(Point(90, 150), Point(140, 150), Point(130, 155), Point(120, 160), Point(110, 160), Point(100, 155))
    mouth.setFill("red")
    mouth.draw(win)
    p = win.getMouse()
    if p:
        win.close()


main()
