import pygame
from shape import *
from util_params import *
from levelandtimer import *
#class for each level

class Level:
    
    
    def __init__(self, target_image_path, piece_data): 


        #scale target
        self.original_target_image = pygame.image.load(target_image_path).convert_alpha()
        target_rect = self.original_target_image.get_rect()
        scaled_width = target_rect.width * 14
        scaled_height = target_rect.height * 14
        self.target_image = pygame.transform.scale(self.original_target_image, (scaled_width, scaled_height))
            

        #calculate center of main area
        main_area_center_x = MAIN_AREA_X + (MAIN_AREA_WIDTH/2) +1 #slight errors
        main_area_center_y = MAIN_AREA_Y + (MAIN_AREA_HEIGHT/2) +2 #slight errors
            
        
        #targets center is in the middle of the main area
        #have to make sure all pieces pngs center is in the center
        self.target_rect = self.target_image.get_rect(center=(main_area_center_x, main_area_center_y))
        

        #piece setup
        self.pieces = []
        # index pieces pos in index area
        initial_x = INDEX_AREA_X + 20 
        initial_y = INDEX_AREA_Y + 20 
        
        for i, data in enumerate(piece_data):
            #calc pos based on offset
            x_offset = data['initial_pos_offset'][0] * 100 #column spacing
            y_offset = data['initial_pos_offset'][1] * 120 #row spacing
            
            piece_pos = (initial_x + x_offset, initial_y + y_offset)
            
            shape = IndexShape(
                image_path=data['path'],
                initial_pos=piece_pos,
                correct_grid_coords=data['correct_grid'],
                scale_factor=14,
                index_scale_factor = 7
            )
            self.pieces.append(shape)
        
        self.is_completed = False


    #handles events for index pieces
    def handle_event(self, event):

        if self.is_completed:
            return
            
        for piece in self.pieces:
            piece.handle_event(event)
            
        #everytime mouse button is released check if the level is completed
        if event.type == pygame.MOUSEBUTTONUP:
            self.check_completion()
            
    def check_completion(self):
        #checks in level is finished
        if not self.is_completed:
            #goes to true if all are true inside  all()
            all_correct = all(piece.correctly_placed() for piece in self.pieces)
            
            if all_correct:
                #finishes level and print
                self.is_completed = True
                for piece in self.pieces:
                    piece.is_placed = True
                print("Level Complete")
                
                
        return self.is_completed

    def draw(self, surface):
        #draw taget image based on topleft of rect
        surface.blit(self.target_image, self.target_rect.topleft)

        #draw all index Pieces
        for piece in self.pieces:
            piece.draw(surface)

    def get_active_piece(self):
        #returnss piece being dragged
        for piece in self.pieces:
            if piece.is_dragging:
                return piece
        return None


#-------ACTUAL LEVELS, CHANGE THESE TO CHANGE THE GAME----------------------------------------------------------

def get_level_data(level_index):
    
    LEVELS = [
        #Level ONE
            {"target_image": "LevelOne.png",
               "pieces": 
               [{"path": "Square_Shape.png",
                "initial_pos_offset": (0, 0),
                "correct_grid": [(5, 5)]}]},
        #LEVEL TWO
            {"target_image": "LevelTwo.png",
               "pieces": 
               [{"path": "Small_L_Shape.png",
                "initial_pos_offset": (0, 0),
                "correct_grid": [(4, 3), (6, 7), (5, 6)]},
                {"path": "T_Shape.png",
                "initial_pos_offset": (1, 0),
                "correct_grid": [(6, 3)]},
                {"path": "L_Shape.png",
                "initial_pos_offset": (0, 1),
                "correct_grid": [(4, 5), (6, 6)]},
                {"path": "S_Shape.png",
                "initial_pos_offset": (1, 1),
                "correct_grid": [(5, 5), (4, 3)]},
                {"path": "I_Shape.png",
                "initial_pos_offset": (0, 2),
                "correct_grid": [(7, 6), (5, 6), (4, 5)]}]},
            #LEVEL THREE
            {"target_image": "Level_Three.png",
               "pieces": 
               [{"path": "L_Shape.png",
                "initial_pos_offset": (0, 0),
                "correct_grid": [(2, 2), (4, 2), (2, 4)]},
                {"path": "L_Shape.png",
                "initial_pos_offset": (1, 0),
                "correct_grid": [(4, 2), (2, 2), (2, 4)]},
                {"path": "Small_L_Shape.png",
                "initial_pos_offset": (0, 1),
                "correct_grid": [(3, 2), (2, 2), (3, 3)]},
                {"path": "Square_Shape.png",
                "initial_pos_offset": (1, 1),
                "correct_grid": [(2, 5), (5, 6), (2, 2), (3, 3)]},
                {"path": "T_Shape.png",
                "initial_pos_offset": (0, 2),
                "correct_grid": [(4, 4), (3, 5)]},
                {"path": "Square_Shape.png",
                "initial_pos_offset": (1, 2),
                "correct_grid": [(5, 6), (2, 5), (2, 2), (3, 3)]}]},
            #LEVEL FOUR
                {"target_image": "Level_Four.png",
               "pieces": 
               [{"path": "L_Shape.png",
                "initial_pos_offset": (0, 0),
                "correct_grid": [(5, 7)]},
                {"path": "Small_L_Shape.png",
                "initial_pos_offset": (1, 0),
                "correct_grid": [(3, 3), (4, 4)]},
                {"path": "Small_L_Shape.png",
                "initial_pos_offset": (0, 1),
                "correct_grid": [(3, 3), (4, 4)]},
                {"path": "I_Shape.png",
                "initial_pos_offset": (1, 1),
                "correct_grid": [(3, 7), (8, 6)]},
                {"path": "I_Shape.png",
                "initial_pos_offset": (0, 2),
                "correct_grid": [(3, 7), (8, 6)]},
                {"path": "S_Shape.png",
                "initial_pos_offset": (1, 2),
                "correct_grid": [(5, 5)]}]}
            ]
    

    if 0 <= level_index < len(LEVELS):
        return LEVELS[level_index]
    else:
        return None #no more levels
#---------------------------------------------------------------------------------------------------------------------
