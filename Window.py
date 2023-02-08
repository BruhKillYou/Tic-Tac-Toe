import pygame
import sys

background_colour = (0, 0, 0)

screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Mouseketeers')
screen.fill(background_colour)

pygame.display.flip()

running = True
while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()