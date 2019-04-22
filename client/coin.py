import pyglet


class Coin(pyglet.sprite.Sprite):
    red_image = pyglet.resource.image('assets/coin-red.png')
    blue_image = pyglet.resource.image('assets/coin-blue.png')

    def __init__(self, x, y):
        pyglet.sprite.Sprite.__init__(self, self.red_image, x, y)

    def set_batch(self, batch):
        self.batch = batch

    def set_color(self, color):
        if color == 'blue':
            self.image = self.blue_image
