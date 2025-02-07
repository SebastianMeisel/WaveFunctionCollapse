import unittest
import pygame
from WaveFunctionCollaps.tile import Tile

class TestTile(unittest.TestCase):
    def setUp(self):
        self.Tile = Tile()

    def test_Tile_exists(self):
        "Test the Tile class exists."
        self.assertIsNotNone(self.Tile, "Tile does not exist.")
        self.assertIsInstance(self.Tile, Tile, "Tile is not a class.")

    def test_Tile_pixels(self):
        "Test the pixel array of Tile."
        self.assertIsNotNone(self.Tile.pixel, "Tile's pixel array does not exist.")
        self.assertIsInstance(self.Tile.pixel, list, "Tile.pixel is not an list.")

TileTest=unittest.TestLoader().loadTestsFromTestCase(TestTile)
