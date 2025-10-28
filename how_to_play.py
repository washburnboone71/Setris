import pygame
from random import randint
from util_params import WIDTH, HEIGHT

def how_to_play():

    background = pygame.Surface((WIDTH,HEIGHT))
    how_to_play_location = 'how_to_play.png'
    how_to_play_image = pygame.image.load(how_to_play_location).convert_alpha()

    #scale the drawing
    scaled_how_to_play_screen = pygame.transform.scale(how_to_play_image, (WIDTH, HEIGHT-100))

    #background.blit(scaled_start_screen, (0,37))

    background.blit(scaled_how_to_play_screen, (0,37))

    
    return background

def how_to_play_X():

    background = pygame.Surface((WIDTH,HEIGHT))
    how_to_play_X_location = 'how_to_play_x.png'
    how_to_play_X_image = pygame.image.load(how_to_play_X_location).convert_alpha()

    #scale the drawing
    scaled_how_to_play_X_screen = pygame.transform.scale(how_to_play_X_image, (WIDTH, HEIGHT-100))

    #background.blit(scaled_start_screen, (0,37))

    background.blit(scaled_how_to_play_X_screen, (0,37))

    
    return background