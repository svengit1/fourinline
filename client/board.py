import numpy as np
import constants as const


class Board:
    class __Board:
        board_red = None
        board_blue = None

        def __init__(self):
            self.board_red = np.zeros((const.GAME_ROWS, const.GAME_COLUMNS), dtype='int64')
            self.board_blue = np.zeros((const.GAME_ROWS, const.GAME_COLUMNS), dtype='int64')

        def calculate_coin_row(self, column):
            return 6 - np.bincount(np.where(self.board_red != 0, self.board_red, self.board_blue)[:, column])[0]

        def add_coin(self, row, column, player):
            if player == 'red':
                self.board_red[row, column] = 1
            else:
                self.board_blue[row, column] = 1

        def get_red_board(self):
            return self.board_red

        def get_blue_board(self):
            return self.board_blue

    instance = False

    def __init__(self):
        if not Board.instance:
            Board.instance = Board.__Board()

    def __getattr__(self, name):
        return getattr(self.instance, name)
