import pygame

class Interactable(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))  # Red color for the interactable object
        self.rect = self.image.get_rect(topleft=pos)

    def interact(self):
        print("Interacted with the object!")
