import pygame

class Target:
    def __init__(self, pos, hp, color):
        self.pos = pygame.Vector2(pos)
        self.hp = hp
        self.color = color

    def hit(self, damage: float) -> bool:
        self. hp -= damage
        return self.hp <= 0