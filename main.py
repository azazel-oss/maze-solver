from graphics import Window
from maze import Maze


def main():
    win = Window(1500, 1500)

    # a = Cell(win)
    # a.has_bottom_wall = False
    # a.draw(300, 400, 400, 500)
    #
    # b = Cell(win)
    # b.has_top_wall = False
    # b.draw(300, 500, 400, 600)
    #
    # c = Cell(win)
    # c.has_right_wall = False
    # c.draw(50, 50, 100, 100)
    #
    # d = Cell(win)
    # d.has_left_wall = False
    # d.draw(100, 50, 150, 100)
    #
    # c.draw_move(d)
    # a.draw_move(b, True)

    Maze(50, 50, 10, 10, 100, 100, win)
    win.wait_for_close()


main()
