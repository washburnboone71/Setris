import pygame
from util_params import *
from background import *
from start_screen import *
from random import randint
from how_to_play import *
from Levelcounter import *
from shapes import *
# pygame setup
pygame.init()


#music setup
pygame.mixer.init()
music_file = ['Moog_city_2.mp3','Sweden.mp3','Subwoofer_Lullaby.mp3']
pygame.mixer.music.load(music_file[randint(0,2)])
pygame.mixer.music.play(-1)


# sound setup
sound = 'click_sound.ogg'
click_sound = pygame.mixer.Sound(sound)


#set width and height of screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#declare clock
clock = pygame.time.Clock()


#pygame is running once the code is run
running = True
#game doesn't start until you press 'play' or enter
game_started = False
# is showing help screen is set to show when you click '?'
is_showing_help = False


# background items
First_background = start_screen()
Second_background = make_background()
play_background = start_screen_play_selected()
question_background = start_screen_question_selected()
how_to_play_background = how_to_play()
how_to_play_X_background = how_to_play_X()


#declare areas for on screen buttons
FULLSCREEN = pygame.Rect(0, 0, WIDTH, HEIGHT)
TRIGGER_AREA_PLAY = pygame.Rect(0, 475, WIDTH // 4, HEIGHT // 4)
TRIGGER_AREA_QUESTION = pygame.Rect(800, 475, 150, HEIGHT // 4)
TRIGGER_AREA_QUESTION_X = pygame.Rect(900, 50, 100, 100)

#create instance of the level
level_display = Levelcounter('ka1.ttf', 50, (255,255,255), (905, 615))

while running:
    
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER YOUR GAME HERE
    if event.type == pygame.KEYUP:

        #if enter is pressed start the game
        if event.key == pygame.K_RETURN: #k_return is = to enter
            game_started = True


        #if escape is pressed while on the how to play screen go back to orignal start screen
        if event.key == pygame.K_ESCAPE and is_showing_help:
            is_showing_help = False

    
    #declare requirements for hovering a button
    mouse_x, mouse_y = pygame.mouse.get_pos()
    is_hovering_play = TRIGGER_AREA_PLAY.collidepoint(mouse_x, mouse_y)  
    is_hovering_question = TRIGGER_AREA_QUESTION.collidepoint(mouse_x, mouse_y)
    is_hovering_question_X = TRIGGER_AREA_QUESTION_X.collidepoint(mouse_x, mouse_y)
    
    is_carried = False

    if game_started:
        screen.blit(Second_background, (0,0))
        level_display.blit(screen)
        

    elif is_showing_help:
        screen.blit(how_to_play_background, (0,0))
        if is_hovering_question_X:
            screen.blit(how_to_play_X_background, (0,0))    
            if event.type == pygame.MOUSEBUTTONUP:
                is_showing_help = False

    else:
        if is_hovering_play:
            screen.blit(play_background, (0,0))
            
            if event.type == pygame.MOUSEBUTTONUP:
                game_started = True
                click_sound.play()

        elif is_hovering_question:
            screen.blit(question_background, (0,0))
    

            if event.type == pygame.MOUSEBUTTONUP:
                is_showing_help = True
                

            
        else:
            screen.blit(First_background, (0, 0))
    

    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()


