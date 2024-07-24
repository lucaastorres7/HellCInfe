import pygame


def collision(character, object):
    if character.rect.colliderect(object.rect):
        print("Collision detected!")
        character.direction = pygame.Vector2(0, 0)
        character.rect.topleft = (0, 0)