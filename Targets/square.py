import pygame
from .target import Target
import config

class Squaretarget(Target):
    def __init__(self, pos):
        super().__init__(pos, hp = 20, color = config.yeallow)

    def draw(self, screen):
        size = 20
        x, y = self.pos
        half = size // 2
        points = [
            (x - half, y - half),  # lewy górny
            (x + half, y - half),  # prawy górny
            (x + half, y + half),  # prawy dolny
            (x - half, y + half)   # lewy dolny
        ]
        pygame.draw.polygon(screen, self.color, points)
        pygame.draw.polygon(screen, config.darker_yellow, points,2)