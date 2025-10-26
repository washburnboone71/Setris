import pygame
from util_params import *
from background import *
from start_screen import *

game_started = False

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# make background
First_background = start_screen()
Second_background = make_background()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER YOUR GAME HERE
    if event.type == pygame.KEYUP:

        if event.key == pygame.K_RETURN: #k_return is = to enter
            
            game_started = True
    
    #use game state to determine screen
    if game_started:
        screen.blit(Second_background, (0,0))
    else:
        screen.blit(First_background, (0,0))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()