import time

import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
HEALTH = 50

PLAYER_SPRITESHEET = pygame.image.load(
    'assets/characters/Player_Knight_SpriteSheet.png')
ENEMY_IMAGE = 'assets/enemy/enemy_left.png'
ROCK_IMAGE = 'assets/backgrounds/rock.png'
BONES_IMAGE = 'assets/backgrounds/bones.png'
COIN_IMAGE = 'assets/backgrounds/coin.png'
POTION_IMAGE = 'assets/backgrounds/potion.png'
SHIELD_IMAGE = 'assets/backgrounds/shield.png'
derrota_img = pygame.image.load(
    "assets/backgrounds/teladederrotabackground.jpg")
derrota_button_img = pygame.image.load("assets/assetsmenu/restartbutton.png")
quit_derrota_img = pygame.image.load("assets/assetsmenu/quitderrotabutton.png")

WIN_SCREEN = pygame.transform.scale(pygame.image.load(
    "assets/backgrounds/win_screen.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT))
DUNGEON_SCREEN = pygame.transform.scale(pygame.image.load(
    "assets/backgrounds/dungeon_screen.jpg"), (SCREEN_WIDTH, SCREEN_HEIGHT))

CLOCK = pygame.time.Clock()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
