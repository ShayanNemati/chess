import pygame
from pygame.locals import *
from classes import *

#display window
pygame.init()

width = 640
height = 640
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("chess")
pygame.display.set_icon(pygame.image.load("image/favicon.png"))

#load board image
board0 = pygame.image.load("image/board.jpg")
board0.convert()
board = pygame.transform.rotozoom(board0,0,0.4)
rect_board = board.get_rect()
rect_board.center = width//2,height//2


#load white peice image
w_king0 = pygame.image.load("image/w_king.png")
w_king0.convert()
w_king = pygame.transform.rotozoom(w_king0,0,0.4)

w_queen0 = pygame.image.load("image/w_queen.png")
w_queen0.convert()
w_queen = pygame.transform.rotozoom(w_queen0,0,0.4)

w_rook0 = pygame.image.load("image/w_rook.png")
w_rook0.convert()
w_rook = pygame.transform.rotozoom(w_rook0,0,0.4)

w_bishop0 = pygame.image.load("image/w_bishop.png")
w_bishop0.convert()
w_bishop = pygame.transform.rotozoom(w_bishop0,0,0.4)

w_knight0 = pygame.image.load("image/w_knight.png")
w_knight0.convert()
w_knight = pygame.transform.rotozoom(w_knight0,0,0.4)

w_pawn0 = pygame.image.load("image/w_pawn.png")
w_pawn0.convert()
w_pawn = pygame.transform.rotozoom(w_pawn0,0,0.4)


#load black peice image
b_king0 = pygame.image.load("image/b_king.png")
b_king0.convert()
b_king = pygame.transform.rotozoom(b_king0,0,0.4)

b_queen0 = pygame.image.load("image/b_queen.png")
b_queen0.convert()
b_queen = pygame.transform.rotozoom(b_queen0,0,0.4)

b_rook0 = pygame.image.load("image/b_rook.png")
b_rook0.convert()
b_rook = pygame.transform.rotozoom(b_rook0,0,0.4)

b_bishop0 = pygame.image.load("image/b_bishop.png")
b_bishop0.convert()
b_bishop = pygame.transform.rotozoom(b_bishop0,0,0.4)

b_knight0 = pygame.image.load("image/b_knight.png")
b_knight0.convert()
b_knight = pygame.transform.rotozoom(b_knight0,0,0.4)

b_pawn0 = pygame.image.load("image/b_pawn.png")
b_pawn0.convert()
b_pawn = pygame.transform.rotozoom(b_pawn0,0,0.4)


#value of peice
peices = {
    "queen": 9,
    "rook": 5,
    "bishop": 3,
    "knight": 3,
    "pawn": 1
}

screen.fill((40,40,40))
screen.blit(board,((width-board.get_width())/2,(height-board.get_height())/2))

screen.blit(b_rook,(91,91))
screen.blit(b_knight,(148,87))
screen.blit(b_bishop,(212,86))
screen.blit(b_queen,(266,86))
screen.blit(b_king,(327,84))
screen.blit(b_bishop,(392,86))
screen.blit(b_knight,(447,87))
screen.blit(b_rook,(513,91))

screen.blit(b_pawn,(93,154))
screen.blit(b_pawn,(154,154))
screen.blit(b_pawn,(214,154))
screen.blit(b_pawn,(274,154))
screen.blit(b_pawn,(334,154))
screen.blit(b_pawn,(394,154))
screen.blit(b_pawn,(454,154))
screen.blit(b_pawn,(514,154))



screen.blit(w_rook,(91,512))
screen.blit(w_knight,(148,508))
screen.blit(w_bishop,(212,507))
screen.blit(w_queen,(266,507))
screen.blit(w_king,(327,505))
screen.blit(w_bishop,(392,507))
screen.blit(w_knight,(447,508))
screen.blit(w_rook,(513,512))

screen.blit(w_pawn,(93,454))
screen.blit(w_pawn,(154,454))
screen.blit(w_pawn,(214,454))
screen.blit(w_pawn,(274,454))
screen.blit(w_pawn,(334,454))
screen.blit(w_pawn,(394,454))
screen.blit(w_pawn,(454,454))
screen.blit(w_pawn,(514,454))
pygame.display.flip()


rect = Rect(80,81,60,60)
rect2 = Rect(140,81,60,60)
pygame.draw.rect(screen,(255,0,0),rect)
pygame.draw.rect(screen,(0,0,255),rect2)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit(0)