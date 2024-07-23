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
enemy1 = Enemy(rock_img, 500, 500, 100)

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

    if character.is_attack and character.rect.colliderect(enemy1.rect):
        print("Enemy hit!")
        enemy1.take_damage(10)
        character.attacking = False  # Reset attacking state

    screen.fill((0, 45, 0))

    character.draw(screen)
    rock.draw(screen)

    if not enemy1.is_dead():
        enemy1.draw(screen)

    enemy1.update(character)

    collision(character, rock)

    if character.is_dead():
        print("Player is dead!")
        running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
