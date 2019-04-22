import numpy as np

board = [0] * 42


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

    return np.array([[2,1], [2, 2], [2, 3]])



