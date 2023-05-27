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
            if self.x - self.speed >= 0:  # Check if within the left boundary
                self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.update_sprite()
            if self.x + self.width + self.speed <= global_constants.SCREEN_WIDTH:  # Check if within the right boundary
                self.x += self.speed
        if keys[pygame.K_UP]:
            self.update_sprite()
            if self.y - self.speed >= 0:  # Check if within the top boundary
                self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.update_sprite()
            if self.y + self.height + self.speed <= global_constants.SCREEN_HEIGHT:  # Check if within the bottom boundary
                self.y += self.speed


class NPC(Character):
    def __init__(self, sprite_paths, x, y):
        super().__init__(50, 50, 0, sprite_paths)
        self.x = x
        self.y = y

    def handle_input(self, player):
        if (((self.x - player.x) ** 2 + (self.y - player.y) ** 2) ** 0.5 <= 20):
           #initiaze dialouge 
           return True
        else: return False