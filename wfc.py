import pygame
from WaveFunctionCollaps.grid import Grid
from WaveFunctionCollaps.tile import Tile
from WaveFunctionCollaps.canvas import Canvas

CanvasSize = (801, 801)
Canvas = Canvas(CanvasSize)
Grid = Grid(width=20)
run = True
if __name__ == "__main__":
    Canvas.draw()
    while run:
        Grid.draw(Canvas, (200, 30, 100))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()
