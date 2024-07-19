from settings import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_IMAGE
from functions.move import move_player
from characters.player import Player
from characters.static_objects import StaticObject
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('HellCInfe')

character_img = pygame.image.load(PLAYER_IMAGE)

character = Player(character_img, 0, 300)
rock = StaticObject(character_img, 250, 400)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        move_player(event, character)

    character.update()

    screen.fill((0, 45, 0))

    character.draw(screen)
    rock.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
