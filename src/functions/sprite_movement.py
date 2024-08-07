import pygame


def sprite_movement(spritesheet, type: str, size: int, sprite_array: list):
    iteration = 0

    if type == 'idle':
        iteration = 2
    elif type == 'attack':
        iteration = 5
    elif type == 'moving':
        iteration = 4

    for i in range(iteration):
        action = spritesheet.subsurface(
            (i * 16, size), (16, 16))
        action = pygame.transform.scale(
            action, (16 * 5, 16 * 5))

        sprite_array.append(action)
