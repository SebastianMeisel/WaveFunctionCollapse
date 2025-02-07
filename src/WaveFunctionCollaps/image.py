import pygame

class Image:
    def __init__(self, image: pygame.Surface) -> None: 
        self.img = image
        self.pixels = pygame.surfarray.pixels3d(self.img)  # NumPy array of shape (W, H, 3)
        self.tiles = []  # 2D array to store extracted tiles

    def extractTiles(self) -> list:
        tile_size = 3
        img_width, img_height = self.img.get_width(), self.img.get_height()

        # Compute max number of full tiles
        tile_rows = img_height // tile_size
        tile_cols = img_width // tile_size

        # Create a correctly sized 2D list
        self.tiles = [[None for _ in range(tile_cols)] for _ in range(tile_rows)]

        # Iterate through full tiles only
        for j in range(tile_rows):
            for i in range(tile_cols):
                tile = []
                for k in range(tile_size):
                    for m in range(tile_size):
                        # Correct pixel access order (width, height)
                        col = i * tile_size + m
                        row = j * tile_size + k
                        r, g, b = self.pixels[col][row]  # Access in (width, height) order
                        tile.append((r, g, b, 255))  # Store as tuple
                self.tiles[j][i] = tile  # Store tile in 2D list

        return self.tiles
