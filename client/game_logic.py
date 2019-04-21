board = [0] * 42


def turn(player):
    if player == "blue":
        return "red"
    elif player == "red":
        return "blue"


