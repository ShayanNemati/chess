import pygame
from pygame.locals import *
from classes import *

pygame.init()
pygame.mixer.init()

#display window
width = 640
height = 640
screen = Screen(width, height).screen

#sounds
start_game = pygame.mixer.Sound('sound/game-start.mp3')

#load chessboard
board = Chessboard(width, height)

#fill screen color
screen.fill((40,40,40))

#define squares
x = 80
y = 501
for rank in range(1,9):
    rank_squares = []
    for file in range(1,9):
        square = Square((rank, file), (x, y), None)
        square.default_color(screen)
        rank_squares.append(square)
        screen.blit(square.surf, square.coordinate)
        x += 60
    board.squares.append(rank_squares)
    y -= 60
    x -= 8*60

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

#insert peice in squares
for color in board.pieces:
    for type in board.pieces[color]:
        for piece in board.pieces[color][type]:
            board.squares[piece.current_square[0]-1][piece.current_square[1]-1].piece = piece

board.blit_pieces(screen)
start_game.play()
pygame.display.flip()

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
                        if sq.piece != None:
                            sq.highlight_square(screen)
                            sq.piece.show_legal_moves(screen, board)
            board.blit_pieces(screen)
            pygame.display.flip()