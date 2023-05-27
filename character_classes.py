import pygame
import global_constants

class Character:
    def __init__(self, width, height, speed, sprite_paths):
        self.width = width
        self.height = height
        self.speed = speed
        self.sprites = []
        self.current_sprite_index = 0
        self.load_sprites(sprite_paths)

    def load_sprites(self, sprite_paths):
        for path in sprite_paths:
            sprite = pygame.image.load(path).convert_alpha()
            sprite = pygame.transform.scale(sprite, (self.width, self.height))
            self.sprites.append(sprite)

    def get_current_sprite(self):
        return self.sprites[self.current_sprite_index]

    def update_sprite(self):
        self.current_sprite_index = (self.current_sprite_index + 1) % len(self.sprites)

class Player(Character):
    def __init__(self, sprite_paths):
        super().__init__(50, 50, 5, sprite_paths)
        self.x = (global_constants.SCREEN_WIDTH - self.width) // 2
        self.y = (global_constants.SCREEN_HEIGHT - self.height) // 2

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.update_sprite()
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.update_sprite()
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.update_sprite()
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.update_sprite()
            self.y += self.speed