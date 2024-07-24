import sys

import pygame

from characters.player import Player
from characters.enemy import Enemy
from characters.static_objects import StaticObject
from functions.collision import collision
from functions.move import move_player
from settings import CLOCK, ROCK_IMAGE, SCREEN_HEIGHT, SCREEN_WIDTH

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('HellCInfe')

# Junta e adiciona os sprites ao player
all_sprites = pygame.sprite.Group()
character = Player(0, 300)
all_sprites.add(character)

rock_img = pygame.image.load(ROCK_IMAGE)

rock = StaticObject(rock_img, 250, 400)

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

    alive_enemies = []
    for enemy in enemies:
        if enemy.is_dead():
            drops.append(enemy.drop(rock_img))
        else:
            alive_enemies.append(enemy)
    enemies = alive_enemies

    for enemy in enemies:
        enemy.draw(screen)

    for drop in drops:
        drop.draw(screen)

    collision(character, rock)

    if character.is_dead():
        print("Player is dead!")
        running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
