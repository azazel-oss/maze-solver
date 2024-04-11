from graphics import Window, Point, Cell


def main():
    win = Window(800, 600)
    point1 = Point(20, 70)
    point2 = Point(50, 40)
    cell = Cell(win, has_right_wall=False)
    next_cell = Cell(win, has_left_wall=False)
    cell.draw(point1, point2)
    next_cell.draw(Point(50, 70), Point(80, 40))
    cell.draw_move(next_cell, False)
    win.wait_for_close()


main()
