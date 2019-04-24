import numpy as np

active_player = 'blue'

row = [0 for i in range(7)]
board = np.array([row.copy() for i in range(6)])


def turn(player):
    if player == "blue":
        return "red"
    elif player == "red":
        return "blue"


def calculate_coin_row(column):
    return 6 - np.bincount(board[:, column])[0]


def add_coin(row, column, player):
    if player == 'red':
        board[row][column] = 1
    else:
        board[row][column] = 2


def check_game_state(state, row_length):
    shp = state.shape

    for y in range(0, shp[0]):
        for x in range(0, shp[1]):
            print(x, y)

    return np.array([[2, 1], [2, 2], [2, 3]])
