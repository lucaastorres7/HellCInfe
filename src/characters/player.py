from functions.sprite_movement import sprite_movement
from settings import *
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.idle_right = []
        self.idle_left = []
        self.right_attack_sprt = []
        self.left_attack_sprt = []

        sprite_movement(PLAYER_SPRITESHEET, 'idle', 0, self.idle_right)

        sprite_movement(PLAYER_SPRITESHEET, 'idle', 16, self.idle_left)

        sprite_movement(PLAYER_SPRITESHEET, 'attack',
                        64, self.right_attack_sprt)

        sprite_movement(PLAYER_SPRITESHEET, 'attack',
                        80, self.left_attack_sprt)

        self.index = 0
        self.speed = 4
        self.direction = pygame.Vector2(0, 0)
        self.is_moving = False
        self.last_direction = "right"

        self.image = self.idle_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.current_health = HEALTH
        self.max_health = HEALTH

        self.coins = 0
        self.potions = 0
        self.shields = 0
        self.is_attack = False

        self.is_shield = False
        self.invulnerability_time = 3
        self.invulnerability_start = 0

        self.moving_right_sprt = []
        sprite_movement(
            PLAYER_SPRITESHEET, 'moving', 32, self.moving_right_sprt)

        self.moving_left_sprt = []
        sprite_movement(
            PLAYER_SPRITESHEET, 'moving', 48, self.moving_left_sprt)

    def attack(self):
        self.is_attack = True

    def heal(self, amount):
        self.current_health += amount
        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def shield(self):
        self.is_shield = True
        self.invulnerability_start = time.time()

    def moving(self):
        self.is_moving = True

    def update(self, obstacles):
        if self.is_attack:
            if self.index > 5:
                self.index = 0
                self.is_attack = False

            if self.last_direction == "right":
                self.image = self.right_attack_sprt[int(self.index)]

            elif self.last_direction == "left":
                self.image = self.left_attack_sprt[int(self.index)]
            self.index += 0.2

        elif self.is_moving:
            if self.direction.x == 1:
                if self.index > 4:
                    self.index = 0

                self.image = self.moving_right_sprt[int(self.index)]
                self.index += 0.1
                self.last_direction = "right"

            elif self.direction.x == -1:
                if self.index > 4:
                    self.index = 0

                self.image = self.moving_left_sprt[int(self.index)]
                self.index += 0.1
                self.last_direction = "left"

            elif self.direction.y == 1 or self.direction.y == -1:
                if self.index > 4:
                    self.index = 0

                if self.last_direction == "right":
                    self.image = self.moving_right_sprt[int(self.index)]

                elif self.last_direction == "left":
                    self.image = self.moving_left_sprt[int(self.index)]
                self.index += 0.1

        else:
            if self.index > 2:
                self.index = 0

            if self.last_direction == "right":
                self.image = self.idle_right[int(self.index)]
            elif self.last_direction == "left":
                self.image = self.idle_left[int(self.index)]
            self.index += 0.05

        self.rect.x += self.direction.x * self.speed
        self.handle_collisions(obstacles, 'horizontal')
        self.rect.y += self.direction.y * self.speed
        self.handle_collisions(obstacles, 'vertical')

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def handle_collisions(self, obstacles, direction):
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                if direction == 'horizontal':
                    if self.direction.x > 0:  # Moving right
                        self.rect.right = obstacle.rect.left
                    elif self.direction.x < 0:  # Moving left
                        self.rect.left = obstacle.rect.right

                elif direction == 'vertical':
                    if self.direction.y > 0:  # Moving down
                        self.rect.bottom = obstacle.rect.top
                    elif self.direction.y < 0:  # Moving up
                        self.rect.top = obstacle.rect.bottom

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)
        self.render_health_bar(surface)

    def take_damage(self, amount):
        if self.is_shield:
            pass
        else:
            self.current_health -= amount
            if self.current_health <= 0:
                self.current_health = 0

    def is_dead(self):
        return self.current_health <= 0

    def won(self):
        return self.coins == 10

    def render_health_bar(self, surface):
        health_bar_width = self.rect.width
        health_bar_height = 10
        health_bar_x = self.rect.x
        health_bar_y = self.rect.y - health_bar_height - 2

        health_ratio = self.current_health / self.max_health

        pygame.draw.rect(surface, RED, (health_bar_x,
                         health_bar_y, health_bar_width, health_bar_height))

        pygame.draw.rect(surface, GREEN, (health_bar_x, health_bar_y,
                         health_bar_width * health_ratio, health_bar_height))

    def reset(self):
        self.current_health = self.max_health
        self.rect.topleft = (100, 100)
        self.is_shield = False
        self.invulnerability_start = 0
        self.is_attack = False
        self.is_moving = False
        self.direction = pygame.Vector2(0, 0)
        self.index = 0
        self.last_direction = "right"
        self.image = self.idle_right[self.index]
        self.coins = 0
        self.potions = 0
        self.shields = 0
