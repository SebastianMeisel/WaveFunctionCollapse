import unittest
import pygame
from random import randrange
from WaveFunctionCollaps.image import Image



class TestImage(unittest.TestCase):
    def setUp(self):
        pygame.init()
        city: pygame.Surface = pygame.image.load("../assets/City.png").convert_alpha()
        self.Image = Image(city)

        # Ensure tiles are populated
        self.Image.extractTiles()

        self.sampleX = randrange(len(self.Image.tiles))  # Get valid tile row index
        self.sampleY = randrange(len(self.Image.tiles[0]))  # Get valid tile col index

        # Extract expected color from the top-left pixel of the sampled tile
        self.testColor = self.Image.img.get_at((self.sampleY * 3, self.sampleX * 3))

    def test_Image_exists(self):
        "Test, the Image class exists."
        self.assertIsNotNone(self.Image, "Image does not exist.")
        self.assertIsInstance(self.Image, Image, "Image is not a class.")

    def test_Image_isSurface(self):
        "Test, the Image is a Surface."
        self.assertIsInstance(self.Image.img, pygame.Surface, "Image is a Surface.")

    def test_Image_pixelArray(self):
        "Test, the Image class has a pixel array"
        self.assertIsNotNone(self.Image.pixels, "Image has no pixel array.")
        self.assertGreater(len(self.Image.pixels), 0, "Image.pixels is not an array.")
        self.assertGreater(len(self.Image.pixels[0]), 0, "Image.pixels is not a 2D array.")

    def test_Image_extractTiles(self):
        "Test the extractTiles method of Image."
        self.assertIsNotNone(self.Image.tiles)

        # Ensure extractTiles result matches stored tiles
        self.assertEqual(len(self.Image.extractTiles()), len(self.Image.tiles), 
                         "Image.tiles is not the return value of extractTiles method.")

        # Check the dimensions of tiles
        self.tile_rows = len(self.Image.tiles)
        self.tile_cols = len(self.Image.tiles[0]) if self.tile_rows > 0 else 0

        # Validate sampleX and sampleY are within bounds
        self.assertTrue(0 <= self.sampleX < self.tile_rows, 
                        f"sampleX {self.sampleX} out of range (max {self.tile_rows - 1})")
        self.assertTrue(0 <= self.sampleY < self.tile_cols, 
                        f"sampleY {self.sampleY} out of range (max {self.tile_cols - 1})")

        # Extracted tile's first pixel should match the expected testColor
        extracted_color = self.Image.tiles[self.sampleX][self.sampleY][0]  # First pixel of the tile
        expected_color = (self.testColor.r, self.testColor.g, self.testColor.b, self.testColor.a)  # Convert Color to Tuple

        self.assertEqual(
            extracted_color, 
            expected_color, 
            f"Image.tile[{self.sampleX},{self.sampleY}] is not the expected value of {expected_color}, got {extracted_color} instead."
        )

ImageTest=unittest.TestLoader().loadTestsFromTestCase(TestImage)
