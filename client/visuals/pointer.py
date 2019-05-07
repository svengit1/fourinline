import pyglet
import constants as const


class Pointer(pyglet.sprite.Sprite):
    column = 0
    red_image = pyglet.resource.image('assets/pointer-red.png')
    blue_image = pyglet.resource.image('assets/pointer-blue.png')

    def __init__(self, nxt):
        super().__init__(img=self.blue_image, x=const.POINTER_START_X, y=const.POINTER_START_Y)
        self.scale = const.POINTER_SCALE
        self.set_color(nxt)

    def move_left(self):
        if self.column != 0:
            self.x -= const.POINTER_MOVE
            self.column -= 1

    def move_right(self):
        if self.column != 6:
            self.x += const.POINTER_MOVE
            self.column += 1

    def set_color(self, nxt):
        if nxt == -1:
            self.image = self.blue_image
        else:
            self.image = self.red_image

    def reset_pointer(self):
        self.x = const.POINTER_START_X
        self.column = 0
