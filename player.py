import pygame
import math

class Player:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.radius = 20
        self.color = (0, 200, 255)
        self.outline = (0, 100, 160)
        self.angle = 0

    def update(self, keys, mouse_pos):
        velocity = pygame.Vector2(0, 0)
        speed = 3

        if keys[pygame.K_w]: velocity.y -= 1
        if keys[pygame.K_s]: velocity.y += 1
        if keys[pygame.K_a]: velocity.x -= 1
        if keys[pygame.K_d]: velocity.x += 1

        if velocity.length_squared() > 0:
            velocity = velocity.normalize() * speed
            self.pos += velocity

        direction = pygame.Vector2(mouse_pos) - self.pos
        self.angle = math.degrees(math.atan2(-direction.y, direction.x))

    def draw(self, screen):
        self.draw_barrel(screen)
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
        pygame.draw.circle(screen, self.outline, self.pos, self.radius, 3)

    def draw_barrel(self, screen):
        barrel_length = 30
        barrel_width = 10
        angle_rad = math.radians(-self.angle)

        cx, cy = self.pos

        direction = pygame.Vector2(math.cos(angle_rad), math.sin(angle_rad))
        perp = pygame.Vector2(-direction.y, direction.x)

        p1 = self.pos + direction * barrel_length + perp * (barrel_width / 2)
        p2 = self.pos + direction * barrel_length - perp * (barrel_width / 2)
        p3 = self.pos - perp * (barrel_width / 2)
        p4 = self.pos + perp * (barrel_width / 2)

        pygame.draw.polygon(screen, (100, 100, 100), [p1, p2, p3, p4])
