import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_HEIGHT = 1024
WINDOW_WIDTH = 768

background_colour = (0, 0, 0)

screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Mouseketeers')
screen.fill(background_colour)

pygame.display.flip()

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

running = True
while running:
    drawGrid()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    
def drawGrid():
    blockSize = 20
    for x in range (0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)