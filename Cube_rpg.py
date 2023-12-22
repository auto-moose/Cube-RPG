# Import modules.
import pygame

# Setup Pygame
pygame.init()

# Creates window
screen = pygame.display.set_mode([1500, 850])


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (255, 0, 0), (50, 50, 50, 50), 0)

    pygame.display.flip()

pygame.quit()