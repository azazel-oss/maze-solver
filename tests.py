import unittest
from maze import Maze
from graphics import Window


class Tests(unittest.TestCase):
    def test_maze_rows(self):
        num_cols = 12
        num_rows = 10
        win = Window(1500, 1500)
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win, None)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_entrance_exit_break(self):
        num_cols = 6
        num_rows = 4
        win = Window(1500, 1500)
        m1 = Maze(0, 0, num_rows, num_cols, 100, 100, win, None)
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[num_rows - 1][num_cols - 1].has_bottom_wall, False)


if __name__ == "__main__":
    unittest.main()
