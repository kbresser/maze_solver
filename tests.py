import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_break_entrance_and_exit(self):
        # Create a test maze (perhaps with a small size like 3x3)
        maze = Maze(0, 0, 3, 3, 10, 10)
        
        # Verify the entrance wall is removed
        self.assertFalse(maze._cells[0][0].has_top_wall)
        
        # Verify the exit wall is removed
        self.assertFalse(maze._cells[2][2].has_bottom_wall)

    def test_reset_cells_visited(self):
        # Create a test maze
        maze = Maze(0, 0, 3, 3, 10, 10)
        
        # Mark some cells as visited
        maze._cells[0][0].visited = True
        maze._cells[1][1].visited = True
        
        # Reset the visited status
        maze._reset_cells_visited()
        
        # Check that all cells are marked as not visited
        for row in maze._cells:
            for cell in row:
                self.assertFalse(cell.visited)

if __name__ == "__main__":
     unittest.main()