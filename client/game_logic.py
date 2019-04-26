import numpy as np

active_player = 'blue'


def turn(player):
    if player == "blue":
        return "red"
    elif player == "red":
        return "blue"


def check_game_state(state, row_length, player):
    shp = state.shape
    result = []
    print("Shape ", shp)
    for y in range(0, shp[0]):
        inrow = 0
        row = []
        for x in range(0, shp[1]):
            if state[y, x] == player:
                inrow += 1
                row.append([y, x])

            if state[y, x] == 0 or x == shp[1]-1:
                if inrow >= row_length and len(row) > 0:
                    result.append(row)
                inrow = 0
                row = []
    print(result)
    return np.array(result)
