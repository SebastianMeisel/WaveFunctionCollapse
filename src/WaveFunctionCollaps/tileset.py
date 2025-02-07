import pygame

class TileSet():
    def __init__(self):
        self.Set: list = []

    def create(self, tiles: list) -> list:
        self.Set: list = [] # reset 
        for tile in tiles:
            self.Set.append(0)
        return self.Set
