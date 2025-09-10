"""This is the main file for our chess game"""
import pygame
#! wild card imports shuold be fixed at the end later
from pygame.locals import *
from classes import *

pygame.init()
pygame.mixer.init()

#display window
WIDTH = 640
HEIGHT = 640
screen = Screen(WIDTH, HEIGHT).screen

#sounds
start_game = pygame.mixer.Sound('sound/game-start.mp3')
move = pygame.mixer.Sound('sound/move-self.mp3')

#load chessboard
board = Chessboard(WIDTH, HEIGHT)

#fill screen color
screen.fill((40,40,40))

#define squares
X = 80
Y = 501
for rank in range(1,9):
    rank_squares = []
    for file in range(1,9):
        square = Square((rank, file), (X, Y), None)
        square.default_color(screen)
        rank_squares.append(square)
        screen.blit(square.surf, square.coordinate)
        X += 60
    board.squares.append(rank_squares)
    Y -= 60
    X -= 8*60

#define peice
board.pieces = {
        'white': {
            "pawn": [Pawn(1, (2,i), (94+(i-1)*60,454)) for i in range(1,9)],
            "rook": [Rook(1, (1,1), (91,512)), Rook(1, (1,8), (513,512))],
            "knight": [Knight(1, (1,2), (148,508)), Knight(1, (1,7), (447,508))],
            "bishop": [Bishop(1, (1,3), (212,507)), Bishop(1, (1,6), (392,507))],
            "queen": [Queen(1, (1,4), (266,507))],
            "king": [King(1, (1,5), (327,505))]
        },
        'black': {
            "pawn": [Pawn(0, (7,i), (94+(i-1)*60,154)) for i in range(1,9)],
            "rook": [Rook(0, (8,1), (91,91)), Rook(0, (8,8), (513,91))],
            "knight": [Knight(0, (8,2), (148,87)), Knight(0, (8,7), (447,87))],
            "bishop": [Bishop(0, (8,3), (212,86)), Bishop(0, (8,6), (392,86))],
            "queen": [Queen(0, (8,4), (266,86))],
            "king": [King(0, (8,5), (327,84))]
        }
    }

# for color in board.pieces:
#     for typee in board.pieces[color]:
#         for piece in board.pieces[color][typee]:
#             board.squares[piece.current_point[0]-1][piece.current_point[1]-1].piece = piece

for color, type_dict in board.pieces.items():
    for typee, pieces in type_dict.items():
        for piece in pieces:
            board.squares[piece.current_point[0]-1][piece.current_point[1]-1].piece = piece


board.blit_pieces(screen)
start_game.play()
pygame.display.flip()

SELECTED_SQUARE = None

#start chess
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            board.blit_chessboard(screen)
            for rank in board.squares:
                for sq in rank:
                    if sq.rect.collidepoint(event.pos):
                        if (sq.piece is not None) and (SELECTED_SQUARE is not None) and (sq in SELECTED_SQUARE.piece.legal_squares or sq in SELECTED_SQUARE.piece.legal_squares2):
                            SELECTED_SQUARE.piece.capture(sq , board)
                            move.play()
                            SELECTED_SQUARE.piece = None
                            SELECTED_SQUARE = None
                            
                        elif (sq.piece is None) and (SELECTED_SQUARE is not None) and (sq in SELECTED_SQUARE.piece.legal_squares):
                            SELECTED_SQUARE.piece.move(sq)
                            move.play()
                            SELECTED_SQUARE.piece = None
                            SELECTED_SQUARE = None
                        elif sq.piece is not None:
                            SELECTED_SQUARE = sq
                            SELECTED_SQUARE.highlight_square(screen)
                            SELECTED_SQUARE.piece.show_legal_moves(screen, board)

            board.blit_pieces(screen)
            pygame.display.flip()
