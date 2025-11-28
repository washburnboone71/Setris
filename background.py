
import pygame
from util_params import WIDTH, HEIGHT 

def make_background():
    
    
    MAX_BLACK_X = 687 
    GRID_SPACING = 56 #the size of the grid squares in pixels
    LINE_COLOR = (130, 130, 130) #color for the grid line
    SURFACE_COLOR = (150, 130, 60) #color of brownish surface
    SCREENS_COLOR = (20,20,20)
    background = pygame.Surface((WIDTH,HEIGHT))

    #fill entire background)
    background.fill(SURFACE_COLOR) 

    #create all mini screens in the background
    MAIN_SCREEN_RECT = pygame.Rect(15, 15, MAX_BLACK_X-15, HEIGHT-30)
    INDEX_SCREEN_RECT = pygame.Rect(712, 15, 263, 570)
    TIME_SCREEN_RECT = pygame.Rect(712, 605, 148, 80)
    LEVEL_SCREEN_RECT = pygame.Rect(885, 605 , 90 , 80 )

    # draw black square
    pygame.draw.rect(background,SCREENS_COLOR, MAIN_SCREEN_RECT, border_radius=25)
    pygame.draw.rect(background,SCREENS_COLOR, INDEX_SCREEN_RECT, border_radius=25)
    pygame.draw.rect(background,SCREENS_COLOR, TIME_SCREEN_RECT, border_radius=25)
    pygame.draw.rect(background,SCREENS_COLOR, LEVEL_SCREEN_RECT, border_radius=25)

    for x in range(MAIN_SCREEN_RECT.left, MAIN_SCREEN_RECT.right, GRID_SPACING):
        start_point = (x, MAIN_SCREEN_RECT.top)
        end_point = (x, MAIN_SCREEN_RECT.bottom-1)
        pygame.draw.line(background, LINE_COLOR, start_point, end_point, 2)

    # Start at the top edge of the rect and step by GRID_SPACING until the bottom edge
    for y in range(MAIN_SCREEN_RECT.top, MAIN_SCREEN_RECT.bottom, GRID_SPACING):
        start_point = (MAIN_SCREEN_RECT.left, y)
        end_point = (MAIN_SCREEN_RECT.right-1, y)
        pygame.draw.line(background, LINE_COLOR, start_point, end_point, 2)
    
    #draw 2 lines to cover the two sticking through the edges
    pygame.draw.line(background, (SURFACE_COLOR), (15,15), (700, 15), 2)
    pygame.draw.line(background, (SURFACE_COLOR), (15,15), (15, 685), 2)

    
            
    # return the background surface
    return background
def game_over():
    background = pygame.Surface((WIDTH,HEIGHT))
    game_over_location = 'Game_Over.png'
    game_over_image = pygame.image.load(game_over_location).convert_alpha()
    scaled_game_over_screen = pygame.transform.scale(game_over_image, (WIDTH, HEIGHT))

    background.blit(scaled_game_over_screen, (0,0))
    return background