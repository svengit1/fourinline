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
    result = []
    print("Shape ", shp)
    for y in range(0, shp[0]):
        inrow = 0
        row = []
        for x in range(0, shp[1]):
            if state[y, x] == 1:
                inrow += 1
                row.append([y, x])
            else:
                inrow == 0
                row = []
            if inrow >= row_length:
                result.append(row)

    print(result)
    return result
