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

screen.fill((40,40,40))
# screen.blit(board.surf,((width-board.surf.get_width())/2,(height-board.surf.get_height())/2))

#define squares
x = 80
y = 501
for rank in range(1,9):
    rank_squares = []
    for file in range(1,9):
        square = Square((rank, file), (x, y))
        rank_squares.append(square)
        screen.blit(square.surf, square.coordinate)
        x += 60
    board.squares.append(rank_squares)
    y -= 60
    x -= 8*60

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

#load white peice image
# screen.blit(b_rook,(91,91))
# screen.blit(b_knight,(148,87))
# screen.blit(b_bishop,(212,86))
# screen.blit(b_queen,(266,86))
# screen.blit(b_king,(327,84))
# screen.blit(b_bishop,(392,86))
# screen.blit(b_knight,(447,87))
# screen.blit(b_rook,(513,91))

# screen.blit(b_pawn,(94,154))
# screen.blit(b_pawn,(154,154))
# screen.blit(b_pawn,(214,154))
# screen.blit(b_pawn,(274,154))
# screen.blit(b_pawn,(334,154))
# screen.blit(b_pawn,(394,154))
# screen.blit(b_pawn,(454,154))
# screen.blit(b_pawn,(514,154))



# screen.blit(w_rook,(91,512))
# screen.blit(w_knight,(148,508))
# screen.blit(w_bishop,(212,507))
# screen.blit(w_queen,(266,507))
# screen.blit(w_king,(327,505))
# screen.blit(w_bishop,(392,507))
# screen.blit(w_knight,(447,508))
# screen.blit(w_rook,(513,512))

# screen.blit(w_pawn,(94,454))
# screen.blit(w_pawn,(154,454))
# screen.blit(w_pawn,(214,454))
# screen.blit(w_pawn,(274,454))
# screen.blit(w_pawn,(334,454))
# screen.blit(w_pawn,(394,454))
# screen.blit(w_pawn,(454,454))
# screen.blit(w_pawn,(514,454))
board.blit_pieces(screen)
pygame.display.flip()

#start chess
start_game.play()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit(0)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for rank in board.squares:
                for sq in rank:
                    sq.default_color()
                    screen.blit(sq.surf, sq.coordinate)
                    if sq.rect.collidepoint(event.pos):
                        if (sq.point[0]+sq.point[1]) % 2 == 0:
                            sq.surf.fill((185, 202, 67))
                        else:
                            sq.surf.fill((245, 246, 130))
                        screen.blit(sq.surf, sq.coordinate)
            board.blit_pieces(screen)
            pygame.display.flip()
        