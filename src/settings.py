import time

import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
HEALTH = 50

PLAYER_SPRITESHEET = pygame.image.load(
    'assets/characters/Player_Knight_SpriteSheet.png')
ROCK_IMAGE = 'assets/backgrounds/rock.png'
BONES_IMAGE = 'assets/backgrounds/bones.png'
MOEDA_IMAGE = 'assets/backgrounds/moeda.png'
POCAO_IMAGE = 'assets/backgrounds/pocao.png'
ESCUDO_IMAGE = 'assets/backgrounds/escudo.png'
CLOCK = pygame.time.Clock()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
