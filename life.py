import numpy as np
from _run_life import run_life

def life(n=20, plot=False):
    """Set up the board and start the simulation"""
    # Fill the board randomly (but with a known seed for repeatability)
    np.random.seed(1)
    board = [[np.random.randint(0, 2) for i in range(n)] for j in range(n)]

    ####### DON'T CHANGE THIS LINE #######
    run_life(board, update, n, plot=plot)

def update(board, n):
    """Calculate the next board from the current board"""
    # Create the board at t+1 and zero-fill it
    next_board = [[0 for i in range(n)] for j in range(n)]

    # Figure out what to do to each cell
    for i in range(n):
        for j in range(n):
            n_alive_neighbors = get_n_alive_neighbors(board, n, i, j)

            # Apply live/die rules
            if board[i][j] == 1:
                if n_alive_neighbors in (2, 3):
                    next_board[i][j] = 1
                else:
                    next_board[i][j] = 0

            if board[i][j] == 0:
                if n_alive_neighbors == 3:
                    next_board[i][j] = 1
                else:
                    next_board[i][j] = 0

    # Copy the next board into the current board
    for i in range(n):
        for j in range(n):
            board[i][j] = next_board[i][j]

def get_n_alive_neighbors(board, n, i, j):
    """Return the number of neighbors of (i, j) that are alive"""
    n_alive_neighbors = 0
    # Go through all the positions on the board and add up how many
    # alive ones there are, but only if they're neighbors
    for i_neighbor in range(n):
        for j_neighbor in range(n):
                neighbor_val = board[i_neighbor][j_neighbor]
                if is_neighbor(i, j, i_neighbor, j_neighbor):
                    n_alive_neighbors += neighbor_val

    return n_alive_neighbors

def is_neighbor(i1, j1, i2, j2):
    """Return True if (i1, j1) is a neighbor of (i2, j2)"""
    if abs(i1 - i2) <= 1 and abs(j1 - j2) <= 1 and (
        i1 != i2 or j1 != j2):
        return True
    else:
        return False


####### DON'T CHANGE BELOW HERE #######

if __name__ == '__main__':
    life(n=20, plot=False)