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

    def blit_shapes(self):
        #make it a long if chain where if theres three shapes in the list of shapes it blits [0] in this specific place [1] in the place... make it a for loop though and then the next if loop will be for if there is 4 in the list of shapes

#not finished yet
#make the shape to make a png(i can easily just draw all three)
#make shapes 