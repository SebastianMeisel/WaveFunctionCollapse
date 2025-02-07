import pygame
from .tile import Tile

class Grid():
    def __init__(self, width: int, height: int = 0):
        self.width = width
        self.height = height if height > 0 else width
        self.grid = []
        for _ in range(self.height):
            self.grid.append([0] * self.width)
        for row in range(self.height):
            for col in range(self.width):
                self.grid[row][col] = Tile()

    def draw(self, Canvas, color) -> bool:
        for i in range(self.width):
            for j in range(self.height):
                width = (Canvas.width // self.width)
                height = (Canvas.height // self.height)
                x = i * width
                y = j * height
                pygame.draw.rect(Canvas.surface, color, (x, y, x + width, y + height), 1, 1)
        return True
