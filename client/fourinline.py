import pyglet
from pyglet.window import key
from pyglet.gl import *

import game_logic
import constants as const

from visuals.coin import Coin

from board import Board

from visuals.pointer import Pointer
from visuals.turn_indicator import TurnIndicator
import visuals.marker as marker

# Resources loading


# Init

window = pyglet.window.Window(const.WINDOW_WIDTH, const.WINDOW_HEIGHT, caption='Connect Four')

front = pyglet.graphics.OrderedGroup(2)
foreground = pyglet.graphics.OrderedGroup(1)
background = pyglet.graphics.OrderedGroup(0)

board_image = pyglet.resource.image('assets/board.png')
board_sprite = pyglet.sprite.Sprite(img=board_image, x=0, y=40, group=background)


coins = []
coin_batch = pyglet.graphics.Batch()

board = Board()
pointer = Pointer(board.next_player())
turn_indicator = TurnIndicator(board.next_player())

marker_batch = pyglet.graphics.Batch()


@window.event
def on_draw():
    window.clear()
    coin_batch.draw()
    board_sprite.draw()
    pointer.draw()
    turn_indicator.draw()
    marker_batch.draw()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        pointer.move_left()
    elif symbol == key.RIGHT:
        pointer.move_right()

    if symbol == key.ENTER or symbol == key.SPACE:
        current_player = board.next_player()
        place_coin(board.move(pointer.column), pointer.column, current_player)

        game = game_logic.check_game_over(board.get_board())
        if game:
            victory_marker(game)


def place_coin(row, column, player):
    c = Coin(const.COIN_X_START + (column * const.COIN_OFFSET),
                const.COIN_Y_START + ((const.GAME_ROWS-row-1) * const.COIN_OFFSET),
            coin_batch, player, foreground, (row, column))
    coins.append(c)
    pointer.set_color(board.next_player())
    turn_indicator.change_image(board.next_player())


def victory_marker(points):
    c = [list(filter(lambda coin: coin.get_position() == p, coins))[0] for p in points]
    for i in c:
        i.scale = 0.4
        i.group = front


if __name__ == '__main__':
    pyglet.app.run()
