import sys
from random import randint

import pygame

from characters.enemy import Enemy
from characters.player import Player
from characters.static_objects import StaticObject
from functions.move import move_player
from settings import *
from ui.defeat import show_defeat
from ui.menu import show_menu
from ui.win import show_win

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('HellCInfe')
choice_menu = show_menu(screen)

if choice_menu == "quit":
    pygame.quit()
    sys.exit()

# Quantidade de coins
fonte = pygame.font.SysFont('arial', 40, True, True)
quant_deads = 0

# Junta e adiciona os sprites ao player
all_sprites = pygame.sprite.Group()
character = Player(0, 300)
all_sprites.add(character)

enemy_img = pygame.image.load(ENEMY_IMAGE)
rock_img = pygame.image.load(ROCK_IMAGE)
bones_img = pygame.image.load(BONES_IMAGE)
coin_img = pygame.image.load(COIN_IMAGE)
coin_spawn = False
potion_img = pygame.image.load(POTION_IMAGE)
potion_spawn = False
shield_img = pygame.image.load(SHIELD_IMAGE)
shield_spawn = False


x_coin = randint(80, 950)
y_coin = randint(80, 750)
coin = StaticObject(coin_img, x_coin, y_coin)

x_potion = randint(80, 950)
y_potion = randint(80, 750)
potion = StaticObject(potion_img, x_potion, y_potion)

x_shield = randint(80, 950)
y_shield = randint(80, 750)
shield = StaticObject(shield_img, x_shield, y_shield)

obstacles = [
    StaticObject(rock_img, randint(40, 950), randint(40, 750)),
    StaticObject(rock_img, randint(40, 950), randint(40, 750)),
    StaticObject(rock_img, randint(40, 950), randint(40, 750)),
    StaticObject(rock_img, randint(40, 950), randint(40, 750)),
]

enemies = [
    Enemy(enemy_img, 500, 300, 20),
]

drops = []

stop = False
defeat = False
running = True
while running:
    CLOCK.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                character.attack()
        move_player(event, character)

    if not stop:
        character.update(obstacles)

        for enemy in enemies:
            enemy.update(character)

    for enemy in enemies:
        if character.is_attack and character.rect.colliderect(enemy.rect):
            enemy.take_damage(10)
            character.is_attack = False  # Reset attacking state

    screen.blit(DUNGEON_SCREEN, (0, 0))

    character.draw(screen)
    coin.draw(screen)
    potion.draw(screen)
    shield.draw(screen)

    mensage = f'Coins: {character.coins}'
    text_format = fonte.render(mensage, False, (255, 255, 255))

    alive_enemies = []

    for enemy in enemies:
        if enemy.is_dead():
            drops.append(enemy.drop())
            if quant_deads % 4 == 0:
                for i in range(2):
                    x_enemy = randint(50, 950)
                    y_enemy = randint(50, 750)
                    enemies.append(Enemy(enemy_img, y_enemy, 300, 20),)
            else:
                x_enemy = randint(50, 950)
                y_enemy = randint(50, 750)
                enemies.append(Enemy(enemy_img, y_enemy, 300, 20),)
        else:
            alive_enemies.append(enemy)
    enemies = alive_enemies

    for obstacle in obstacles:
        obstacle.draw(screen)

    for enemy in enemies:
        enemy.draw(screen)

    for drop in drops:
        drop.draw(screen)

    if character.rect.colliderect(coin):
        character.coins = character.coins + 1
        x_coin = -100
        y_coin = -100
        coin = StaticObject(coin_img, x_coin, y_coin)
        coin_spawn_time = time.time()
        coin_spawn = True

    if coin_spawn:
        coin_elapsed_time = time.time() - coin_spawn_time
        if coin_elapsed_time > 5:
            x_coin = randint(80, 950)
            y_coin = randint(80, 750)
            coin = StaticObject(coin_img, x_coin, y_coin)
            coin_spawn = False

    if character.rect.colliderect(potion):
        character.potions = character.potions + 1
        character.heal(10)
        x_potion = -100
        y_potion = -100
        potion = StaticObject(potion_img, x_potion, y_potion)
        potion_spawn_time = time.time()
        potion_spawn = True

    if potion_spawn:
        potion_elapsed_time = time.time() - potion_spawn_time
        if potion_elapsed_time > 5:
            x_potion = randint(80, 950)
            y_potion = randint(80, 750)
            potion = StaticObject(potion_img, x_potion, y_potion)
            potion_spawn = False

    if character.rect.colliderect(shield):
        character.shield()
        character.shields = character.shields + 1
        x_shield = -100
        y_shield = -100
        shield = StaticObject(shield_img, x_shield, y_shield)
        shield_spawn_time = time.time()
        shield_spawn = True

    if shield_spawn:
        shield_elapsed_time = time.time() - shield_spawn_time
        if shield_elapsed_time > 10:
            x_shield = randint(80, 950)
            y_shield = randint(80, 750)
            shield = StaticObject(shield_img, x_shield, y_shield)
            shield_spawn = False

    if character.is_shield:
        character.elapsed_time = time.time() - character.invulnerability_start
        if character.elapsed_time > character.invulnerability_time:
            character.is_shield = False

    if character.is_dead():
        stop = True
        defeat = True

    if character.won():
        stop = True

    if stop:
        if defeat:
            response = show_defeat()
        else:
            response = show_win()
        if response == "restart":
            character.reset()
            defeat = False
            stop = False

    if not stop:
        screen.blit(text_format, (750, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
