import pygame
import time


class Levelcounter:
   
    def __init__(self, font_path, font_size, color, level_position, timer_position):
        
        #set initial values
        self.count = 1  
        self.elapsed_time_ms = 0 
        self.color = color

        self.timer_position = timer_position
        self.level_position = level_position
        
        self.font = pygame.font.Font(font_path, font_size)
        
        self.start_time = time.time()
        self.update_level_surface()
        self.update_timer_surface()


   


    def calc_time(self, ms):
        total_seconds = ms // 1000
        seconds = total_seconds % 60
        return seconds

        
    def timer(self):
        elapsed_seconds = time.time() - self.start_time #time since program was opened(changing) - time since program was opened(unchanging)
        self.elapsed_time_ms = int(elapsed_seconds * 1000)
        self.update_timer_surface() # imediatly goes to function


    def update_timer_surface(self):
        time_text = self.calc_time(self.elapsed_time_ms) # takes tje elasped time and turns it into seconds
        self.timer_surface = self.font.render(f"{time_text}", True, self.color) #render time onto screen
        self.timer_rect = self.timer_surface.get_rect(topleft=self.timer_position)


    def increment_level(self):
        self.count += 1
        self.update_level_surface()

    
    def update_level_surface(self):
        level_blit = f"{self.count}"
        self.level_surface = self.font.render(level_blit, True, self.color)
        self.level_rect = self.level_surface.get_rect(topleft=self.level_position)

    
    def blit(self, screen: pygame.Surface):
        screen.blit(self.timer_surface, self.timer_rect)
        screen.blit(self.level_surface, self.level_rect)
