import pygame
from character import Character
from environment import Environment
from interactable import Interactable
from platforms import Platform, Pit

pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Metroidvania Example")

# Creating sprite groups
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
interactables = pygame.sprite.Group()

# Creating instances of the character, environment, and interactable objects
character = Character((100, 500))  # Start character on a platform
environment = Environment((0, 0), (800, 600))
platform1 = Platform((50, 550), (200, 10))
platform2 = Platform((300, 450), (200, 10))
platform3 = Platform((550, 350), (200, 10))
interactable = Interactable((400, 300))
pit = Pit((100, 500))  # Set reset position to the starting platform

# Adding sprites to the groups
all_sprites.add(environment)
all_sprites.add(character)
all_sprites.add(platform1)
all_sprites.add(platform2)
all_sprites.add(platform3)
all_sprites.add(interactable)
platforms.add(platform1)
platforms.add(platform2)
platforms.add(platform3)
interactables.add(interactable)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys_pressed = pygame.key.get_pressed()
    character.update(keys_pressed, platforms)

    # Check for pit
    pit.check_pit(character)

    # Check for interactions
    if pygame.sprite.spritecollideany(character, interactables):
        interactable.interact()

    # Drawing
    screen.fill((0, 0, 0))  # Clear screen with black
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

# jacob should ask out the girl from the coffee shop cuz he is cute
