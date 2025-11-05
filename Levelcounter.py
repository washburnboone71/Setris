import pygame
from background import*
import time
from util_params import*



class Levelcounter:

    def __init__(self, font_path, font_size, color, start_position):
        self.count = 0 #initial level
        self.color = color
        self.position = start_position
        self.font = pygame.font.Font(font_path, font_size)
        self.update_surface()
        
        

    def increment(self):
        self.count += 1
        self.update_surface()

    def update_surface(self):
        text_to_blit = str(self.count)
        self.text_surface = self.font.render(text_to_blit, True, self.color)
        self.text_rect = self.text_surface.get_rect(topleft=self.position)

    def blit(self, screen: pygame.surface):
        screen.blit(self.text_surface, self.text_rect)
        
    

