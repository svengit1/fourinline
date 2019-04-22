import pyglet
from pyglet.window import key

import game_logic
from pointer import Pointer
from coin import Coin

# Resources loading

board_image = pyglet.resource.image('assets/board.png')


# Init
w = 581
h = 520

active_player = 'blue'

window = pyglet.window.Window(w, h)

coins = []
blue_coin_batch = pyglet.graphics.Batch()
red_coin_batch = pyglet.graphics.Batch()

pointer = Pointer()


@window.event
def on_draw():
    window.clear()
    board_image.blit(0, 0)

    pointer.draw()

    blue_coin_batch.draw()
    red_coin_batch.draw()


@window.event
def on_key_press(symbol, modifiers):
    global active_player

    if symbol == key.LEFT:
        pointer.move_left()
    elif symbol == key.RIGHT:
        pointer.move_right()

    if symbol == key.ENTER or symbol == key.SPACE:
        coin = Coin(pointer.x - 3, game_logic.calculate_coin_y(pointer.column))
        coin.scale = 0.3

        if active_player == 'red':
            pointer.set_color('red')

            coin.set_batch(red_coin_batch)
            coin.set_color('red')
        else:
            pointer.set_color('blue')

            coin.set_batch(blue_coin_batch)
            coin.set_color('blue')

        coins.append(coin)
        active_player = game_logic.turn(active_player)


if __name__ == '__main__':
    pyglet.app.run()
