import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))  # Blue color for the character
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = 5
        self.jump_speed = 16  # Increased jump speed for better responsiveness
        self.gravity = 0.8  # Adjusted gravity for smoother falling
        self.vel_y = 0
        self.is_jumping = False
        self.start_pos = pos  # Save the starting position
        self.space_pressed = False  # Track if spacebar is pressed

    def update(self, keys_pressed, platforms):
        # Apply gravity
        if not self.is_jumping:
            self.vel_y += self.gravity

        # Horizontal movement
        if keys_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Jumping
        if not self.space_pressed and keys_pressed[pygame.K_SPACE] and not self.is_jumping:
            self.space_pressed = True
            self.is_jumping = True
            self.vel_y = -self.jump_speed

        # Check if spacebar is released
        if not keys_pressed[pygame.K_SPACE]:
            self.space_pressed = False

        # Update vertical position
        self.rect.y += self.vel_y

        # Check for collision with platforms
        platform_collision = pygame.sprite.spritecollideany(self, platforms)
        if platform_collision:
            if self.vel_y > 0:
                self.rect.bottom = platform_collision.rect.top
                self.vel_y = 0
                self.is_jumping = False

        # Debug prints to understand the state
        print(f"pos: {self.rect.topleft}, vel_y: {self.vel_y}, is_jumping: {self.is_jumping}, space_pressed: {self.space_pressed}")
