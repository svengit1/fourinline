import pyglet
from pyglet.window import key

# Resources loading
red_coin_image = pyglet.resource.image('assets/coin-red.png')
blue_coin_image = pyglet.resource.image('assets/coin-blue.png')
board_image = pyglet.resource.image('assets/board.png')

pointer_red_image = pyglet.resource.image('assets/pointer-red.png')
pointer_blue_image = pyglet.resource.image('assets/pointer-blue.png')

# Init
w = 581
h = 501

window = pyglet.window.Window(w, h)

blue_coins = []
red_coins = []
blue_coin_batch = pyglet.graphics.Batch()
red_coin_batch = pyglet.graphics.Batch()

pointer = pyglet.sprite.Sprite(pointer_blue_image, 100, 100)
pointer.scale = 0.4


@window.event
def on_draw():
    window.clear()
    board_image.blit(0, 0)

    pointer.draw()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        print('left')
    elif symbol == key.RIGHT:
        print('right')


if __name__ == '__main__':
    pyglet.app.run()
