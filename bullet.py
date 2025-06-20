import pygame
import math
import config

class Bullet:
    def __init__(self, pos, angle):
        self.pos = pygame.Vector2(pos)
        self.speed = 7
        self.radius = config.bullet_size
        self.color = config.blue_player  # kolor taki sam jak gracz

        # Ruch w kierunku kąta lufy
        angle_rad = math.radians(-angle)
        self.velocity = pygame.Vector2(
            math.cos(angle_rad), math.sin(angle_rad)
        ) * self.speed

    def update(self):
        self.pos += self.velocity

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
        pygame.draw.circle(screen, config.blue_outline, self.pos, self.radius, 2)