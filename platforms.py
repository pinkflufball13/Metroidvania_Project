import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill((139, 69, 19))  # Brown color for the platform
        self.rect = self.image.get_rect(topleft=pos)

class Pit:
    def __init__(self, reset_position):
        self.reset_position = reset_position

    def check_pit(self, character):
        if character.rect.top > 600:  # If character falls below the screen
            character.rect.topleft = self.reset_position
            character.vel_y = 0  # Reset vertical velocity
            character.is_jumping = False  # Allow jumping again
