import pygame

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Sprite")

clock = pygame.time.Clock()

# Load your sprite
import os
print(os.getcwd())
sprite = pygame.image.load("images-removebg-preview.png").convert_alpha()

# Starting position
x = 100
y = 100

# Speed (pixels per frame)
dx = 8
dy = 9

# Get sprite size
sprite_rect = sprite.get_rect()

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the sprite
    x += dx
    y += dy

    # Bounce off left/right walls
    if x <= 0 or x + sprite_rect.width >= WIDTH:
        dx = -dx

    # Bounce off top/bottom walls
    if y <= 0 or y + sprite_rect.height >= HEIGHT:
        dy = -dy

    # Draw everything
    screen.fill((30, 30, 30))  
    screen.blit(sprite, (x, y))

    pygame.display.flip()
    clock.tick(100)  # 100 FPS

