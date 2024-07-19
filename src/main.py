from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from functions.move import move_player
from characters.player import Player
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('My game')

character_img = pygame.image.load('assets/player.png')

character = Player(character_img, 0, 300)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        move_player(event, character)

    character.update()

    screen.fill((0, 0, 0))

    character.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
