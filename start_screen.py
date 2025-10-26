#code for starting screen
import pygame
from random import randint
from util_params import WIDTH, HEIGHT


def start_screen():

    background = pygame.Surface((WIDTH,HEIGHT))
    background.fill((63,63,63))

    # get start screen image and define it
    start_screen_location = 'start_screen.png'
    start_screen_image = pygame.image.load(start_screen_location).convert_alpha()

    #scale the drawing
    scaled_start_screen = pygame.transform.scale(start_screen_image, (WIDTH, HEIGHT-75))

    background.blit(scaled_start_screen, (0,37))

    #return the backgorund
    return background

    