import numpy as np
import constants as const


class Board:
    class __Board:
        board = None

        def __init__(self):
            self.board = np.zeros((const.GAME_ROWS, const.GAME_COLUMNS), dtype='int64')

        def calculate_coin_row(self, column):
            return 6 - np.bincount(self.board[:, column])[0]

        def add_coin(self, row, column, player):
            if player == 'red':
                self.board[row, column] = 1
            else:
                self.board[row, column] = 2

    instance = False

    def __init__(self):
        if not Board.instance:
            Board.instance = Board.__Board()

    def __getattr__(self, name):
        return getattr(self.instance, name)
