from graphics import *

rec = []


def main():
    win = GraphWin()
    shape = Rectangle(Point(0, 0), Point(20, 20))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        rec.append(Rectangle(Point(dx, dy), Point(dx + 20, dy + 20)))
        rec[i].setOutline("red")
        rec[i].setFill("red")
        rec[i].draw(win)
    Text(Point(50, 20), "Click again to quit.").draw(win)
    p = win.getMouse()
    if p:
        win.close()


main()
