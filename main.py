import pygame
import character_classes
from dialogue import Dialogue, DialogueManager
import mini_1, mini_2, mini_3, mini_4, mini_5, mini_6, mini_7, mini_8, mini_9, mini_10, mini_11, mini_12, mini_13, mini_14, mini_15
import global_constants
import sys
import time

# Scenes
scenes = {
    1: mini_1.menu,
    2: mini_2.menu,
    3: mini_5.menu,
    4: mini_4.menu,
    5: mini_6.menu,
    6: mini_3.menu,
    7: mini_7.menu,
    8: mini_8.menu,
    9: mini_9.menu,
    # 10: mini_10.menu,
    # 11: mini_11.menu,
    # 12: mini_12.menu,
    # 13: mini_13.menu,
    # 14: mini_14.menu,
    # 15: mini_15.menu,
} #etc

# Global Constants
playedLevel = False
mini_level = 0

# Game Loop
def main():
    global playedLevel, mini_level

    # Initialize Pygame
    pygame.init()

    # Set up the screen
    screen = pygame.display.set_mode((global_constants.SCREEN_WIDTH, global_constants.SCREEN_HEIGHT))
    pygame.display.set_caption("The Missing Sock")

    # Set up the player
    player = character_classes.Player(['./sprites/mainsock-1.png'])
    socks = [
        character_classes.NPC(['./sprites/sidesock1-1.png', './sprites/sidesock1-2.png'], 400, 20),
        character_classes.NPC(['./sprites/sidesock2-1.png', './sprites/sidesock2-2.png'], 300, 120),
        character_classes.NPC(['./sprites/sidesock3-1.png', './sprites/sidesock3-2.png'], 240, 180),
        character_classes.NPC(['./sprites/sidesock4-1.png', './sprites/sidesock4-2.png'], 300, 320),
        character_classes.NPC(['./sprites/sidesock5-1.png', './sprites/sidesock5-2.png'], 400, 420),
        character_classes.NPC(['./sprites/sidesock6-1.png', './sprites/sidesock6-2.png'], 464, 326),
        character_classes.NPC(['./sprites/sidesock7-1.png', './sprites/sidesock7-2.png'], 500, 320),
        character_classes.NPC(['./sprites/sidesock8-1.png', './sprites/sidesock8-2.png'], 550, 220)
    ]

    # Create dialogue instance
    dialogue_manager = DialogueManager()
    current_dialogue = dialogue_manager.activateDialogue()
    current_dialogue.started = True
    current_dialogue.is_active = True

    start_dialogue = Dialogue(["[Press Space To Talk]"])
    current_dialogue.started = True

    def checkSocks():
        for index, sock in enumerate(socks):
            if sock.handle_input(player):
                if not current_dialogue.is_active:
                    return (True, index)

        return (False, -1)

    foundSocks = (False, -1)

    pygame.mixer.init()
    pygame.mixer.music.load("./music/Eli-Game-2-Song.ogg") 
    pygame.mixer.music.play(-1,0.0)

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    if current_dialogue.is_active and not current_dialogue.done:
                        current_dialogue.next_line()
                    elif not current_dialogue.is_active and foundSocks[0]:
                        current_dialogue = dialogue_manager.activateDialogue()
                        current_dialogue.is_active = True
                        playedLevel = False

        # check if dialogue is done
        if current_dialogue.done and playedLevel == False and dialogue_manager.dialogue_index % 2 == 0:
            if (mini_level > 9):
                pass
            elif (mini_level + 1 == 1 
                  or mini_level + 1 == 7 
                  or mini_level + 1 == 10 
                  or mini_level + 1 == 11
                  or mini_level + 1 == 12 
                  or mini_level + 1 == 14 
                  or mini_level + 1 == 15 
                  or mini_level + 1 == 13):
                scenes[mini_level + 1](0)
                time.sleep(0.8)
            else:
                scenes[mini_level + 1]()
            
            socks.remove(socks[foundSocks[1]])
            mini_level += 1
            playedLevel = True
            current_dialogue = dialogue_manager.activateDialogue()
            current_dialogue.is_active = True

        if current_dialogue.is_active == False and foundSocks[0]:
            start_dialogue.is_active = True
        else:
            start_dialogue.is_active = False

        foundSocks = checkSocks()

        # Handle player movement
        player.handle_input()
        
        # Update the screen
        screen.fill((255, 255, 255))

        for sock in socks: # Rendering the socks
            sock_sprite = sock.get_current_sprite()
            screen.blit(sock_sprite, (sock.x, sock.y))

        current_sprite = player.get_current_sprite()
        screen.blit(current_sprite, (player.x, player.y))

        if current_dialogue.is_active:  # Render the dialogue
            current_dialogue.render(screen) 

        if start_dialogue.is_active:
            start_dialogue.render(screen) 

        pygame.display.flip()

        # Limit the frame rate
        pygame.time.Clock().tick(60)

main()