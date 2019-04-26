import numpy as np


class Board:
    board = None

    def __init__(self):
        self.board = np.zeros((6, 7), dtype='int64')

    def calculate_coin_row(self, column):
        return 6 - np.bincount(self.board[:, column])[0]

    def add_coin(self, row, column, player):
        if player == 'red':
            self.board[row, column] = 1
        else:
            self.board[row, column] = 2
