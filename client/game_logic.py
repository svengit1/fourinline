import constants as const
import numpy as np

victory_sums = (15, 30, 60, 120, 31, 62, 124, 63, 126, 127)
victory_positions = [range(i, i+4) for i in range(4)] + \
                    [range(i, i+5) for i in range(3)] + \
                    [range(i, i+6) for i in range(2)] + \
                    [range(0, 7)]

power_of_two = [2**n for n in range(max(const.GAME_ROWS, const.GAME_COLUMNS)+1)]


def diagonal(board, off, direction):
    shp = board.shape
    ind = []
    vals = []
    column = 0

    if direction == 0:
        row = 0
        if off >= 0:
            for column in range(off, shp[1]):
                ind.append((row, column))
                vals.append(board[row, column])
                row += 1
                if row == shp[0]:
                    break
        else:
            for row in range(abs(off), shp[0]):
                ind.append((row, column))
                vals.append(board[row, column])
                column += 1
                if column == shp[1]:
                    break
    else:
        row = shp[0] - 1
        if off >= 0:
            for column in range(off, shp[1]):
                ind.append((row, column))
                vals.append(board[row, column])
                row -= 1
                if row < 0:
                    break
        else:
            for row in range(abs(off), shp[0]):
                ind.append((row, column))
                vals.append(board[row, column])
                column -= 1
                if column < 0:
                    break

    return np.array(vals), ind


def check_game_state(board):
    wining = []

    for direction in [0, 1]:
        for off in range(-board.shape[0]+1, board.shape[1]):
            d_vals, ind = diagonal(board, off, direction)
            val = d_vals.dot(power_of_two[:len(d_vals)])

            if val in victory_sums:
                wining.append([ind[i] for i in np.nonzero(d_vals)[0]])

    for x, b in enumerate([board, board.T]):
        state = list(b.dot(power_of_two[:len(b[0])]))
        intersect = set(state).intersection(victory_sums)
        if intersect:
            i = intersect.pop()
            row = state.index(i)
            r = [(row, e) for e in victory_positions[victory_sums.index(i)]]
            if x:
                wining.append(list(map(lambda j: j[::-1], r)))
            else:
                wining.append(r)

    return wining


def check_game_over(board):
    b_p1 = np.where(board < 1, 0, 1)
    b_p2 = np.where(board > -1, 0, 1)
    game = []
    t = check_game_state(b_p1)
    if t:
        game = t

    t = check_game_state(b_p2)
    if t:
        game = t

    return game
