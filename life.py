import matplotlib.pyplot as plt
import numpy as np

def setBoard(board, initial_state):

if __name__ == '__main__':
    grid = 100
    board = np.zeros((grid,grid))
    for yi in xrange(grid):
        for xi in xrange(grid):
            if (xi + yi) % 2 == 0:
                board[yi][xi] = 1
    plt.pcolormesh(board)
    plt.show()
