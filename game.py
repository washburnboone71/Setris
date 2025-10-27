import pygame
from util_params import *
from background import *
from start_screen import *

game_started = False
TRIGGER_AREA_PLAY = pygame.Rect(0, 475, WIDTH // 4, HEIGHT // 4)
TRIGGER_AREA_QUESTION = pygame.Rect(800, 475, 150, HEIGHT // 4)
# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

# make background
First_background = start_screen()
Second_background = make_background()

play_background = start_screen_play_selected()
question_background = start_screen_question_selected()

Current_background = []

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

    #get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos() 
    is_hovering_play = TRIGGER_AREA_PLAY.collidepoint(mouse_x, mouse_y)  
    is_hovering_question = TRIGGER_AREA_QUESTION.collidepoint(mouse_x, mouse_y)
    #use game state to determine screen
    if game_started:
        screen.blit(Second_background, (0,0))
        

    else:
        if is_hovering_play:
            screen.blit(play_background, (0,0))
            
            if event.type == pygame.MOUSEBUTTONUP:
                game_started = True

        elif is_hovering_question:
            screen.blit(question_background, (0,0))
            
        else:
            screen.blit(First_background, (0, 0))
            

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()


