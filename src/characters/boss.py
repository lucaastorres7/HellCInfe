import pygame
import time
from settings import BONES_IMAGE
from characters.drop import Drop

item_drop = pygame.image.load(BONES_IMAGE)
move_sprites_paths = [
    r"assets/characters/moveB1.png",]

attack_sprites_paths = []

class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y, move_sprites_paths, attack_sprites_paths, life_Boss, collectible=item_drop):
        super().__init__()

       # Carregar imagens individuais para os sprites de movimento e ataque
        self.move_sprites = [pygame.image.load(path).convert_alpha() for path in move_sprites_paths]
        self.attack_sprites = [pygame.image.load(path).convert_alpha() for path in attack_sprites_paths]

        if not self.move_sprites:
            raise ValueError("Nenhuma sprite de movimento foi carregada.")

        
        self.image = self.move_sprites[0]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.life_Boss = life_Boss
        self.attack_range = 50
        self.last_attack_Boss = 0
        self.cooldown_attack_Boss = 1.0
        self.collectible = collectible
        self.current_animation = self.move_sprites
        self.animation_index = 0
        self.speed_animation_Boss = 0.1
        self.speed_Boss = 1
        self.last_animation_update = time.time()

    def update(self, target):
        # Atualização da animação
        now = time.time()
        if now - self.last_animation_update > self.speed_animation_Boss:
            self.last_animation_update = now
            if len(self.current_animation) > 0:
                self.animation_index = (self.animation_index + 1) % len(self.current_animation)
                self.image = self.current_animation[self.animation_index]
            else:
                print("A lista de animação está vazia.")
        
        # Movimentação do Boss
        direction = pygame.Vector2(target.rect.x - self.rect.x, target.rect.y - self.rect.y)
        distance = direction.length()
        
        if distance > 0:
            direction = direction.normalize()
            self.rect.x += direction.x * self.speed_Boss
            self.rect.y += direction.y * self.speed_Boss

        # Lógica de ataque
        if distance <= self.attack_range and now - self.last_attack_Boss > self.cooldown_attack_Boss:
            self.attack(target)
            self.last_attack_Boss = now

    def attack(self, target):
        # Lógica de ataque do Boss
        print("Boss attacks player!")
        target.take_damage(10)  # Ajuste conforme necessário

    def damage_taken(self, value):
        if self.life_Boss > 0:
            self.life_Boss -= value
        print(f"Boss Life: {self.life_Boss}")

    def defeat(self):
        self.kill()  # Remove o boss do grupo de sprites
        if self.collectible:
            return Drop(self.collectible, self.rect.x, self.rect.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def drop(self):
        return Drop(self.collectible, self.rect.x, self.rect.y)

