import pygame
from pygame.locals import *

pygame.init()

width = 640
height = 640
screen = pygame.display.set_mode((width,height))

board0 = pygame.image.load("image/board.jpg")
board0.convert()
board = pygame.transform.rotozoom(board0,0,0.4)
rect_board = board.get_rect()
rect_board.center = width//2,height//2

w_king = pygame.image.load("image/w_king.png")
w_queen = pygame.image.load("image/w_queen.png")
w_rook = pygame.image.load("image/w_rook.png")
w_bishop = pygame.image.load("image/w_bishop.png")
w_knight = pygame.image.load("image/w_knight.png")
w_pawn = pygame.image.load("image/w_pawn.png")

b_king = pygame.image.load("image/b_king.png")
b_queen = pygame.image.load("image/b_queen.png")
b_rook = pygame.image.load("image/b_rook.png")
b_bishop = pygame.image.load("image/b_bishop.png")
b_knight = pygame.image.load("image/b_knight.png")
b_pawn = pygame.image.load("image/b_pawn.png")

while True:
    screen.fill((40,40,40))
    screen.blit(board,((width-board.get_width())/2,(height-board.get_height())/2))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit(0)