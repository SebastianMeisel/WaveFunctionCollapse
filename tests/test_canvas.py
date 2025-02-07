import unittest
import pygame
from WaveFunctionCollaps.canvas import Canvas

class TestCanvas(unittest.TestCase):
    def setUp(self):
        self.size = (800,800)
        self.Canvas = Canvas(size=self.size)

    def test_Canvas_exists(self):
        "Test the Canvas class exists."
        self.assertIsNotNone(self.Canvas, "Canvas does not exist.")
        self.assertIsInstance(self.Canvas, Canvas, "Canvas is not a class.")

    def test_CanvasHasSize(self):
        """Test that Canvas has an attribute size of type tuple.
           Check it's the size given at initialization of Canvas.
        """
        self.assertIsNotNone(self.Canvas.size)
        self.assertIsInstance(self.Canvas.size, tuple)
        self.assertEqual(self.Canvas.size, self.size)
        self.assertEqual(self.Canvas.width, self.size[0])
        self.assertEqual(self.Canvas.height, self.size[1])

    def test_drawCanvas(self):
        """Test that Canvas has a draw method,
           that initializes the attribute surface with an Surface object.
        """
        self.assertTrue(self.Canvas.draw())
        self.assertIsInstance(self.Canvas.surface, pygame.Surface)


CanvasTest=unittest.TestLoader().loadTestsFromTestCase(TestCanvas)
