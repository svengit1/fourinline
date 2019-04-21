import pyglet
from pyglet.window import key
from game_logic import *

# Resources loading
red_coin_image = pyglet.resource.image('assets/coin-red.png')
blue_coin_image = pyglet.resource.image('assets/coin-blue.png')
board_image = pyglet.resource.image('assets/board.png')

pointer_red_image = pyglet.resource.image('assets/pointer-red.png')
pointer_blue_image = pyglet.resource.image('assets/pointer-blue.png')

# Init
w = 581
h = 520

active_player = 'blue'

window = pyglet.window.Window(w, h)

blue_coins = []
red_coins = []
blue_coin_batch = pyglet.graphics.Batch()
red_coin_batch = pyglet.graphics.Batch()

pointer = pyglet.sprite.Sprite(pointer_blue_image, 25+(80*6), 470)
pointer.scale = 0.4


@window.event
def on_draw():
    window.clear()
    board_image.blit(0, 0)

    pointer.draw()


@window.event
def on_key_press(symbol, modifiers):
    global active_player

    if symbol == key.LEFT:
        if pointer.x != 25:
            pointer.x -= 80
    elif symbol == key.RIGHT:
        if pointer.x != 505:
            pointer.x += 80

    if symbol == key.ENTER or symbol == key.SPACE:
        if active_player == 'red':
            pointer.image = pointer_red_image
        else:
            pointer.image = pointer_blue_image
        active_player = turn(active_player)


if __name__ == '__main__':
    pyglet.app.run()
