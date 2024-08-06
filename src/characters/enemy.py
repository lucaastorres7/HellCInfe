import time

import pygame as pg

from characters.drop import Drop
from settings import BONES_IMAGE

bones_img = pg.image.load(BONES_IMAGE)


class Enemy:
    def __init__(self, image, x, y, health, item_drop=bones_img):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.health = health
        self.speed = 2  # Adjust the speed as needed
        self.attack_range = 50  # Adjust attack range as needed
        self.last_attack_time = 0  # Track last attack time
        self.attack_cooldown = 1.0  # Cooldown time in seconds
        self.item_drop = item_drop

    def update(self, target):
        direction = pg.Vector2(target.rect.x - self.rect.x,
                               target.rect.y - self.rect.y)

        if direction.length() > 0:
            direction = direction.normalize()

        self.rect.x += direction.x * self.speed
        self.rect.y += direction.y * self.speed

        if self.rect.colliderect(target.rect) and self.can_attack():
            self.attack(target)

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
        print(f"Enemy health: {self.health}/100")

    def can_attack(self):
        current_time = time.time()
        if current_time - self.last_attack_time > self.attack_cooldown:
            self.last_attack_time = current_time
            return True
        return False

    def attack(self, target):
        print("Enemy attacks player!")
        target.take_damage(10)  # Adjust the damage amount as needed

    def is_dead(self):
        return self.health <= 0

    def drop(self):
        return Drop(self.item_drop, self.rect.x, self.rect.y)
