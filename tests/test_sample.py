from test_canvas import *
from test_grid import *
from test_tile import *
from test_image import *
from test_tileset import *

AllTests=unittest.TestSuite([GridTest,TileTest, CanvasTest, ImageTest, TileSetTest])
#unittest.TextTestRunner(verbosity=2).run(AllTests)

unittest.main(verbosity=2)

# Local Variables:
# jinx-languages: "en_US"
# End:
