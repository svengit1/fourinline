import numpy as np

active_player = 'blue'


def turn(player):
    if player == "blue":
        return "red"
    elif player == "red":
        return "blue"


def check_game_state(state, row_length):
    shp = state.shape

    for y in range(0, shp[0]):
        for x in range(0, shp[1]):
            print(x, y)

    return np.array([[2, 1], [2, 2], [2, 3]])


class Board:
    board = None

    def __init__(self):
        row = [0 for i in range(7)]
        self.board = np.array([row.copy() for i in range(6)])

    def calculate_coin_row(self, column):
        return 6 - np.bincount(self.board[:, column])[0]

    def add_coin(self, row, column, player):
        if player == 'red':
            self.board[row][column] = 1
        else:
            self.board[row][column] = 2
