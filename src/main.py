import sys
from random import randint

import pygame

from characters.enemy import Enemy
from characters.player import Player
from characters.boss import Boss, spritesheet_path
from characters.static_objects import StaticObject
from functions.collision import collision
from functions.move import move_player
from characters.player import Player
from characters.enemy import Enemy
from ui.defeat import show_defeat
from ui.menu import show_menu
from ui.win import show_win
from random import randint
from settings import *
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('HellCInfe')
choice_menu = show_menu(screen)

if choice_menu == "quit":
    pygame.quit()
    sys.exit()

# Quantidade de moedas
fonte = pygame.font.SysFont('arial', 40, True, True)
quant_moedas, quant_pocao, quant_escudo = 0, 0, 0
quant_deads = 0 

# Junta e adiciona os sprites ao player
all_sprites = pygame.sprite.Group()
character = Player(0, 300)
all_sprites.add(character)

# Junta e adiciona os sprites ao Boss
boss = Boss(32, 32, spritesheet_path, 20) 
all_sprites.add(boss) 

enemy_img = pygame.image.load(ENEMY_IMAGE)
rock_img = pygame.image.load(ROCK_IMAGE)
bones_img = pygame.image.load(BONES_IMAGE)
moeda_img = pygame.image.load(MOEDA_IMAGE)
coin_spawn = False
pocao_img = pygame.image.load(POCAO_IMAGE)
potion_spawn = False
escudo_img = pygame.image.load(ESCUDO_IMAGE)
shield_spawn = False

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
    Enemy(enemy_img, 500, 300, 20),
]

drops = []

contador = 0
verification = 1
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
            
    if character.is_attack and character.rect.colliderect(boss.rect) and boss.life_Boss > 0:
        print("Boss hit!")
        boss.damage_taken(10)  # Aplica dano ao boss
        character.is_attack = False  
 
    if boss.life_Boss > 0 and contador > 3:
        boss.update(character)  
    else:
         # Se o boss foi derrotado  
          for drop_item in range(verification):
            verification -= 1
            if boss.life_Boss <= 0:
                drops.append(boss.drop()) 
            boss.defeat()
            if boss in all_sprites:
                all_sprites.remove(boss)  # Remover o boss do grupo de sprites
            boss_defeated = True


    screen.fill((0, 12, 0))
    
    # O boss só vai ser desenhado após o player derrotar um número expecífico de inimigos
    if contador > 3:
        boss.draw(screen)
        all_sprites.draw(screen)
    
    character.draw(screen)
    rock.draw(screen)
    moeda.draw(screen) 
    pocao.draw(screen)
    escudo.draw(screen)

    mensage = f'Moedas: {character.coins}'
    mensage1 = f'Poção: {character.potions}'
    mensage2 = f'Escudo: {character.shields}'
    text_format = fonte.render(mensage, False, (255, 255, 255))
    text_format1 = fonte.render(mensage1, False, (255, 255, 255))
    text_format2 = fonte.render(mensage2, False, (255, 255, 255))
    alive_enemies = []

    for enemy in enemies:
        if enemy.is_dead():
            drops.append(enemy.drop())
            x_enemy = randint(50, 950)
            y_enemy = randint(50, 750)
            enemies.append(Enemy(enemy_img, y_enemy, 300, 20),)
            contador += 1
        else:
            alive_enemies.append(enemy)
    enemies = alive_enemies

    for enemy in enemies:
        enemy.draw(screen)

    for drop in drops:
        drop.draw(screen)

    collision(character, rock)
    if character.rect.colliderect(moeda):
        character.coins = character.coins + 1
        x_moeda = -100
        y_moeda = -100
        moeda = StaticObject(moeda_img, x_moeda, y_moeda)
        coin_spawn_time = time.time()
        coin_spawn = True

    if coin_spawn:
        coin_elapsed_time = time.time() - coin_spawn_time
        if coin_elapsed_time > 5:
            x_moeda = randint(80, 950)
            y_moeda = randint(80, 750)
            moeda = StaticObject(moeda_img, x_moeda, y_moeda)
            coin_spawn = False

    if character.rect.colliderect(pocao):
        character.potions = character.potions + 1
        character.heal(10)
        x_pocao = -100
        y_pocao = -100
        pocao = StaticObject(pocao_img, x_pocao, y_pocao)
        potion_spawn_time = time.time()
        potion_spawn = True

    if potion_spawn:
        potion_elapsed_time = time.time() - potion_spawn_time
        if potion_elapsed_time > 5:
            x_pocao = randint(80, 950)
            y_pocao = randint(80, 750)
            pocao = StaticObject(pocao_img, x_pocao, y_pocao)
            potion_spawn = False

    if character.rect.colliderect(escudo):
        character.shield()
        character.shields = character.shields + 1
        x_escudo = -100
        y_escudo = -100
        escudo = StaticObject(escudo_img, x_escudo, y_escudo)
        shield_spawn_time = time.time()
        shield_spawn = True

    if shield_spawn:
        shield_elapsed_time = time.time() - shield_spawn_time
        if shield_elapsed_time > 10:
            x_escudo = randint(80, 950)
            y_escudo = randint(80, 750)
            escudo = StaticObject(escudo_img, x_escudo, y_escudo)
            shield_spawn = False

    if character.is_shield:
        character.elapsed_time = time.time() - character.invulnerability_start
        if character.elapsed_time > character.invulnerability_time:
            print("its over")
            character.is_shield = False

    if character.is_dead():
        show_defeat(character=character)

    if character.won():
        show_win(character=character)

    screen.blit(text_format, (750, 10))
    screen.blit(text_format1, (750, 50))
    screen.blit(text_format2, (750, 90))
    pygame.display.flip()

pygame.quit()
sys.exit() 
