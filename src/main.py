import sys

import pygame

from characters.player import Player
from characters.static_objects import StaticObject
from functions.collision import collision
from functions.move import move_player
from settings import (CLOCK, PLAYER_SPRITESHEET, ROCK_IMAGE, SCREEN_HEIGHT,
                      SCREEN_WIDTH)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('HellCInfe')

# Junta e adiciona os sprites ao player
all_sprites = pygame.sprite.Group()
character = Player(0, 300)
all_sprites.add(character)

rock_img = pygame.image.load(ROCK_IMAGE)

rock = StaticObject(rock_img, 250, 400)

running = True
while running:
    CLOCK.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        move_player(event, character)

    character.update()

    screen.fill((0, 45, 0))

    character.draw(screen)
    rock.draw(screen)

    collision(character, rock)

    pygame.display.flip()

pygame.quit()
sys.exit()
