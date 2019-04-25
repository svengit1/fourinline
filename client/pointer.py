import pyglet
import constants as const


class Pointer(pyglet.sprite.Sprite):
    column = 0
    red_image = pyglet.resource.image('assets/pointer-red.png')
    blue_image = pyglet.resource.image('assets/pointer-blue.png')

    def __init__(self):
        pyglet.sprite.Sprite.__init__(self, img=self.blue_image, x=const.pointer_start_x, y=const.pointer_start_y)
        self.scale = const.pointer_scale

    def move_left(self):
        if self.column != 0:
            self.x -= const.pointer_move
            self.column -= 1

    def move_right(self):
        if self.column != 6:
            self.x += const.pointer_move
            self.column += 1

    def set_color(self, color):
        if color == 'red':
            self.image = self.red_image
        else:
            self.image = self.blue_image
