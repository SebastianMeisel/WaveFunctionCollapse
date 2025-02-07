import unittest
import pygame
from WaveFunctionCollaps.grid import Grid
from WaveFunctionCollaps.tile import Tile
from WaveFunctionCollaps.canvas import Canvas

class TestGrid(unittest.TestCase):
    def setUp(self):
        self.width = 20
        self.Grid = Grid(self.width)
        self.size = (800,800)
        self.Canvas = Canvas(self.size)
        self.color= (245, 185, 39, 255)

    def test_Grid_exists(self):
        "Test, the Grid class exists."
        self.assertIsNotNone(self.Grid, "Grid does not exist.")
        self.assertIsInstance(self.Grid, Grid, "Grid is not a class.")

    def test_Grid_dimensions(self):
        "Test the Grid class is initialized with the expected values"
        self.assertEqual(self.Grid.width, self.Grid.height,
                         "Grid.height != Grid.width.")
        self.assertEqual(self.Grid.width, 20, "Grid.width != 20.")
        self.assertGreater(self.Grid.width, 0, "Grid has zero width.")
        self.assertGreater(self.Grid.height, 0, "Grid has zero height.")
        self.assertEqual(len(self.Grid.grid), self.Grid.height, "Array of grid's length != height.")
        self.assertEqual(len(self.Grid.grid[0]), self.Grid.width, "Array of rows' length != width.")


    def test_Grid_containsTiles(self):
        "Test, the Grid contains Tiles."
        for row in range(self.Grid.height):
            for col in range (self.Grid.width):
                self.assertIsInstance(self.Grid.grid[row][col], Tile, f"Grid[{row}][{col}] is not an Instance of Tile")

    def test_drawGrid(self):
        """Test that Grid has a draw method,
           that draws the Grid on the Canvas.
        """
        self.Canvas.draw()
        self.assertTrue(self.Grid.draw(self.Canvas, self.color))
        for i in range(self.Grid.width):
            for j in range(self.Grid.height):
                x = i * (self.Canvas.width // self.Grid.width)
                y = j * (self.Canvas.height // self.Grid.height)
                self.assertEqual(self.Canvas.surface.get_at((x,y)), self.color, f"Wrong color at {x}:{y}")

GridTest=unittest.TestLoader().loadTestsFromTestCase(TestGrid)
