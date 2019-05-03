import constants as const

active_player = 'blue'

victory_sums = (15, 30, 60, 120)
victory_positions = [range(i, i+4) for i in range(4)]
power_of_two = [2**n for n in range(max(const.GAME_ROWS, const.GAME_COLUMNS)+1)]


def turn(player):
    if player == "blue":
        return "red"
    elif player == "red":
        return "blue"


def check_game_state(board):
    state = list(board.dot(power_of_two[:len(board[0])]))
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
