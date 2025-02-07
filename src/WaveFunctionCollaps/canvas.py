import pygame

class Canvas():
    def __init__(self, size: tuple) -> None:
        self.size: tuble = size
        self.width: int = size[0]
        self.height: int = size[1]

    def draw(self) -> bool:
        self.surface = pygame.display.set_mode(self.size)
        self.surface.set_alpha(0)
        return True
