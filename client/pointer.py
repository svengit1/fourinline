import pyglet


class Pointer(pyglet.sprite.Sprite):
    column = 0
    red_image = pyglet.resource.image('assets/pointer-red.png')
    blue_image = pyglet.resource.image('assets/pointer-blue.png')

    def __init__(self):
        pyglet.sprite.Sprite.__init__(self, img=self.blue_image, x=23, y=470)
        self.scale = 0.4

    def move_left(self):
        if self.column != 0:
            self.x -= 80
            self.column -= 1

    def move_right(self):
        if self.column != 503:
            self.x += 80
            self.column += 1

    def set_color(self, color):
        if color == 'red':
            self.image = self.red_image
        else:
            self.image = self.blue_image
