import pygame
from pygame.locals import *

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
GAME_ON = True
SPEED = 20

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

square = pygame.Surface((50,50))
square.fill((255,0,0))
POS = [(200,200)]

def move_square(direction):
    if UP == direction:
        POS.append((POS[0][0], POS[0][1] - 20))
    elif direction == DOWN:
        POS.append((POS[0][0], POS[0][1] + 20))
    elif direction == LEFT:
        POS.append((POS[0][0] - 20, POS[0][1]))
    else:
        POS.append((POS[0][0] + 20, POS[0][1]))
    POS.pop(0)


while GAME_ON:

    for event in pygame.event.get():
        if event.type == QUIT:
            GAME_ON = False
        if event.type == KEYDOWN:
            if event.key==K_UP:
                print("UP")
                move_square(UP)                
            elif event.key==K_LEFT:
                print("LEFT")
                move_square(LEFT)               
            elif event.key==K_DOWN:
                print("DOWN")
                move_square(DOWN)                
            elif event.key==K_RIGHT:
                print("RIGHT")
                move_square(RIGHT)
    
    screen.fill((0,0,0))
    screen.blit(square, POS[0])
    pygame.display.update()

pygame.quit()