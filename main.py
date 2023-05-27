import pygame
import character_classes
import global_constants
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((global_constants.SCREEN_WIDTH, global_constants.SCREEN_HEIGHT))
pygame.display.set_caption("Top-Down Movement")

# Set up the player
player = character_classes.Player([''])

# Game Loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle player movement
    player.handle_input()

    # Update the screen
    screen.fill((0, 0, 0))
    current_sprite = player.get_current_sprite()
    screen.blit(current_sprite, (player.x, player.y))
    pygame.display.flip()

    # Limit the frame rate
    pygame.time.Clock().tick(60)