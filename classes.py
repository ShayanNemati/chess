import pygame
from pygame.locals import *

class Screen:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("chess")
        pygame.display.set_icon(pygame.image.load("image/favicon.png"))

class Chessboard(Screen):

    files = ['a','b','c','d','e','f','g','h']
    squares = []
    pieces = {}

    def __init__(self, w, h):
        self.surf = pygame.transform.rotozoom(pygame.image.load("image/board.jpg").convert(), 0, 0.4)
        self.rect = self.surf.get_rect(center=(w//2, h//2))

    def blit_chessboard(self, screen):
        for rank in self.squares:
                for sq in rank:
                    sq.default_color(screen)
                    # screen.blit(sq.surf, sq.coordinate)

    def blit_pieces(self, screen):
        for color in self.pieces:
            for type in self.pieces[color]:
                for piece in self.pieces[color][type]:
                    screen.blit(piece.surf, piece.coordinate)

class Square(Chessboard):
    
    def __init__(self, point, coordinate, piece):
        self.point = point
        self.coordinate = coordinate
        self.piece = piece
        self.surf = pygame.Surface((60,60))
        self.rect = self.surf.get_rect(topleft=self.coordinate)

    def __str__(self):
        return self.files[self.point[1]-1] + str(self.point[0])
        
    def default_color(self, screen):
        if (self.point[0]+self.point[1]) % 2 == 0:
            self.surf.fill((125, 148, 93))
        else:
            self.surf.fill((238, 238, 213))
        screen.blit(self.surf, self.coordinate)
    
    def highlight_square(self, screen):
        if (self.point[0]+self.point[1]) % 2 == 0:
            self.surf.fill((185, 202, 67))
        else:
            self.surf.fill((245, 246, 130))
        screen.blit(self.surf, self.coordinate)

    def show_move_marker(self, screen):
        if (self.point[0]+self.point[1]) % 2 == 0:
            pygame.draw.circle(self.surf, (99, 128, 70), (self.surf.get_width()//2, self.surf.get_height()//2), 10, 0)
        else:
            pygame.draw.circle(self.surf, (202, 203, 179), (self.surf.get_width()//2, self.surf.get_height()//2), 10, 0)
        screen.blit(self.surf, self.coordinate)

    def show_capture_marker(self, screen):
        if (self.point[0]+self.point[1]) % 2 == 0:
            pygame.draw.circle(self.surf, (99, 128, 70), (self.surf.get_width()//2, self.surf.get_height()//2), 30, 5)
        else:
            pygame.draw.circle(self.surf, (202, 203, 179), (self.surf.get_width()//2, self.surf.get_height()//2), 30, 5)
        screen.blit(self.surf, self.coordinate)

class Piece(Screen):
    """This is a MOTHER class for all the pieces"""
    
    color_name = ("Black", "White")
    move_history = []
    legal_squares = []
    
    def __init__(self, color_id, current_square, coordinate):
        self.color_id = color_id
        self.color = self.color_name[color_id]
        self.current_square = current_square
        self.coordinate = coordinate

    def show_legal_moves(self, screen, chessboard):
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

    def __init__(self ,color, current_square, coordinate):
        super().__init__(color, current_square, coordinate)
        if color == 1:
            self.surf = pygame.image.load("image/w_pawn.png").convert_alpha()
        else:
            self.surf = pygame.image.load("image/b_pawn.png").convert_alpha()
        self.surf = pygame.transform.rotozoom(self.surf ,0, 0.4)
    
    def show_legal_moves(self, screen, chessboard):

        self.legal_squares.clear()

        if len(self.move_history) == 0:
            if self.color_id == 0:
                self.legal_squares.append(chessboard.squares[self.current_square[0]-2][self.current_square[1]-1])
                self.legal_squares.append(chessboard.squares[self.current_square[0]-3][self.current_square[1]-1])  
            else:
                self.legal_squares.append(chessboard.squares[self.current_square[0]][self.current_square[1]-1])
                self.legal_squares.append(chessboard.squares[self.current_square[0]+1][self.current_square[1]-1])

        for sq in self.legal_squares:
            sq.show_move_marker(screen)
            # screen.blit(sq.surf, sq.coordinate)

    def en_passant(self):
        pass
    
    def promotion(self):
        pass

    def __str__(self):
        return "Pawn"

class Rook(Piece):
    """This is the son class for the rook"""
    value = 5
    
    def __init__(self, color, current_square, coordinate):
        super().__init__(color, current_square, coordinate)
        if color == 1:
            self.surf = pygame.image.load("image/w_rook.png").convert_alpha()
        else:
            self.surf = pygame.image.load("image/b_rook.png").convert_alpha()
        self.surf = pygame.transform.rotozoom(self.surf, 0, 0.4)

    def __str__(self):
        return "Rook"

class Knight(Piece):
    """This is the son class for the knight"""
    value = 3

    def __init__(self, color, current_square, coordinate):
        super().__init__(color, current_square, coordinate)
        if color == 1:
            self.surf = pygame.image.load("image/w_knight.png").convert_alpha()
        else:
            self.surf = pygame.image.load("image/b_knight.png").convert_alpha()
        self.surf = pygame.transform.rotozoom(self.surf, 0, 0.4)

    def __str__(self):
        return "Knight"

class Bishop(Piece):
    """This is the son class for the bishop"""
    value = 3

    def __init__(self, color, current_square, coordinate):
        super().__init__(color, current_square, coordinate)
        if color == 1:
            self.surf = pygame.image.load("image/w_bishop.png").convert_alpha()
        else:
            self.surf = pygame.image.load("image/b_bishop.png").convert_alpha()
        self.surf = pygame.transform.rotozoom(self.surf, 0, 0.4)

    def __str__(self):
        return "Bishop"

class Queen(Piece):
    """This is the son class for the queen"""
    value = 9

    def __init__(self, color, current_square, coordinate):
        super().__init__(color, current_square, coordinate)
        if color == 1:
            self.surf = pygame.image.load("image/w_queen.png").convert_alpha()
        else:
            self.surf = pygame.image.load("image/b_queen.png").convert_alpha()
        self.surf = pygame.transform.rotozoom(self.surf, 0, 0.4)

    def __str__(self):
        return "Queen"

class King(Piece):
    """This is the son class for the king"""

    def __init__(self, color, current_square, coordinate):
        super().__init__(color, current_square, coordinate)
        if color == 1:
            self.surf = pygame.image.load("image/w_king.png").convert_alpha()
        else:
            self.surf = pygame.image.load("image/b_king.png").convert_alpha()
        self.surf = pygame.transform.rotozoom(self.surf, 0, 0.4)

    def __str__(self):
        return "King"

    def castle(self):
        pass