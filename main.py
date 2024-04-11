from graphics import Window, Point, Cell


def main():
    win = Window(800, 600)
    point1 = Point(20, 40)
    point2 = Point(50, 70)
    cell = Cell(win, has_left_wall=False)
    cell.draw(point1, point2)
    win.wait_for_close()


main()
