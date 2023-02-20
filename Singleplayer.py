import sys
import pygame

# Resolution
WIDTH = 1020
HEIGHT = 750

ROWS = 15
COLS = 15
SQUARE_SIZE = WIDTH // COLS

LINE_WIDTH = 15

#Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)

# PyGame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mouseketeers")
screen.fill(BG_COLOR)

class Game:
    
    def __init__(self):
        self.show_lines()
    
    def show_lines(self):
        
        # Vertical
        pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - SQUARE_SIZE, 0), (WIDTH - SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - 2*SQUARE_SIZE, 0), (WIDTH - 2*SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - 3*SQUARE_SIZE, 0), (WIDTH - 3*SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - 4*SQUARE_SIZE, 0), (WIDTH - 4*SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - 5*SQUARE_SIZE, 0), (WIDTH - 5*SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - 6*SQUARE_SIZE, 0), (WIDTH - 6*SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - 7*SQUARE_SIZE, 0), (WIDTH - 7*SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - 8*SQUARE_SIZE, 0), (WIDTH - 8*SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - 9*SQUARE_SIZE, 0), (WIDTH - 9*SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - 10*SQUARE_SIZE, 0), (WIDTH - 10*SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - 11*SQUARE_SIZE, 0), (WIDTH - 11*SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - 12*SQUARE_SIZE, 0), (WIDTH - 12*SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (WIDTH - 13*SQUARE_SIZE, 0), (WIDTH - 13*SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        
        # Horizontal
        pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQUARE_SIZE), (WIDTH, HEIGHT - SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - 2*SQUARE_SIZE), (WIDTH, HEIGHT - 2*SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - 3*SQUARE_SIZE), (WIDTH, HEIGHT - 3*SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - 4*SQUARE_SIZE), (WIDTH, HEIGHT - 4*SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - 5*SQUARE_SIZE), (WIDTH, HEIGHT - 5*SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - 6*SQUARE_SIZE), (WIDTH, HEIGHT - 6*SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - 7*SQUARE_SIZE), (WIDTH, HEIGHT - 7*SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - 8*SQUARE_SIZE), (WIDTH, HEIGHT - 8*SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT - 9*SQUARE_SIZE), (WIDTH, HEIGHT - 9*SQUARE_SIZE), LINE_WIDTH)


def main():
    
    # Object
    game = Game()
    
    while True:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()
main()