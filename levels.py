import pygame
from util_params import *
from background import *
from start_screen import *
from random import randint
from how_to_play import *
from levelandtimer import *
from shapes import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))

Second_background = make_background()
level_display = Levelcounter('ka1.ttf', 50, (255,255,255), (905, 615))


class Level:
    def __init__(self, shape_to_make, shapes):
        self.shape_to_make = shape_to_make
        self.shapes = shapes

    def blit_shape_to_make(self):


#not finished yet
#make the shape to make a png(i can easily just draw all three)
#make shapes 