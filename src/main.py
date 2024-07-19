from settings import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_IMAGE, ROCK_IMAGE
from characters.static_objects import StaticObject
from functions.move import move_player
from characters.player import Player
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('HellCInfe')

character_img = pygame.image.load(PLAYER_IMAGE)
rock_img = pygame.image.load(ROCK_IMAGE)

character = Player(character_img, 0, 300)
rock = StaticObject(rock_img, 250, 400)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        move_player(event, character)

    character.update()

    if character.rect.colliderect(rock.rect):
        print("Collision detected!")
        character.direction = pygame.Vector2(0, 0)
        character.rect.topleft = (0, 300)

    screen.fill((0, 45, 0))

    character.draw(screen)
    rock.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
