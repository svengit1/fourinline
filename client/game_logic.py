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


def get_diag_indices(off, shp, d):
    ind = []
    row = 0
    column = 0
    diagonal_ind = np.nonzero(d)[0]

    if off >= 0:
        for column in range(off, shp[1]):
            ind.append((row, column))
            row += 1
    else:
        for row in range(abs(off), shp[0]):
            ind.append((row, column))
            column += 1

    return [ind[i] for i in diagonal_ind]


def check_game_state_diagonal(board):
    for off in range(-board.shape[0]+1, board.shape[1]):
        d = np.diagonal(board, off)
        val = d.dot(power_of_two[:len(d)])

        if val in victory_sums:
            return get_diag_indices(off, board.shape, d)

    return None


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

    t = check_game_state_diagonal(b_p1)
    if t:
        game = t

    t = check_game_state_diagonal(b_p2)
    if t:
        game = t

    # t = check_game_state_diagonal(b_p1.fliplr())
    # if t:
    #     game = t
    #
    # t = check_game_state_diagonal(b_p2.fliplr())
    # if t:
    #     game = t

    return game
