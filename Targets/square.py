import pygame
from target import Target
import config

class Squaretarget(Target):
    def __init__(self, pos):
        super().__init__(pos, hp = 20, color = config.yeallow)