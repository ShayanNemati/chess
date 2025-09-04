import pygame
from pygame.locals import *

class Screen:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("chess")
        pygame.display.set_icon(pygame.image.load("image/favicon.png"))

class Chessboard:

    squares = []
    files = ['a','b','c','d','e','f','g','h']

    def __init__(self, w, h):
        self.surf = pygame.transform.rotozoom(pygame.image.load("image/board.jpg").convert(), 0, 0.4)
        self.rect = self.surf.get_rect()
        self.rect.center = w//2, h//2 

class Square(Chessboard):
    
    def __init__(self, coordinate, point):
        self.coordinate = coordinate
        self.point = point
        self.surf = pygame.Surface((60,60))
        self.rect = self.surf.get_rect(topleft=self.coordinate)
        #color of square
        if (self.point[0]+self.point[1]) % 2 == 0:
            self.surf.fill((125, 148, 93))
            # self.surf.fill((0, 0, 0))
        else:
            self.surf.fill((238, 238, 213))
            # self.surf.fill((255, 255, 255))

    def __str__(self):
        return self.files[self.point[1]-1] + str(self.point[0])
        

class Piece:
    """This is a MOTHER class for all the pieces"""
    
    color_name = ("Black", "White")
    move_history = []
    
    def __init__(self,color_id,square):
        self.color = self.color_name[color_id]
        self.square = square

    def show_legal_moves(self):
        pass
    
    def move(self):
        pass
    
    def legal_move_or_not(self):
        pass
    
    def capture(self):
        pass
    
    def king_check(self):
        pass

class Pawn(Piece):
    """This is the son class for the pawn"""
    value = 1

    def __init__(self,color,square):
        super().__init__(color,square)
        if color == 1:
            self.image = pygame.image.load("image/w_pawn.png").convert()
        else:
            self.image = pygame.image.load("image/b_pawn.png").convert()
        self.image = pygame.transform.rotozoom(self.image ,0, 0.4)
    
    def en_passant(self):
        pass
    
    def promotion(self):
        pass

class Rook(Piece):
    """This is the son class for the rook"""
    value = 5
    
    def __init__(self,color,square):
        super().__init__(color,square)
        if color == 1:
            self.image = pygame.image.load("image/w_rook.png").convert()
        else:
            self.image = pygame.image.load("image/b_rook.png").convert()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.4)

class Knight(Piece):
    """This is the son class for the knight"""
    value = 3

    def __init__(self,color,square):
        super().__init__(color,square)
        if color == 1:
            self.image = pygame.image.load("image/w_knight.png").convert()
        else:
            self.image = pygame.image.load("image/b_knight.png").convert()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.4)

class Bishop(Piece):
    """This is the son class for the bishop"""
    value = 3

    def __init__(self,color,square):
        super().__init__(color,square)
        if color == 1:
            self.image = pygame.image.load("image/w_bishop.png").convert()
        else:
            self.image = pygame.image.load("image/b_bishop.png").convert()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.4)

class Queen(Piece):
    """This is the son class for the queen"""
    value = 9

    def __init__(self,color,square):
        super().__init__(color,square)
        if color == 1:
            self.image = pygame.image.load("image/w_queen.png").convert()
        else:
            self.image = pygame.image.load("image/b_queen.png").convert()
        self.image = pygame.transform.rotozoom(self.image, 0, 0.4)

class King(Piece):
    """This is the son class for the king"""
    def castle(self):
        pass