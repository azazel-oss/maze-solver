from typing import List
import time
import random
from cell import Cell
from graphics import Window


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows: int,
        num_cols: int,
        cell_size_x,
        cell_size_y,
        win: Window,
        seed: int | None = None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells: List[List[Cell]] = []
        self._create_cells()
        self._break_entrance_and_exit()
        if seed:
            random.seed(seed)
        self._break_walls_r(num_rows - 1, num_cols - 1)
        self._reset_cells_visited()

    def _create_cells(self):
        for _ in range(self.num_rows):
            cells = []
            for _ in range(self.num_cols):
                cells.append(Cell(self.win))
            self._cells.append(cells)

        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = self.x1 + j * self.cell_size_x
        x2 = x1 + self.cell_size_x

        y1 = self.y1 + i * self.cell_size_y
        y2 = y1 + self.cell_size_y

        cell: Cell = self._cells[i][j]
        cell.draw(x1, y1, x2, y2)
        self._animate()

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        self._draw_cell(0, 0)
        exit_cell = self._cells[self.num_rows - 1][self.num_cols - 1]
        exit_cell.has_bottom_wall = False
        self._draw_cell(self.num_rows - 1, self.num_cols - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            to_visit = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            choices = []
            for node in to_visit:
                if (0 <= node[0] < self.num_rows) and (0 <= node[1] < self.num_cols):
                    if not self._cells[node[0]][node[1]]._visited:
                        choices.append((node[0], node[1]))

            if len(choices) == 0:
                self._draw_cell(i, j)
                return
            next_choice = random.choice(choices)

            next_choice_cell: Cell = self._cells[next_choice[0]][next_choice[1]]
            current_cell: Cell = self._cells[i][j]
            if next_choice[0] == i:
                # same row
                if next_choice[1] > j:
                    # ahead
                    current_cell.has_right_wall = False
                    next_choice_cell.has_left_wall = False
                else:
                    # behind
                    current_cell.has_left_wall = False
                    next_choice_cell.has_right_wall = False
            else:
                # same column
                if next_choice[0] > i:
                    # above
                    current_cell.has_bottom_wall = False
                    next_choice_cell.has_top_wall = False
                else:
                    # below
                    current_cell.has_top_wall = False
                    next_choice_cell.has_bottom_wall = False

            self._draw_cell(i, j)
            self._draw_cell(next_choice[0], next_choice[1])
            self._break_walls_r(next_choice[0], next_choice[1])

    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells[i][j]._visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        current_cell: Cell = self._cells[i][j]
        current_cell._visited = True
        if i == self.num_rows - 1 and j == self.num_cols - 1:
            return True
        to_visit = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        for t in range(len(to_visit)):
            item = to_visit[t]
            if (0 <= item[0] < self.num_rows) and (0 <= item[1] < self.num_cols):
                destination_cell = self._cells[item[0]][item[1]]
                if not destination_cell._visited:
                    if (
                        (t == 0 and not current_cell.has_bottom_wall)
                        or (t == 1 and not current_cell.has_top_wall)
                        or (t == 2 and not current_cell.has_right_wall)
                        or (t == 3 and not current_cell.has_left_wall)
                    ):
                        current_cell.draw_move(destination_cell)
                        value = self._solve_r(item[0], item[1])
                        if value:
                            return value
                        else:
                            current_cell.draw_move(destination_cell, True)

        return False
