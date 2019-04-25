import numpy as np

board = [0] * 42


def turn(player):
    if player == "blue":
        return "red"
    elif player == "red":
        return "blue"


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



