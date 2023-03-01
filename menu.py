import pygame
import sys
from button import Button

WIDTH = 720
HEIGHT = 720
PURPLE = "#7600bc"

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Main menu")

bg = pygame.image.load("src/background.png")

def get_font(size):
    
    return pygame.font.Font("src/font.ttf")
    
def singleplayer():
    
    global SCREEN, CLOCK
    SCREEN = pygame.display.set_mode((720, 720))
    CLOCK = pygame.time.Clock()
    screen.fill("#7600bc")
    
    while True:
        
        singleplayer_mouse_pos = pygame.mouse.get_pos()
        drawGrid()
        
        
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if singleplayer_back.checkForInput(singleplayer_mouse_pos):
                    
                    main_menu()
                    
    pygame.display.update()
    
def drawGrid ():
    
    blockSize = 20
    for x in range (0, WIDTH, blockSize):
        
        for y in range (0, HEIGHT, blockSize):
            
            rect = pygame.rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, PURPLE, rect, 1)
        

def multiplayer():
    
    while True:
        
        multiplayer_mouse_pos = pygame.mouse.get_pos()
        
        screen.fill("cyan")
        
        
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if multiplayer_back.checkForInput(multiplayer_mouse_pos):
                    
                    main.menu()
 
     pygame.display.update()
     
def challange():
    
    while True:
        
        challange_mouse_pos = pygame.mouse.get_pos()
        
        screen.fill("cyan")
        
        
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if challange_back.checkForInput(challange_mouse_pos):
                    
                    main_menu()
                    
    pygame.display.update()

def main_menu():
    
    pygame.display.set_caption("Main menu")
    
    while True:
        
        screen.blit(bg, (0, 0))
        
        menu_mouse_pos = pygame.mouse.get_pos()
        
        menu_text = get_font(100).render("Main menu", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(640, 100))
        
        singleplayer_button = Button(image=None, pos=(640, 250),
                                     text_input="Singleplayer", font=get_font(75), base_color="#d7fcd4", hovering_color="white")
        multiplayer_button = Button(image=None, pos=(640, 400),
                                    text_input="Multiplayer", font=get_font(75), base_color="#d7fcd4", hovering_color="white")
        challange_button = Button(image=None, pos=(640, 550),
                                  text_input="Challange", font=get_font(75), base_color="#d7fcd4", hovering_color="white")
        
        screen.blit(menu_text, menu_rect)
        
        for Button in [singleplayer_button, multiplayer_button, challange_button]:
            
            button.changeColor(menu_mouse_pos)
            button.update(screen)
            
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if singleplayer_button.checkForInput(menu_mouse_pos):
                    singleplayer()
                if multiplayer_button.checkForInput(menu_mouse_pos):
                    multiplayer()
                if challange_button.checkForInput(menu_mouse_pos):
                    challange()
                    
        pygame.display.update()
    
main_menu()