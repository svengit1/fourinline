import pyglet
import constants as const


class Pointer(pyglet.sprite.Sprite):
    column = 0
    red_image = pyglet.resource.image('assets/pointer-red.png')
    blue_image = pyglet.resource.image('assets/pointer-blue.png')

    def __init__(self):
        pyglet.sprite.Sprite.__init__(self, img=self.blue_image, x=const.POINTER_START_X, y=const.POINTER_START_Y)
        self.scale = const.POINTER_SCALE

    def move_left(self):
        if self.column != 0:
            self.x -= const.POINTER_MOVE
            self.column -= 1

    def move_right(self):
        if self.column != 6:
            self.x += const.POINTER_MOVE
            self.column += 1

    def set_color(self, color):
        if color == 'red':
            self.image = self.red_image
        else:
            self.image = self.blue_image
