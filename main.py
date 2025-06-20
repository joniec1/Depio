import pygame
from player import Player
from bullet import Bullet

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player = Player(400, 300)  # start w środku ekranu
bullets = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            bullets.append(Bullet(player.pos, player.angle))

    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    player.update(keys, mouse_pos)
    for bullet in bullets:
        bullet.update()

    screen.fill((30, 30, 30))  # ciemne tło
    player.draw(screen)

    for bullet in bullets:
        bullet.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()