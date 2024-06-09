from typing import List
import time
from cell import Cell
from graphics import Window


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win: Window,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    def _create_cells(self):
        self._cells: List[List[Cell]] = []
        for _ in range(self.num_rows):
            cells = []
            for _ in range(self.num_cols):
                cells.append(Cell(self.win))
            self._cells.append(cells)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = self.x1 + i * self.cell_size_x
        x2 = x1 + self.cell_size_x

        y1 = self.y1 + j * self.cell_size_y
        y2 = y1 + self.cell_size_y

        cell: Cell = self._cells[i][j]
        cell.draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
