from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, start_point: Point, end_point: Point) -> None:
        self.__start_point = start_point
        self.__end_point = end_point

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.__start_point.x,
            self.__start_point.y,
            self.__end_point.x,
            self.__end_point.y,
            fill=fill_color,
            width=2,
        )
        canvas.pack(fill=BOTH, expand=1)


class Window:
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title("Maze")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()

    def close(self):
        self.__is_running = False

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.__canvas, fill_color)


class Cell:
    def __init__(
        self,
        window: Window,
        has_left_wall=True,
        has_right_wall=True,
        has_top_wall=True,
        has_bottom_wall=True,
    ) -> None:
        self._win = window
        self._x = None
        self._y = None
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

    def draw(self, t_l_point: Point, b_r_point: Point):
        t_r_point = Point(b_r_point.x, t_l_point.y)
        b_l_point = Point(t_l_point.x, b_r_point.y)
        self._x = (t_l_point.x + t_r_point.x) // 2
        self._y = (t_l_point.y + b_l_point.y) // 2
        if self.has_top_wall:
            self._win.draw_line(Line(t_l_point, t_r_point), "black")
        if self.has_right_wall:
            self._win.draw_line(Line(t_r_point, b_r_point), "black")
        if self.has_bottom_wall:
            self._win.draw_line(Line(b_l_point, b_r_point), "black")
        if self.has_left_wall:
            self._win.draw_line(Line(t_l_point, b_l_point), "black")

    def draw_move(self, to_cell, undo=False):
        line = Line(Point(self._x, self._y), Point(to_cell._x, to_cell._y))
        fill_color = "gray" if undo else "red"
        self._win.draw_line(line, fill_color)
