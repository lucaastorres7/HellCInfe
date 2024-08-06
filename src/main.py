import sys

import pygame

from random import randint
from characters.player import Player
from characters.enemy import Enemy
from characters.static_objects import StaticObject
from functions.collision import collision
from functions.move import move_player
from settings import CLOCK, ROCK_IMAGE, SCREEN_HEIGHT, SCREEN_WIDTH, BONES_IMAGE, MOEDA_IMAGE, POCAO_IMAGE, ESCUDO_IMAGE
from menu import show_menu

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('HellCInfe')
choice_menu = show_menu(screen)

if choice_menu == "play":
    # Quantidade de moedas
    fonte = pygame.font.SysFont('arial', 40, True, True)
    quant_moedas, quant_pocao, quant_escudo = 0, 0, 0

    # Junta e adiciona os sprites ao player
    all_sprites = pygame.sprite.Group()
    character = Player(0, 300)
    all_sprites.add(character)

    rock_img = pygame.image.load(ROCK_IMAGE)
    bones_img = pygame.image.load(BONES_IMAGE)
    moeda_img = pygame.image.load(MOEDA_IMAGE)
    pocao_img = pygame.image.load(POCAO_IMAGE)
    escudo_img = pygame.image.load(ESCUDO_IMAGE)

    rock = StaticObject(rock_img, 250, 400)
    x_moeda = randint(80, 950)
    y_moeda = randint(80, 750)
    moeda = StaticObject(moeda_img, x_moeda, y_moeda)

    x_pocao = randint(80, 950)
    y_pocao = randint(80, 750)
    pocao = StaticObject(pocao_img, x_pocao, y_pocao)

    x_escudo = randint(80, 950)
    y_escudo = randint(80, 750)
    escudo = StaticObject(escudo_img, x_escudo, y_escudo)

    enemies = [
        Enemy(rock_img, 500, 300, 20),
    ]

    drops = []

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

        character.update()
        for enemy in enemies:
            enemy.update(character)

        for enemy in enemies:
            if character.is_attack and character.rect.colliderect(enemy.rect):
                print("Enemy hit!")
                enemy.take_damage(10)
                character.is_attack = False  # Reset attacking state

        screen.fill((0, 45, 0))

        character.draw(screen)
        rock.draw(screen)
        moeda.draw(screen)
        pocao.draw(screen)
        escudo.draw(screen)

        mensage = f'Moedas: {quant_moedas}'
        mensage1 = f'Poção: {quant_pocao}'
        mensage2 = f'Escudo: {quant_escudo}'
        text_format = fonte.render(mensage, False, (255, 255, 255))
        text_format1 = fonte.render(mensage1, False, (255, 255, 255))
        text_format2 = fonte.render(mensage2, False, (255, 255, 255))
        alive_enemies = []

        for enemy in enemies:
            if enemy.is_dead():
                drops.append(enemy.drop())
            else:
                alive_enemies.append(enemy)
        enemies = alive_enemies

        for enemy in enemies:
            enemy.draw(screen)

        for drop in drops:
            drop.draw(screen)

        collision(character, rock)

        if character.rect.colliderect(moeda):
            x_moeda = randint(80, 950)
            y_moeda = randint(80, 750)
            moeda = StaticObject(moeda_img, x_moeda, y_moeda)
            quant_moedas = quant_moedas + 1

        if character.rect.colliderect(pocao):
            x_pocao = randint(80, 950)
            y_pocao = randint(80, 750)
            pocao = StaticObject(pocao_img, x_pocao, y_pocao)
            quant_pocao = quant_pocao + 1

        if character.rect.colliderect(escudo):
            x_escudo = randint(80, 950)
            y_escudo = randint(80, 750)
            escudo = StaticObject(escudo_img, x_escudo, y_escudo)
            quant_escudo = quant_escudo + 1

        if character.is_dead():
            print("Player is dead!")
            running = False
        screen.blit(text_format, (750, 10))
        screen.blit(text_format1, (750, 50))
        screen.blit(text_format2, (750, 90))
        pygame.display.flip()

    pygame.quit()
    sys.exit()