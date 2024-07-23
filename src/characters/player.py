import pygame

from settings import PLAYER_SPRITESHEET, SCREEN_HEIGHT, SCREEN_WIDTH, HEALTH


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.health = HEALTH

        self.idle_right = []
        for i in range(2):
            img_idle_right = PLAYER_SPRITESHEET.subsurface(
                (i * 16, 0), (16, 16))
            img_idle_right = pygame.transform.scale(
                img_idle_right, (16 * 5, 16 * 5))
            self.idle_right.append(img_idle_right)

        self.idle_left = []
        for i in range(2):
            img_idle_left = PLAYER_SPRITESHEET.subsurface(
                (i * 16, 16), (16, 16))
            img_idle_left = pygame.transform.scale(
                img_idle_left, (16 * 5, 16 * 5))
            self.idle_left.append(img_idle_left)

        self.right_attack_sprt = []
        self.is_attack = False
        for i in range(5):
            img_right_atk = PLAYER_SPRITESHEET.subsurface(
                (i * 16, 64), (16, 16))
            img_right_atk = pygame.transform.scale(
                img_right_atk, (16 * 5, 16 * 5))
            self.right_attack_sprt.append(img_right_atk)

        self.left_attack_sprt = []
        for i in range(5):
            img_left_atk = PLAYER_SPRITESHEET.subsurface(
                (i * 16, 80), (16, 16))
            img_left_atk = pygame.transform.scale(
                img_left_atk, (16 * 5, 16 * 5))
            self.left_attack_sprt.append(img_left_atk)

        self.moving_right_sprt = []
        for i in range(4):
            img_moving_right = PLAYER_SPRITESHEET.subsurface(
                (i * 16, 32), (16, 16))
            img_moving_right = pygame.transform.scale(
                img_moving_right, (16 * 5, 16 * 5))
            self.moving_right_sprt.append(img_moving_right)

        self.moving_left_sprt = []
        for i in range(4):
            img_moving_left = PLAYER_SPRITESHEET.subsurface(
                (i * 16, 48), (16, 16))
            img_moving_left = pygame.transform.scale(
                img_moving_left, (16 * 5, 16 * 5))
            self.moving_left_sprt.append(img_moving_left)

        self.index = 0
        self.image = self.idle_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.speed = 4
        self.direction = pygame.Vector2(0, 0)
        self.is_moving = False
        self.last_direction = "right"  # Default direction

    def attack(self):
        self.is_attack = True

    def moving(self):
        self.is_moving = True

    def update(self):
        if self.is_attack:
            if self.index > 5:
                self.index = 0
                self.is_attack = False

            if self.last_direction == "right":
                self.image = self.right_attack_sprt[int(self.index)]
            elif self.last_direction == "left":
                self.image = self.left_attack_sprt[int(self.index)]
            self.index += 0.1

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
        self.rect.y += self.direction.y * self.speed

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0

        print(f"Player: {self.health}/{HEALTH} HP")

    def is_dead(self):
        return self.health <= 0
