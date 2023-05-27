import pygame
import global_constants

class DialogueManager():
    def __init__(self):
        self.dialogue_index = 0
        
    def activateDialogue(self):
        return Dialogue(self.pickDialogue())

    def pickDialogue(self):
        dialogueList = [
            [
                "[Thoughts]: Where am I? *Press Space to Continue*",
                "[Thoughts]: WAIT! Where is Georgina? How can I be a sock with no matching sock!",
                "[Thoughts]: Well I better get looking before Georgina gets lost, or worse gets sucked into that VOID...",
                "[Thoughts]: Laundry machines...",
                "[Thoughts]: Wait. Why can't I move?",
                "[Thoughts]: Oh, it's arrow keys. You would think at least WASD would work...",
            ],
            [
                "I totally saw Georgina moments ago! She's in there!",
                "Or not! I might have lied.",
                "Hope you have fun with the minigame, though!"
            ],
            [
                "[Thoughts]: Well that was weird..."
            ],
            [
                "What? Georgina?", 
                "GEORGINA'S MINE! BACK OFF!",
                "YOU'LL NEVER FIND HER!"
            ],
            [
                "[Thoughts]: So aggressive!"
            ],
            [
                "No, I haven't seen Georgina, but did you see Taylor Swift last week?",
                "She wanted to shake it off and sock it to me with her fashion sense :)",
                "Ok, bye bye now!"
            ],
            [
                "[Thoughts]: What a fan!"
            ],
            [
                "Sorry, who?",
                "Georgia?",
                "Who's Georgia?",
                "Could you speak a little louder?",
                "George?",
                "Oh well, good luck finding George!"
            ],
            [
                "[Thoughts]: Hm... I thought I spoke clearly enough..."
            ],
            [
                "I once knew a Georgina..."
            ],
            [
                "[Thoughts]: Did you now?"
            ],
            [
                "Oh, yeah, she should be right in there!",
                "You must have missed her.",
                "You should go in again!",
                "You can't? Well, I'll go in once you come out!",
                "If I'm not back in 10 seconds, tell Tayler Swift I love her."
            ],
            [
                "[Thoughts]: I'm so glad he's helping me! Hopefully he comes back!"
            ],
            [
                "Quien es esta Georgina que hablas bien? Es ella una lavadora?",
                "Asquerosa bestia sockish, vete!"
            ],
            [
                "[Thoughts]: Espero que te guste nuestro juego!"
            ],
            [
                "...",
                "...",
                "...",
                "...",
                "...",
                "...",
                "...",
                "...",
                "...",
                "...",
                "...",
                "...",
                "...",
                "...",
                "BOO!"
            ],
            [
                "[Thoughts]: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHH"
            ],
            [
                "I'm Georgina!",
                "You found me!",
                "Wow, you found me!",
                "Just kidding, you're trapped here...",
                "FOREVER!",
                "Go play your games little sock...",
                "I'll be coming for you next. So get Lost little one!"
            ]]
        index = self.dialogue_index
        self.dialogue_index += 1
        return dialogueList[index]

class Dialogue():
    def __init__(self, dialogue_text):
        self.font = pygame.font.Font(None, 28)
        self.dialogue = dialogue_text
        self.dialogue_index = 0
        self.is_active = False
        self.line_width = 75

        self.started = False
        self.done = False

    def next_line(self):
        self.started = True
        self.is_active = True
        self.dialogue_index += 1
        if self.dialogue_index >= len(self.dialogue):
            self.is_active = False
            self.done = True

    def render(self, surface):
        if self.is_active:
            text_lines = self.wrap_text(self.dialogue[self.dialogue_index], self.line_width)
            for i, line in enumerate(text_lines):
                text = self.font.render(line, True, (0, 0, 0))
                text_rect = text.get_rect(center=(global_constants.SCREEN_WIDTH // 2, global_constants.SCREEN_HEIGHT - len(text_lines) * 30 + i * 30))
                surface.blit(text, text_rect)

    @staticmethod
    def wrap_text(text, line_width):
        words = text.split(" ")
        wrapped_lines = []
        current_line = ""
        for word in words:
            if len(current_line) + len(word) <= line_width:
                current_line += word + " "
            else:
                wrapped_lines.append(current_line.strip())
                current_line = word + " "
        if current_line:
            wrapped_lines.append(current_line.strip())
        return wrapped_lines
    