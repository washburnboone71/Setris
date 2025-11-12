import pygame
import time



class Levelcounter:
   
    def __init__(self, font_path, font_size, color, level_position, timer_position):
        
        #set initial values
        self.count = 1  
        self.color = color
        self.start_time_ms = None
        self.paused_time_ms = 0
        self.is_running = False
        self.has_started = False
        self.timer_position = timer_position
        self.level_position = level_position
        
        self.font = pygame.font.Font(font_path, font_size)
        
        self.timer_surface = self.render_timer_text('0:00')
        self.level_surface = self.render_level_text()


    def render_timer_text(self, time_text):
        return self.font.render(f"{time_text}", True, self.color)
    
    def render_level_text(self):
        level_blit = f"{self.count}"
        return self.font.render(level_blit, True, self.color)
    


    def start_timer(self):
        #starts the timer
        if not self.is_running:
            self.start_time_ms = pygame.time.get_ticks() - self.paused_time_ms
            self.is_running = True
            self.has_started = True

    def stop_timer(self): #for at the end when capturing players time
        if self.is_running:
            self.paused_time_ms = pygame.time.get_ticks() - self.start_time_ms
            self.is_running = False
    
    def get_ms(self):
        if self.is_running and self.start_time_ms is not None:
            return pygame.time.get_ticks() - self.start_time_ms
        else:
            return self.paused_time_ms
    
    def get_time_string(self):
        total_ms = self.get_ms()
        total_seconds = int(total_ms // 1000)
        minutes = int(total_seconds //60)
        seconds = int( total_seconds% 60)
        return f"{minutes:01d}:{seconds:02d}"



    def increment_level(self):
        self.count += 1
        self.level_surface = self.render_level_text()

    def update_and_blit_timer(self, screen:pygame.Surface):
        time_text = self.get_time_string()
        self.timer_surface = self.render_timer_text(time_text)
        self.timer_rect = self.timer_surface.get_rect(topleft=self.timer_position)
        screen.blit(self.timer_surface, self.timer_rect)

    
    def blit_level(self, screen:pygame.Surface):
        self.level_rect = self.level_surface.get_rect(topleft=self.level_position)
        screen.blit(self.level_surface, self.level_rect)

    
    def blit_both(self, screen: pygame.Surface):
        self.blit_level(screen)
        self.update_and_blit_timer(screen)