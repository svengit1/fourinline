import numpy as np
import constants as const
import random as rnd


class Board:
    board = None
    player = 0

    def __init__(self):
        self.clear_board()
        self.player = rnd.choice([-1, 1])

    def move(self, column):
        row = np.where(abs(self.board[:, column]) == 1)[0]
        if len(row):
            row = row[0]
        else:
            row = self.board.shape[0]

        row -= 1

        if row > 0:
            self.board[row, column] = self.player
            self.player *= -1
        return row

    def next_player(self):
        return self.player

    def get_board(self):
        return self.board

    def clear_board(self):
        self.board = np.zeros((const.GAME_ROWS, const.GAME_COLUMNS), dtype='int64')
