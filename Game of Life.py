import numpy as np
import pygame
import sys
import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
width = 100
height = 100
blockSize = 5
WINDOW_HEIGHT = blockSize * height
WINDOW_WIDTH = blockSize * width


def insertGlider(x,y, board):
    board[x][y] = 1
    board[x+1][y+1] = 1
    board[x+1][y+2] = 1
    board[x][y+2] = 1
    board[x-1][y+2] = 1


def generateBoard():
    return np.zeros((int(WINDOW_HEIGHT/blockSize),int(WINDOW_WIDTH/blockSize)), dtype=int)

def generateRandomBoard():
    return np.round(np.random.uniform(low=0, high=1, size=(int(WINDOW_HEIGHT/blockSize),int(WINDOW_WIDTH/blockSize)) )).astype(int)

def generateNext(board):
    neighbours = np.zeros(board.shape, dtype=int)
    for i in [-1,0,1]:
        brd= np.roll(board, i, axis = 1)
        for j in [-1,0,1]:
            neighbours += np.roll(brd, j, axis = 0)

    three = (neighbours == 3)
    four = np.logical_and(board.astype(bool) ,(neighbours == 4))

    return np.logical_or(three, four).astype(int)



def main():
    global SCREEN, CLOCK
    pygame.init()
    pygame.display.set_caption('Conway\'s Game of Life')
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    board=generateRandomBoard()
    # board=generateBoard()
    # insertGlider(5,5,board)
    prevBoard = None
    while True:
        if np.array_equal(prevBoard, board):
            break
        drawGrid(board)
        prevBoard = board
        board = generateNext(board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        time.sleep(0.025)


def drawGrid(board):
    global blockSize, WINDOW_WIDTH, WINDOW_HEIGHT
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect)
            if board[int(x/blockSize)][int(y/blockSize)] != 0:
                pygame.draw.rect(SCREEN, BLACK, rect)
            else:
                pygame.draw.rect(SCREEN, WHITE, rect)

main()