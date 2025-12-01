import pygame
from util_params import *

class IndexShape:
    
    
    def __init__(self, image_path, initial_pos, correct_grid_coords, scale_factor, index_scale_factor):
       
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.scale_factor = scale_factor
        self.index_scale_factor = index_scale_factor

        self.current_scale = index_scale_factor
        self.rotation_angle = 0
        self.update_image()

        self.rect = self.image.get_rect(topleft=initial_pos)
        self.original_pos = initial_pos
        self.is_dragging = False
        self.is_placed = False #true when piece is placed in correct position
        
        self.correct_grid_coords = correct_grid_coords 

        self.offset_x = 0
        self.offset_y = 0



    def update_image(self):
        new_width = int(self.original_image.get_width() * self.current_scale)
        new_height = int(self.original_image.get_height() * self.current_scale)
        scaled_image = pygame.transform.scale(self.original_image, (new_width, new_height))
        self.image = pygame.transform.rotate(scaled_image, self.rotation_angle)

    def resize_piece(self, new_scale):
        #store the center position
        center = self.rect.center
        
        #update scale and image
        self.current_scale = new_scale
        self.update_image()
       
        self.rect = self.image.get_rect(center=center)

    def rotate(self):
        center = self.rect.center
        self.rotation_angle = (self.rotation_angle - 90) % 360
        self.update_image()
        self.rect = self.image.get_rect(center=center)

    #drag dropping and rotating pieces
    def handle_event(self, event):      
        #if mouse is down 
        if event.type == pygame.MOUSEBUTTONDOWN:
            #if mouse is on piece
            #grabing piece
            if self.rect.collidepoint(event.pos) and not self.is_placed:
                self.is_dragging = True
                self.resize_piece(self.scale_factor)
                # calc offset from clicked point
                self.offset_x = self.rect.x - event.pos[0]
                self.offset_y = self.rect.y - event.pos[1]

        #if mousbutton goes up       
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.is_dragging:
                self.is_dragging = False
                
                #check if dropping outsiode main area
                main_area_check = pygame.Rect(MAIN_AREA_X, MAIN_AREA_Y, MAIN_AREA_WIDTH, MAIN_AREA_HEIGHT)
                if main_area_check.colliderect(self.rect):
                    #snap to grid position
                    snapped_pos = self.snap_to_grid(self.rect.topleft)
                    self.rect.topleft = snapped_pos
                else:
                    #if dropped outside go to orignal position
                    self.resize_piece(self.index_scale_factor)
                    self.rect.topleft = self.original_pos

        #dragging            
        elif event.type == pygame.MOUSEMOTION:
            if self.is_dragging:
                
                self.rect.x = event.pos[0] + self.offset_x
                self.rect.y = event.pos[1] + self.offset_y

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and self.is_dragging:
                self.rotate()
                #calc offset after roation
                self.offset_x = self.rect.x - pygame.mouse.get_pos()[0]
                self.offset_y = self.rect.y - pygame.mouse.get_pos()[1]


    #snaps piece to nearest grid cell
    def snap_to_grid(self, current_pos):
        #get position relative to (15,15)
        rel_x = current_pos[0] - MAIN_AREA_X
        rel_y = current_pos[1] - MAIN_AREA_Y
        
        #get the grid cordinates
        grid_x = round(rel_x / GRID_SPACING)
        grid_y = round(rel_y / GRID_SPACING)
        
        #convert grid back to pixel
        snapped_x = grid_x * GRID_SPACING + MAIN_AREA_X +1
        snapped_y = grid_y * GRID_SPACING + MAIN_AREA_Y +1
        
        return (snapped_x,snapped_y)


    #calc the grid posistion of piece in the main area
    def get_current_grid_coords(self):
        #check if piece is in main area
        if self.rect.x >= MAIN_AREA_X and self.rect.y >= MAIN_AREA_Y:
            #true position
            rel_x = self.rect.x - MAIN_AREA_X -1
            rel_y = self.rect.y - MAIN_AREA_Y -1
            #simplify into grid position
            grid_x = rel_x // GRID_SPACING
            grid_y = rel_y // GRID_SPACING
            return (grid_x, grid_y)
        return None #not in the main area


    #checks if piece is on its correct cordinate
    def correctly_placed(self):
        current_coords = self.get_current_grid_coords()
        if current_coords:
            return current_coords in self.correct_grid_coords
        return False 


    #blits shape
    def draw(self, surface):
        surface.blit(self.image, self.rect)

