active_player = "blue"
board = [0] * 42


def turn():
    global active_player

    if active_player == "blue":
        active_player = "red"
        return 'red'
    if active_player == "red":
        active_player = "blue"
        return 'blue'


