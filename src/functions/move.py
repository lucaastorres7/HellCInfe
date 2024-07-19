import pygame


def move_player(event, character):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            character.direction.x = -1
        elif event.key == pygame.K_RIGHT:
            character.direction.x = 1
        elif event.key == pygame.K_UP:
            character.direction.y = -1
        elif event.key == pygame.K_DOWN:
            character.direction.y = 1
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            character.direction.x = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            character.direction.y = 0
