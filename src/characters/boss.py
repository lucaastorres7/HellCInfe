import pygame
import time
from settings import BONES_IMAGE
from characters.drop import Drop

spritesheet_path = "assets/characters/BOSS.png"
item_drop = pygame.image.load(BONES_IMAGE)

class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y, spritesheet_path, life_Boss, collectible=item_drop):
        super().__init__()

        self.sprite_size = (32, 32)  # Tamanho dos sprites individuais na folha
        self.num_move_sprites = 12  # Número de sprites de movimento por linha
        self.num_attack_sprites = 12  # Número de sprites de ataque por linha

        self.move_sprites = []
        self.attack_sprites = []

        # Carregar a folha de sprites usando o caminho fornecido
        self.spritesheet = pygame.image.load(spritesheet_path).convert_alpha()
        spritesheet_width, spritesheet_height = self.spritesheet.get_size()

        # Verificar se a folha de sprites tem espaço suficiente para todos os sprites
        if spritesheet_width < self.num_move_sprites * self.sprite_size[0] or spritesheet_height < 2 * self.sprite_size[1]:
            raise ValueError("A folha de sprites é menor do que o esperado.")

        # Carregar sprites de movimento (primeira linha da folha)
        for i in range(self.num_move_sprites):
            rect = pygame.Rect(i * self.sprite_size[0], 0, self.sprite_size[0], self.sprite_size[1])
            if rect.right > spritesheet_width or rect.bottom > spritesheet_height:
                raise ValueError("O retângulo para o subsurface está fora dos limites da folha de sprites.")
            img = self.spritesheet.subsurface(rect)
            self.move_sprites.append(pygame.transform.scale(img, self.sprite_size))

        # Carregar sprites de ataque (segunda linha da folha)
        for i in range(self.num_attack_sprites):
            rect = pygame.Rect(i * self.sprite_size[0], self.sprite_size[1], self.sprite_size[0], self.sprite_size[1])
            if rect.right > spritesheet_width or rect.bottom > spritesheet_height:
                raise ValueError("O retângulo para o subsurface está fora dos limites da folha de sprites.")
            img = self.spritesheet.subsurface(rect)
            self.attack_sprites.append(pygame.transform.scale(img, self.sprite_size))

        if self.move_sprites:
            self.image = self.move_sprites[0]
        else:
            raise ValueError("Nenhuma sprite de movimento foi carregada.")

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

