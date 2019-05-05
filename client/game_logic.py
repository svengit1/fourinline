import constants as const
import numpy as np

victory_sums = (15, 30, 60, 120, 31, 62, 124, 63, 126, 127)
victory_positions = [range(i, i+4) for i in range(4)] + \
                    [range(i, i+5) for i in range(3)] + \
                    [range(i, i+6) for i in range(2)] + \
                    [range(0, 7)]

power_of_two = [2**n for n in range(max(const.GAME_ROWS, const.GAME_COLUMNS)+1)]


def check_game_state(board):
    state = list(board.dot(power_of_two[:len(board[0])]))
    intersect = set(state).intersection(victory_sums)
    if intersect:
        i = intersect.pop()
        row = state.index(i)
        return [(row, e) for e in victory_positions[victory_sums.index(i)]]
    else:
        return []


def check_game_over(board):
    b_p1 = np.where(board < 1, 0, 1)
    b_p2 = np.where(board > -1, 0, 1)
    game = []
    t = check_game_state(b_p1)
    if t:
        print('---->', t)
        game = t

    t = check_game_state(b_p2)
    if t:
        game = t

    t = check_game_state(b_p1.T)
    if t:
        game = list(map(lambda f: f[::-1], t))

    t = check_game_state(b_p2.T)
    if t:
        game = list(map(lambda f: f[::-1], t))

    return game
