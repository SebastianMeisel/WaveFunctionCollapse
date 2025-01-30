import unittest
from WaveFunctionCollaps.main import main 

class TestMain(unittest.TestCase):

    def test_main_exist(self):
        self.assertIsInstance(main, Class)


unittest.main()
