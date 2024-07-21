import pygame

from settings import PLAYER_SPRITESHEET, SCREEN_HEIGHT, SCREEN_WIDTH


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # Lista para armazenar os sprites do personagem
        self.idle = []
        # Loop que corta o spritesheet e armazena na lista
        for i in range(2):
            img_idle = PLAYER_SPRITESHEET.subsurface((i * 16, 0), (16, 16))
            img_idle = pygame.transform.scale(img_idle, (16 * 5, 16 * 5))
            self.idle.append(img_idle)

        self.index = 0
        self.image = self.idle[self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.speed = 4
        self.direction = pygame.Vector2(0, 0)

    def update(self):
        # Update da lista para ficar continuadamente em idle
        if self.index > 2:
            self.index = 0
        self.image = self.image = self.idle[int(self.index)]
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
