"""This file is for important classes and all those stuff"""
import pygame
from pygame.locals import *

class Screen:
    """defining a class for the screen """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("chess")
        pygame.display.set_icon(pygame.image.load("image/favicon.png"))

class Chessboard(Screen):
    """Defining the chessboard as a class"""
    files = ['a','b','c','d','e','f','g','h']

    def __init__(self, w, h):
        self.surf = pygame.transform.rotozoom(pygame.image.load("image/board.jpg").convert(), 0, 0.4)
        self.rect = self.surf.get_rect(center=(w//2, h//2))
        self.squares = []
        self.pieces = {}

    def blit_chessboard(self, screen):
        """for bliting the chess board"""
        for rank in self.squares:
            for sq in rank:
                sq.default_color(screen)

#mishe inja ham az .items estefade kard?
    def blit_pieces(self, screen):
        """for bliting pieaces"""
        for rank in self.squares:
            for sq in rank:
                if sq.piece is not None:
                    screen.blit(sq.piece.surf, sq.piece.coordinate)

class Square(Chessboard):
    """This is The square Class whihc inherits from Chessboeard class"""
    def __init__(self, point, coordinate, piece):
        self.point = point
        self.coordinate = coordinate
        self.piece = piece
        self.surf = pygame.Surface((60,60))
        self.rect = self.surf.get_rect(topleft=self.coordinate)

    def __str__(self):
        return self.files[self.point[1]-1] + str(self.point[0])
    
    def default_color(self, screen):
        """Idk"""
        if (self.point[0]+self.point[1]) % 2 == 0:
            self.surf.fill((125, 148, 93))
        else:
            self.surf.fill((238, 238, 213))
        screen.blit(self.surf, self.coordinate)

    def highlight_square(self, screen):
        """For highlighting some square into yellow"""
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
    legal_squares = []
    move_history = []

    def __init__(self, color_id, current_point, coordinate):
        self.color_id = color_id
        self.color = self.color_name[color_id]
        self.current_point = current_point
        self.coordinate = coordinate
        self.is_move = False

    def move(self, move_square, sound):
        sound.play()
        destance_points = (move_square.point[0] - self.current_point[0], move_square.point[1] - self.current_point[1])
        self.current_point = move_square.point
        self.coordinate = (self.coordinate[0] + 60*destance_points[1], self.coordinate[1] - 60*destance_points[0])
        move_square.piece = self
        self.move_history.append(move_square)
        self.is_move = True

    def legal_move_or_not(self):
        pass

    def capture(self, chessboard, move_square, sound):
        move_square.piece = None
        self.move(move_square, sound)

    def king_check(self):
        pass

class Pawn(Piece):
    """This is the son class for the pawn"""
    value = 1

    def __init__(self ,color, current_point, coordinate):
        super().__init__(color, current_point, coordinate)
        if color == 1:
            self.surf = pygame.image.load("image/w_pawn.png").convert_alpha()
        else:
            self.surf = pygame.image.load("image/b_pawn.png").convert_alpha()
        self.surf = pygame.transform.rotozoom(self.surf ,0, 0.4)
        
    def show_legal_moves(self, screen, chessboard):

        self.legal_squares.clear()

        if self.color_id == 0:

            if self.current_point[0] > 1:
                next_square = chessboard.squares[self.current_point[0]-2][self.current_point[1]-1]
                if next_square.piece is None:
                    self.legal_squares.append(next_square)
                    if self.current_point[0] > 2:
                        next_square = chessboard.squares[self.current_point[0]-3][self.current_point[1]-1]
                        if (not self.is_move) and (next_square.piece is None):
                            self.legal_squares.append(next_square)

            if (self.current_point[0] > 1) and (self.current_point[1] > 1) and (chessboard.squares[self.current_point[0]-2][self.current_point[1]-2].piece is not None):
                    self.legal_squares.append(chessboard.squares[self.current_point[0]-2][self.current_point[1]-2])

            if (self.current_point[0] > 1) and (self.current_point[1] < 8) and chessboard.squares[self.current_point[0]-2][self.current_point[1]].piece is not None:
                    self.legal_squares.append(chessboard.squares[self.current_point[0]-2][self.current_point[1]])

        else:

            if self.current_point[0] < 8:
                next_square = chessboard.squares[self.current_point[0]][self.current_point[1]-1]
                if next_square.piece is None:
                    self.legal_squares.append(next_square)
                    if self.current_point[0] < 7:
                        next_square = chessboard.squares[self.current_point[0]+1][self.current_point[1]-1]
                        if (not self.is_move) and (next_square.piece is None):
                            self.legal_squares.append(next_square)

            if (self.current_point[0] < 8) and (self.current_point[1] < 8) and (chessboard.squares[self.current_point[0]][self.current_point[1]].piece is not None):
                self.legal_squares.append(chessboard.squares[self.current_point[0]][self.current_point[1]])

            if (self.current_point[0] < 8) and (self.current_point[1] > 1) and (chessboard.squares[self.current_point[0]][self.current_point[1]-2].piece is not None):
                    self.legal_squares.append(chessboard.squares[self.current_point[0]][self.current_point[1]-2])

        for sq in self.legal_squares:
            if sq.piece is None:
                sq.show_move_marker(screen)
            elif sq.piece.color_id != self.color_id:
                sq.show_capture_marker(screen)

    def en_passant(self):
        pass

    def promotion(self):
        pass

    def __str__(self):
        return "Pawn"

class Rook(Piece):
    """This is the son class for the rook"""
    value = 5
    def __init__(self, color, current_point, coordinate):
        super().__init__(color, current_point, coordinate)
        if color == 1:
            self.surf = pygame.image.load("image/w_rook.png").convert_alpha()
        else:
            self.surf = pygame.image.load("image/b_rook.png").convert_alpha()
        self.surf = pygame.transform.rotozoom(self.surf, 0, 0.4)

    def show_legal_moves(self, screen, chessboard):

        self.legal_squares.clear()

        for i in range(self.current_point[0] - 2, -1, -1):
            square = chessboard.squares[i][self.current_point[1] - 1]
            if square.piece is not None:
                if square.piece.color_id != self.color_id:
                    self.legal_squares.append(square)
                    break
                else:
                    break
            else:
                self.legal_squares.append(square)

        for i in range(self.current_point[0], 8):
            square = chessboard.squares[i][self.current_point[1] - 1]
            if square.piece is not None:
                if square.piece.color_id != self.color_id:
                    self.legal_squares.append(square)
                    break
                else:
                    break
            else:
                self.legal_squares.append(square)

        for j in range(self.current_point[1] - 2, -1, -1):
            square = chessboard.squares[self.current_point[0] - 1][j]
            if square.piece is not None:
                if square.piece.color_id != self.color_id:
                    self.legal_squares.append(square)
                    break
                else:
                    break
            else:
                self.legal_squares.append(square)

        for j in range(self.current_point[1], 8):
            square = chessboard.squares[self.current_point[0] - 1][j]
            if square.piece is not None:
                if square.piece.color_id != self.color_id:
                    self.legal_squares.append(square)
                    break
                else:
                    break
            else:
                self.legal_squares.append(square)

        for sq in self.legal_squares:
            if sq.piece is None:
                sq.show_move_marker(screen)
            elif sq.piece.color_id != self.color_id:
                sq.show_capture_marker(screen)

    def __str__(self):
        return "Rook"

class Knight(Piece):
    """This is the son class for the knight"""
    value = 3

    def __init__(self, color, current_point, coordinate):
        super().__init__(color, current_point, coordinate)
        if color == 1:
            self.surf = pygame.image.load("image/w_knight.png").convert_alpha()
        else:
            self.surf = pygame.image.load("image/b_knight.png").convert_alpha()
        self.surf = pygame.transform.rotozoom(self.surf, 0, 0.4)

    def show_legal_moves(self, screen, chessboard):

        self.legal_squares.clear()
        col , row = self.current_point[0] - 1 ,  self.current_point[1] - 1
        moves = [
            (col - 2, row - 1), (col - 2, row + 1),
            (col - 1, row - 2), (col - 1, row + 2),
            (col + 1, row - 2), (col + 1, row + 2),
            (col + 2, row - 1), (col + 2, row + 1)
        ]

        for r, c in moves:
            if 0 <= r < 8 and 0 <= c < 8:
                self.legal_squares.append(chessboard.squares[r][c])

        for sq in self.legal_squares:
            if sq.piece is None:
                sq.show_move_marker(screen)
            elif sq.piece.color_id != self.color_id:
                sq.show_capture_marker(screen)

    def __str__(self):
        return "Knight"

class Bishop(Piece):
    """This is the son class for the bishop"""
    value = 3

    def __init__(self, color, current_point, coordinate):
        super().__init__(color, current_point, coordinate)
        if color == 1:
            self.surf = pygame.image.load("image/w_bishop.png").convert_alpha()
        else:
            self.surf = pygame.image.load("image/b_bishop.png").convert_alpha()
        self.surf = pygame.transform.rotozoom(self.surf, 0, 0.4)

    def show_legal_moves(self, screen, chessboard):

        self.legal_squares.clear()

        r, c = self.current_point[0] - 2, self.current_point[1] - 2
        while r >= 0 and c >= 0:
            if chessboard.squares[r][c].piece is not None:
                if chessboard.squares[r][c].piece.color_id != self.color_id:
                    self.legal_squares.append(chessboard.squares[r][c])
                    break
                else:
                    break
            else:
                self.legal_squares.append(chessboard.squares[r][c])
                r -= 1
                c -= 1

        r, c = self.current_point[0] - 2, self.current_point[1]
        while r >= 0 and c < 8:
            if chessboard.squares[r][c].piece is not None:
                if chessboard.squares[r][c].piece.color_id != self.color_id:
                    self.legal_squares.append(chessboard.squares[r][c])
                    break
                else:
                    break
            else:
                self.legal_squares.append(chessboard.squares[r][c])
                r -= 1
                c += 1

        r, c = self.current_point[0], self.current_point[1] - 2
        while r < 8 and c >= 0:
            if chessboard.squares[r][c].piece is not None:
                if chessboard.squares[r][c].piece.color_id != self.color_id:
                    self.legal_squares.append(chessboard.squares[r][c])
                    break
                else:
                    break
            else:
                self.legal_squares.append(chessboard.squares[r][c])
                r += 1
                c -= 1

        r, c = self.current_point[0], self.current_point[1]
        while r < 8 and c < 8:
            if chessboard.squares[r][c].piece is not None:
                if chessboard.squares[r][c].piece.color_id != self.color_id:
                    self.legal_squares.append(chessboard.squares[r][c])
                    break
                else:
                    break
            else:
                self.legal_squares.append(chessboard.squares[r][c])
                r += 1
                c += 1

        for sq in self.legal_squares:
            if sq.piece is None:
                sq.show_move_marker(screen)
            elif sq.piece.color_id != self.color_id:
                sq.show_capture_marker(screen)

    def __str__(self):
        return "Bishop"

class Queen(Piece):
    """This is the son class for the queen"""
    value = 9

    def __init__(self, color, current_point, coordinate):
        super().__init__(color, current_point, coordinate)
        if color == 1:
            self.surf = pygame.image.load("image/w_queen.png").convert_alpha()
        else:
            self.surf = pygame.image.load("image/b_queen.png").convert_alpha()
        self.surf = pygame.transform.rotozoom(self.surf, 0, 0.4)

    def show_legal_moves(self, screen, chessboard):

        self.legal_squares.clear()
        row, col = self.current_point[0], self.current_point[1]

        for i in range(row - 2, -1, -1):
            square = chessboard.squares[i][self.current_point[1] - 1]
            if square.piece is not None:
                if square.piece.color_id != self.color_id:
                    self.legal_squares.append(square)
                    break
                else:
                    break
            else:
                self.legal_squares.append(square)

        for i in range(row, 8):
            square = chessboard.squares[i][self.current_point[1] - 1]
            if square.piece is not None:
                if square.piece.color_id != self.color_id:
                    self.legal_squares.append(square)
                    break
                else:
                    break
            else:
                self.legal_squares.append(square)

        for j in range(col - 2, -1, -1):
            square = chessboard.squares[self.current_point[0] - 1][j]
            if square.piece is not None:
                if square.piece.color_id != self.color_id:
                    self.legal_squares.append(square)
                    break
                else:
                    break
            else:
                self.legal_squares.append(square)

        for j in range(col, 8):
            square = chessboard.squares[self.current_point[0] - 1][j]
            if square.piece is not None:
                if square.piece.color_id != self.color_id:
                    self.legal_squares.append(square)
                    break
                else:
                    break
            else:
                self.legal_squares.append(square)

        r, c = row - 2, col - 2
        while r >= 0 and c >= 0:
            if chessboard.squares[r][c].piece is not None:
                if chessboard.squares[r][c].piece.color_id != self.color_id:
                    self.legal_squares.append(chessboard.squares[r][c])
                    break
                else:
                    break
            else:
                self.legal_squares.append(chessboard.squares[r][c])
                r -= 1
                c -= 1

        r, c = row - 2, col
        while r >= 0 and c < 8:
            if chessboard.squares[r][c].piece is not None:
                if chessboard.squares[r][c].piece.color_id != self.color_id:
                    self.legal_squares.append(chessboard.squares[r][c])
                    break
                else:
                    break
            else:
                self.legal_squares.append(chessboard.squares[r][c])
                r -= 1
                c += 1

        r, c = row, col - 2
        while r < 8 and c >= 0:
            if chessboard.squares[r][c].piece is not None:
                if chessboard.squares[r][c].piece.color_id != self.color_id:
                    self.legal_squares.append(chessboard.squares[r][c])
                    break
                else:
                    break
            else:
                self.legal_squares.append(chessboard.squares[r][c])
                r += 1
                c -= 1

        r, c = row, col
        while r < 8 and c < 8:
            if chessboard.squares[r][c].piece is not None:
                if chessboard.squares[r][c].piece.color_id != self.color_id:
                    self.legal_squares.append(chessboard.squares[r][c])
                    break
                else:
                    break
            else:
                self.legal_squares.append(chessboard.squares[r][c])
                r += 1
                c += 1

        for sq in self.legal_squares:
            if sq.piece is None:
                sq.show_move_marker(screen)
            elif sq.piece.color_id != self.color_id:
                sq.show_capture_marker(screen)

    def __str__(self):
        return "Queen"

class King(Piece):
    """This is the son class for the king"""
    value = 0

    def __init__(self, color, current_point, coordinate):
        super().__init__(color, current_point, coordinate)
        if color == 1:
            self.surf = pygame.image.load("image/w_king.png").convert_alpha()
        else:
            self.surf = pygame.image.load("image/b_king.png").convert_alpha()
        self.surf = pygame.transform.rotozoom(self.surf, 0, 0.4)

    def show_legal_moves(self, screen, chessboard):

        self.legal_squares.clear()
        row, col = self.current_point[0] - 1, self.current_point[1] - 1
        moves = [
            (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
            (row, col - 1),                     (row, col + 1),
            (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)
        ]

        for r, c in moves:
            if 0 <= r < 8 and 0 <= c < 8:
                self.legal_squares.append(chessboard.squares[r][c])

        for sq in self.legal_squares:
            if sq.piece is None:
                sq.show_move_marker(screen)
            elif sq.piece.color_id != self.color_id:
                sq.show_capture_marker(screen)

    def __str__(self):
        return "King"

    def castle(self):
        pass
