from graphics import Line, Point, Window


class Cell:
    def __init__(self, win: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self._visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        draw_color = "white"
        line = Line(Point(x1, y1), Point(x1, y2))
        self._win.draw_line(line, draw_color)
        line = Line(Point(x1, y1), Point(x2, y1))
        self._win.draw_line(line, draw_color)
        line = Line(Point(x2, y1), Point(x2, y2))
        self._win.draw_line(line, draw_color)
        line = Line(Point(x1, y2), Point(x2, y2))
        self._win.draw_line(line, draw_color)
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

    def draw_move(self, to_cell: "Cell", undo=False):
        draw_color = "red" if not undo else "gray"
        if not (self._x1 and self._x2 and self._y1 and self._y2):
            return
        if not (to_cell._x1 and to_cell._x2 and to_cell._y1 and to_cell._y2):
            return
        line = Line(
            Point(((self._x1 + self._x2) / 2), ((self._y1 + self._y2) / 2)),
            Point((to_cell._x1 + to_cell._x2) / 2, ((to_cell._y1 + to_cell._y2) / 2)),
        )
        self._win.draw_line(line, draw_color)
