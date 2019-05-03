import pyglet
from pyglet.window import key
from pyglet.gl import *

import game_logic
import constants as const
from board import Board

from visuals.pointer import Pointer
from visuals.coin import Coin
from visuals.turn_indicator import TurnIndicator
import visuals.marker as marker

# Resources loading

board_image = pyglet.resource.image('assets/board.png')


# Init

window = pyglet.window.Window(const.WINDOW_WIDTH, const.WINDOW_HEIGHT, caption='Connect Four')

coins = []
coin_batch = pyglet.graphics.Batch()

pointer = Pointer()
board = Board()

turn_indicator = TurnIndicator()

marker_batch = pyglet.graphics.Batch()


@window.event
def on_draw():
    window.clear()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    coin_batch.draw()

    board_image.blit(0, 40)
    pointer.draw()
    turn_indicator.draw()

    glEnable(GL_LINE_SMOOTH)
    glLineWidth(100.0)
    marker_batch.draw()
    glDisable(GL_LINE_SMOOTH)


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        pointer.move_left()
    elif symbol == key.RIGHT:
        pointer.move_right()

    if symbol == key.ENTER or symbol == key.SPACE:
        place_coin(board.calculate_coin_row(pointer.column), pointer.column)

        game = game_logic.check_game_over(board.get_red_board(), board.get_blue_board())
        if game:
            victory_marker(game)


def place_coin(row, column):
    if row < const.GAME_ROWS:
        coin = Coin(const.COIN_X_START + (column * const.COIN_OFFSET),
                    const.COIN_Y_START + (row * const.COIN_OFFSET))

        coin.set_batch(coin_batch)
        coin.set_color(game_logic.active_player)
        coins.append(coin)

        board.add_coin(row, column, game_logic.active_player)

        switch_player()


def switch_player():
    new_color = game_logic.turn(game_logic.active_player)
    game_logic.active_player = new_color
    pointer.set_color(new_color)
    turn_indicator.switch_image()


def victory_marker(points):
    one = (50 + (points[0][1] * const.COIN_OFFSET),
           90 + (points[0][0] * const.COIN_OFFSET))

    two = (50 + (points[-1][1] * const.COIN_OFFSET),
           90 + (points[-1][0] * const.COIN_OFFSET))

    marker_batch.add(*marker.create_line(one, two, const.YELLOW))


if __name__ == '__main__':
    pyglet.app.run()
