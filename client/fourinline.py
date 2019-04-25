import pyglet
from pyglet.window import key

import game_logic
from pointer import Pointer
from coin import Coin
import constants as const

# Resources loading

board_image = pyglet.resource.image('assets/board.png')


# Init
window = pyglet.window.Window(const.window_width, const.window_height)

coins = []
blue_coin_batch = pyglet.graphics.Batch()
red_coin_batch = pyglet.graphics.Batch()

pointer = Pointer()
board = game_logic.Board()


@window.event
def on_draw():
    window.clear()
    board_image.blit(0, 0)

    blue_coin_batch.draw()
    red_coin_batch.draw()

    pointer.draw()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        pointer.move_left()
    elif symbol == key.RIGHT:
        pointer.move_right()

    if symbol == key.ENTER or symbol == key.SPACE:
        place_coin(board.calculate_coin_row(pointer.column), pointer.column)


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


if __name__ == '__main__':
    pyglet.app.run()
