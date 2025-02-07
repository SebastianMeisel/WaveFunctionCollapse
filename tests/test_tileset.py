import unittest
import pygame
from WaveFunctionCollaps.tileset import TileSet
from WaveFunctionCollaps.image import Image

class TestTileSet(unittest.TestCase):
    def setUp(self):
        pygame.init()
        city: pygame.Surface = pygame.image.load("../assets/City.png").convert_alpha()
        self.Image = Image(city)
        self.tiles = self.Image.extractTiles()
        self.TileSet = TileSet()

    def test_TileSet_exists(self):
        "Test the TileSet class exists."
        self.assertIsNotNone(self.TileSet, "TileSet does not exist.")
        self.assertIsInstance(self.TileSet, TileSet, "TileSet is not a class.")

    def test_TileSet_create(self):
        "Test the TileSet create() method."
        self.assertIsInstance(self.TileSet.create(self.tiles), list,
                              "TileSet.create() does not return list.")
        self.assertEqual(len(self.TileSet.create(self.tiles)),len(self.tiles), "Created TileSet has length other then tiles array returned by Image.extractTiles.")
        self.assertIsNotNone(self.TileSet.Set, "TileSet has no Set.")

TileSetTest=unittest.TestLoader().loadTestsFromTestCase(TestTileSet)
