import numpy as np

active_player = 'blue'


def turn(player):
    if player == "blue":
        return "red"
    elif player == "red":
        return "blue"


def check_game_state(board):
    victory_sums = (7, 15, 30, 60)
    victory_positions = [range(0, 4), range(1, 5), range(2, 6), range(3, 7)]

    v = [0, 1, 2, 4, 8, 16, 32]
    state = list(board.dot(v[:len(board[0])]))
    intersect = set(state).intersection(victory_sums)

    if intersect:
        i = intersect.pop()
        row = state.index(i)
        return [(row, e) for e in victory_positions[victory_sums.index(i)]]
    else:
        return []


def _check_game_over_helper(board):
    state = check_game_state(board)
    if len(state) == 4:
        return state
    else:
        return None


def check_game_over(board_one, board_two):
    game = []
    t = _check_game_over_helper(board_one)
    if t:
        game = t

    t = _check_game_over_helper(board_two)
    if t:
        game = t

    t = _check_game_over_helper(board_one.T)
    if t:
        game = list(map(lambda f: f[::-1], t))

    t = _check_game_over_helper(board_two.T)
    if t:
        game = list(map(lambda f: f[::-1], t))

    return game
