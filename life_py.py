import numpy as np

def update_py(board, N):
    neighbors_arr = np.zeros((N, N))
    for i in range(1, N-1):
        for j in range(1, N-1):
            neighbors_arr[i, j] = getNeighbors(board, i, j, N)
    for i in range(1, N-1):
        for j in range(1, N-1):
            neighbors = neighbors_arr[i, j]
            if board[i, j] == 0:
                if neighbors == 3:
                    board[i, j] = 1
            elif board[i, j] == 1:
                if neighbors < 2 or neighbors > 3:
                    board[i, j] = 0

def getNeighbors(board, index_x, index_y, N):
    neighbors = 0
    for k in [-1,0,1]:
        for l in [-1,0,1]:
            if not (k == 0 and l == 0):
                if board[index_x+k,index_y + l] != 0:
                    neighbors += 1
    return neighbors

