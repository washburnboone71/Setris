import pygame
from util_params import *

class IndexShape:
    
    
    def __init__(self, image_path, initial_pos, correct_grid_coords, scale_factor, index_scale_factor):
       
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.scale_factor = scale_factor
        self.index_scale_factor = index_scale_factor

        self.current_scale = index_scale_factor
        self._update_image_size()

        self.rect = self.image.get_rect(topleft=initial_pos)
        self.original_pos = initial_pos
        self.is_dragging = False
        self.is_placed = False #true when piece is placed in correct position
        
        self.correct_grid_coords = correct_grid_coords 

        self.offset_x = 0
        self.offset_y = 0



    def _update_image_size(self):
        """Helper method to resize the image based on current scale"""
        new_width = int(self.original_image.get_width() * self.current_scale)
        new_height = int(self.original_image.get_height() * self.current_scale)
        self.image = pygame.transform.scale(self.original_image, (new_width, new_height))

    def _resize_piece(self, new_scale):
        """Resize the piece and adjust position to keep it centered"""
        # Store the center position
        center = self.rect.center
        
        # Update scale and image
        self.current_scale = new_scale
        self._update_image_size()
        
        # Update rect with new image, keeping the center position
        self.rect = self.image.get_rect(center=center)

    #drag and dropping pieces
    def handle_event(self, event):      
        #if mouse is down 
        if event.type == pygame.MOUSEBUTTONDOWN:
            #if mouse is on piece
            #grabing piece
            if self.rect.collidepoint(event.pos) and not self.is_placed:
                self.is_dragging = True
                self._resize_piece(self.scale_factor)
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
                    self._resize_piece(self.index_scale_factor)
                    self.rect.topleft = self.original_pos

        #dragging            
        elif event.type == pygame.MOUSEMOTION:
            if self.is_dragging:
                
                self.rect.x = event.pos[0] + self.offset_x
                self.rect.y = event.pos[1] + self.offset_y



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
    def is_correctly_placed(self):
        current_coords = self.get_current_grid_coords()
        if current_coords:
            return current_coords in self.correct_grid_coords
        return False 


    #blits shape
    def draw(self, surface):
        surface.blit(self.image, self.rect)

