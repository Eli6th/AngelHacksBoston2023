import os
import sys
import random
import pygame
from pygame import gfxdraw
 
class Player(object):
    X_POS = 18
    Y_POS = 18

    def __init__(self):
        self.image = pygame.image.load(os.path.join("Assets/Dino", "mainsock-1.png"))

        self.sock_rect = pygame.Rect(self.X_POS, self.Y_POS, 16, 16)
 
    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
 
    def move_single_axis(self, dx, dy):
        self.sock_rect.x += dx
        self.sock_rect.y += dy
        self.collision(dx, dy)
 
    def collision(self, dx, dy):
        for wall in walls:
            if self.sock_rect.colliderect(wall.rect):
                if dx > 0:
                    self.sock_rect.right = wall.rect.left
                if dx < 0:
                    self.sock_rect.left = wall.rect.right
                if dy > 0:
                    self.sock_rect.bottom = wall.rect.top
                if dy < 0:
                    self.sock_rect.top = wall.rect.bottom
 
 
class Wall(object):
 
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
 
 
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
 
 
pygame.display.set_caption("Get to the red square!")
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
 
clock = pygame.time.Clock()
walls = []
player = Player()
 
# Holds the level layout in a list of strings.
level = """
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
W                  W    W       WWW        W
W         WWWWWW   W    WWWW      W   WWW  W
W   WWWW       W   W            W W    W   W
W   W        WWWW  WWWWW     WWWW W    W   W
W  WW  WWWW            W  W  W  W      W   W
W   W     W W      W  WWWW  W          W   W
W   W     W   WWW WW   W  W            WWWWW
W   WWW WWW   W W  W   W  W                W
W     W   W   W W  W      W     WWWWWWW    W                                 
WWW   W   WWWWW W       WWWWWW        W    W                             
W W      WW        W                  W    W                                                          
W W   WWWW   WWW   WWW  WWWWWWWWWWW WWW    W                                                           
W     W       W         W         W   W    W                                                           
W                  W    W      W WW        W                                                           
W         WWWWWW   WWWWWW      W  WWWWW    W                                                           
W   WWWW       W       W                   W                                                           
W   W        WWWWWWWWWWWWW WWWWWW          W                                             
W WWW  WWWW        W  E  W                 W                                                           
W   W     W W      W     W    WW  W    WWWWW                                                           
W   W     W   WWWWWW     W    W   W    W   W                                                          
W   WWW WWW   W W  W W        WWWWW    W   W                                                           
W     W   W   W W  W W              WWWW   W                                                          
WWW   W   WWWWW W  WWW        W            W                                                           
W W      WW        W          W   WWW      W                                                           
W W   WWWW   WWW   W     W    W     W      W                                                           
W     W        W         W    W     W      W                                                           
W                  WWWWWWW WWWWWWWWWWW  WW W                                                           
W       WWWWWWWW   W          W            W                                                           
W   WWWW       W   W      W   W    WWWWWW  W                                                           
W   W        WWWW  WWWW WWW   WW           W                                                          
W WWW  WWWW                   W      W     W                                   
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
""".splitlines()[1:]
 
# Parse the level string above. W = wall, E = exit
x = y = 1
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 10, 10)
        x += 18
    y += 18
    x = 1
 
def menu(): 
    running = True
    while running:
        clock.tick(60)
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
    
        # Move the player if an arrow key is pressed
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.move(-2, 0)
        if key[pygame.K_RIGHT]:
            player.move(2, 0)
        if key[pygame.K_UP]:
            player.move(0, -2)
        if key[pygame.K_DOWN]:
            player.move(0, 2)
    
        if player.sock_rect.colliderect(end_rect):
            return

        # Draw the scene
        screen.fill((0, 0, 0))
        for wall in walls:
            pygame.draw.ellipse(screen, (0, 128, 64), wall.rect)
        pygame.draw.rect(screen, (255, 0, 0), end_rect)
        pygame.draw.rect(screen, (255, 200, 0), player.sock_rect)
        pygame.display.flip()
        clock.tick(360)
    return