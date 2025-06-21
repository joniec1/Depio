import pygame
from player import Player
from bullet import Bullet
from targets.square import Squaretarget
import random 

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player = Player(400, 300)  # start w środku ekranu
bullets = []
squares = []

spawn_interval = 3000 #3000ms = 3s
last_spawn_time = pygame.time.get_ticks()

running = True
while running:

    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            bullets.append(Bullet(player.pos, player.angle))

    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    player.update(keys, mouse_pos)
    
    if current_time - last_spawn_time >= spawn_interval and len(squares) < 5: #asynchroniczne tworzenie kwadratów na ekranie
        x = random.randint(50, 750)
        y = random.randint(50, 550)
        squares.append(Squaretarget(pygame.Vector2(x, y)))
        last_spawn_time = current_time

    screen.fill((30, 30, 30))  # ciemne tło

    for bullet in bullets:
        bullet.update()

    for bullet in bullets:
        bullet.draw(screen)

    for square in squares:
        square.draw(screen)   

    player.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()