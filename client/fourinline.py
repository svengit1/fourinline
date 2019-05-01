import pyglet
from pyglet.window import key
from pyglet.gl import *

import game_logic
import constants as const
from board import Board

from visuals.pointer import Pointer
from visuals.coin import Coin
from visuals.turn_indicator import TurnIndicator
from visuals.marker import create_line

# Resources loading

board_image = pyglet.resource.image('assets/board.png')


# Init

window = pyglet.window.Window(const.window_width, const.window_height, caption='Connect Four')

coins = []
blue_coin_batch = pyglet.graphics.Batch()
red_coin_batch = pyglet.graphics.Batch()

pointer = Pointer()
board = Board()

turn_indicator = TurnIndicator()

marker_batch = pyglet.graphics.Batch()


@window.event
def on_draw():
    window.clear()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    blue_coin_batch.draw()
    red_coin_batch.draw()

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
        marker_batch.add(*create_line((10, 10), (100, 100), (255, 255, 0)))


def place_coin(row, column):
    if row < 6:
        coin = Coin(pointer.x - const.coin_x_offset, const.coin_y_offset + 80 * row)

        if game_logic.active_player == 'red':
            coin.set_batch(red_coin_batch)
            coin.set_color('red')
        else:
            coin.set_batch(blue_coin_batch)
            coin.set_color('blue')

        coins.append(coin)
        board.add_coin(row, column, game_logic.active_player)

        new_color = game_logic.turn(game_logic.active_player)
        game_logic.active_player = new_color
        pointer.set_color(new_color)
        turn_indicator.switch_image()


if __name__ == '__main__':
    pyglet.app.run()
